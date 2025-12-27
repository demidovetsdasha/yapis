from antlr4 import *
from output_dir.DashSQLParserVisitor import DashSQLParserVisitor
from output_dir.DashSQLParser import DashSQLParser


class SemanticError(Exception):
    def __init__(self, message, line=None):
        msg = "Semantic error"
        if line:
            msg += f" on line {line}"
        msg += f": {message}"
        super().__init__(msg)


class SymbolTable:
    def __init__(self, parent=None):
        self.parent = parent
        self.vars = {}
        self.tables = {}  
        self.functions = {}
        self.reactive_columns = {}

    def define_var(self, name, type_, line=None):
        if name in self.vars:
            raise SemanticError(f"Variable '{name}' already declared", line)
        self.vars[name] = type_

    def lookup_var(self, name):
        if name in self.vars:
            return self.vars[name]
        if self.parent:
            return self.parent.lookup_var(name)
        return None

    def define_table(self, name, columns, reactive_columns=None, line=None):
        if name in self.tables:
            raise SemanticError(f"Table '{name}' already exists", line)
        self.tables[name] = columns
        if reactive_columns:
            self.reactive_columns[name] = reactive_columns

    def lookup_table(self, name):
        if name in self.tables:
            return self.tables[name]
        if self.parent:
            return self.parent.lookup_table(name)
        return None

    def get_reactive_columns(self, table_name):
        if table_name in self.reactive_columns:
            return self.reactive_columns[table_name]
        if self.parent:
            return self.parent.get_reactive_columns(table_name)
        return {}

    def define_function(self, name, func_info, line=None):
        if name not in self.functions:
            self.functions[name] = []
        self.functions[name].append(func_info)

    def lookup_function(self, name, arg_count=None):
        if name not in self.functions:
            if self.parent:
                return self.parent.lookup_function(name, arg_count)
            return []
        
        if arg_count is None:
            return self.functions[name]
        
        matching_funcs = [f for f in self.functions[name] if len(f.params) == arg_count]
        return matching_funcs


class FunctionInfo:
    def __init__(self, name, params, return_type, line, parent=None):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.line = line
        self.parent_func = parent
        self.inner_funcs = []


class ReactiveColumnInfo:
    def __init__(self, name, type_, expression_context, is_block=False):
        self.name = name
        self.type = type_
        self.expression_context = expression_context
        self.is_block = is_block
        self.dependencies = []


class SemanticAnalyzer(DashSQLParserVisitor):
    def __init__(self):
        self.global_scope = SymbolTable()
        self.scope = self.global_scope
        self.current_function = None
        self.return_type = None
        self.errors = []
        self.current_table_context = None
        self.in_reactive_column = False
        self.current_reactive_column_type = None

    def add_error(self, message, ctx):
        if hasattr(ctx, "start"):
            line = ctx.start.line
        else:
            line = None
        self.errors.append(SemanticError(message, line))

    def is_numeric(self, t):
        return t in ("int", "float", "bool")

    def promote(self, t1, t2):
        if t1 == t2:
            return t1
        if t1 == "float" and t2 == "int":
            return "float"
        if t1 == "int" and t2 == "float":
            return "float"
        return None

    def is_compatible(self, expected, actual):
        if expected == actual:
            return True
        if self.promote(expected, actual) == expected:
            return True
        if expected == "date" and actual == "string":
            return True
        if (expected == "float" and actual == "int") or (expected == "int" and actual == "float"):
            return True
        return False

    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)
        return self.errors

    def visitStatement(self, ctx):
        if ctx.simple_stmt():
            return self.visit(ctx.simple_stmt())
        elif ctx.compound_stmt():
            return self.visit(ctx.compound_stmt())

    def visitSimple_stmt(self, ctx):
        if ctx.create_table_stmt():
            return self.visit(ctx.create_table_stmt())
        elif ctx.insert_stmt():
            return self.visit(ctx.insert_stmt())
        elif ctx.update_stmt():
            return self.visit(ctx.update_stmt())
        elif ctx.write_stmt():
            return self.visit(ctx.write_stmt())
        elif ctx.select_stmt():
            return self.visit(ctx.select_stmt())
        elif ctx.join_stmt():
            return self.visit(ctx.join_stmt())
        elif ctx.filter_stmt():
            return self.visit(ctx.filter_stmt())
        elif ctx.sort_stmt():
            return self.visit(ctx.sort_stmt())
        elif ctx.assignment_stmt():
            return self.visit(ctx.assignment_stmt())
        elif ctx.function_call_stmt():
            return self.visit(ctx.function_call_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())

    def visitCompound_stmt(self, ctx):
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.switch_stmt():
            return self.visit(ctx.switch_stmt())
        elif ctx.function_def():
            return self.visit(ctx.function_def())

    def visitCreate_table_stmt(self, ctx):
        table_name = ctx.ID().getText()
        columns = {}
        reactive_columns = {}
        
        for col_def in ctx.column_def_list().column_def():
            col_name = col_def.ID().getText()
            col_type = self.visit(col_def.type_name())
            
            if isinstance(col_def, DashSQLParser.SimpleColumnDefContext):
                columns[col_name] = col_type
                
                if col_def.EQUALS():
                    reactive_columns[col_name] = ReactiveColumnInfo(
                        col_name, col_type, col_def.expr(), False
                    )
            elif isinstance(col_def, DashSQLParser.ReactiveColumnDefContext):
                columns[col_name] = col_type
                reactive_columns[col_name] = ReactiveColumnInfo(
                    col_name, col_type, col_def.statement(), True
                )
        
        old_scope = self.scope
        temp_scope = SymbolTable(parent=old_scope)
        self.scope = temp_scope
        
        for col_name, col_type in columns.items():
            temp_scope.define_var(col_name, col_type)
        
        for col_name, reactive_info in reactive_columns.items():
            self.in_reactive_column = True
            self.current_reactive_column_type = reactive_info.type
            
            if reactive_info.is_block:
                for stmt in reactive_info.expression_context:
                    self.visit(stmt)
            else:
                expr_type = self.visit(reactive_info.expression_context)
                if expr_type and not self.is_compatible(reactive_info.type, expr_type):
                    self.add_error(
                        f"Type mismatch in reactive column '{col_name}': "
                        f"expected {reactive_info.type}, got {expr_type}",
                        reactive_info.expression_context
                    )
            
            self.in_reactive_column = False
            self.current_reactive_column_type = None
        
        self.scope = old_scope
        
        try:
            self.scope.define_table(table_name, columns, reactive_columns, ctx.start.line)
        except SemanticError as e:
            self.errors.append(e)

    def visitType_name(self, ctx):
        if ctx.INT_TYPE():   return "int"
        if ctx.FLOAT_TYPE(): return "float"
        if ctx.STRING_TYPE(): return "string"
        if ctx.DATE_TYPE():   return "date"
        if ctx.BOOL_TYPE():   return "bool"
        return None

    def visitInsert_stmt(self, ctx):
        tname = ctx.ID().getText()
        table = self.scope.lookup_table(tname)
        if not table:
            self.add_error(f"Unknown table '{tname}'", ctx)
            return

        if ctx.where_from_condition():
            where_ctx = ctx.where_from_condition()
            var_name = where_ctx.ID(0).getText()
            source_table_name = where_ctx.ID(1).getText()
            source_table = self.scope.lookup_table(source_table_name)
            
            if source_table:
                col_type = list(source_table.values())[0] if source_table else "int"
                self.scope.define_var(var_name, col_type, where_ctx.start.line)

        for row in ctx.insert_row():
            ids = [i.getText() for i in row.id_list().ID()]
            exprs = row.expr_list().expr()

            if len(ids) != len(exprs):
                self.add_error("Column/value mismatch", row)
                continue

            for col, expr in zip(ids, exprs):
                if col not in table:
                    self.add_error(f"Column '{col}' not found in '{tname}'", expr)
                    continue

                expr_type = self.visit(expr)
                expected = table[col]

                if expr_type is None:
                    continue

                if not self.is_compatible(expected, expr_type):
                    self.add_error(
                        f"Type mismatch for column '{col}': expected {expected}, got {expr_type}",
                        expr
                    )

    def visitUpdate_stmt(self, ctx):
        table_name = ctx.ID().getText()
        table = self.scope.lookup_table(table_name)
        
        if not table:
            self.add_error(f"Unknown table '{table_name}'", ctx)
            return
        
        for assign in ctx.update_assignment():
            col_name = assign.ID().getText()
            if col_name not in table:
                self.add_error(f"Column '{col_name}' not found in table '{table_name}'", assign)
                continue
            
            col_type = table[col_name]
            expr_type = self.visit(assign.expr())
            
            if expr_type and not self.is_compatible(col_type, expr_type):
                self.add_error(
                    f"Type mismatch in update for column '{col_name}': "
                    f"expected {col_type}, got {expr_type}",
                    assign
                )
        
        if ctx.condition():
            old_context = self.current_table_context
            self.current_table_context = table
            self.visit(ctx.condition())
            self.current_table_context = old_context

    def visitUpdate_assignment(self, ctx):
        return self.visit(ctx.expr())

    def visitWrite_stmt(self, ctx):
        if ctx.expr():
            self.visit(ctx.expr())
        elif ctx.LPAREN():
            self.visit(ctx.expr())

    def visitSelect_stmt(self, ctx):
        tname = ctx.ID(0).getText()
        table = self.scope.lookup_table(tname)
        if not table:
            self.add_error(f"Unknown table '{tname}'", ctx)
            return

        col_list = ctx.column_list()
        if not col_list.MULT():
            for c in col_list.ID():
                cname = c.getText()
                if cname not in table:
                    self.add_error(f"Unknown column '{cname}' in table '{tname}'", c)

        if ctx.where_condition():
            old_context = self.current_table_context
            self.current_table_context = table
            self.visit(ctx.where_condition())
            self.current_table_context = old_context

        if ctx.AS():
            alias = ctx.ID(1).getText()
            try:
                self.scope.define_table(alias, table.copy(), None, ctx.start.line)
            except SemanticError as e:
                self.errors.append(e)

    def visitColumn_list(self, ctx):
        return None

    def visitJoin_stmt(self, ctx):
        table1 = ctx.ID(0).getText()
        table2 = ctx.ID(1).getText()
        col1 = ctx.ID(2).getText()
        col2 = ctx.ID(3).getText()

        t1 = self.scope.lookup_table(table1)
        t2 = self.scope.lookup_table(table2)

        if not t1:
            self.add_error(f"Unknown table '{table1}'", ctx)
        if not t2:
            self.add_error(f"Unknown table '{table2}'", ctx)

        if t1 and col1 not in t1:
            self.add_error(f"Column '{col1}' not found in table '{table1}'", ctx)
        if t2 and col2 not in t2:
            self.add_error(f"Column '{col2}' not found in table '{table2}'", ctx)

        if ctx.AS():
            alias = ctx.ID(4).getText()
            combined = {}
            if t1:
                combined.update(t1)
            if t2:
                combined.update(t2)
            try:
                self.scope.define_table(alias, combined, None, ctx.start.line)
            except SemanticError as e:
                self.errors.append(e)

    def visitFilter_stmt(self, ctx):
        tname = ctx.ID(0).getText()
        table = self.scope.lookup_table(tname)
        if not table:
            self.add_error(f"Unknown table '{tname}'", ctx)
            return

        old_context = self.current_table_context
        self.current_table_context = table
        self.visit(ctx.condition())
        self.current_table_context = old_context

        if ctx.AS():
            alias = ctx.ID(1).getText()
            try:
                self.scope.define_table(alias, table.copy(), None, ctx.start.line)
            except SemanticError as e:
                self.errors.append(e)

    def visitSort_stmt(self, ctx):
        if ctx.LT():
            tname = ctx.ID(0).getText()
            sort_col = ctx.ID(1).getText()
            alias_idx = 2 if len(ctx.ID()) > 2 else -1
        else:
            tname = ctx.ID(0).getText()
            sort_col = ctx.ID(1).getText()
            alias_idx = 2 if len(ctx.ID()) > 2 else -1

        table = self.scope.lookup_table(tname)
        if not table:
            self.add_error(f"Unknown table '{tname}'", ctx)
            return

        if sort_col not in table:
            self.add_error(f"Column '{sort_col}' not found in table '{tname}'", ctx)

        if ctx.AS() and alias_idx != -1:
            alias = ctx.ID(alias_idx).getText()
            try:
                self.scope.define_table(alias, table.copy(), None, ctx.start.line)
            except SemanticError as e:
                self.errors.append(e)

    def visitAssignment_stmt(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            expr_type = self.visit(ctx.expr())

            if expr_type is None:
                return

            current_type = self.scope.lookup_var(name)
            if current_type is None:
                self.scope.define_var(name, expr_type, ctx.start.line)
            else:
                if not self.is_compatible(current_type, expr_type):
                    self.add_error(
                        f"Type mismatch: cannot assign {expr_type} to variable '{name}' of type {current_type}",
                        ctx
                    )
        else:
            ids = [id_node.getText() for id_node in ctx.id_list().ID()]
            exprs = [self.visit(expr) for expr in ctx.expr_list().expr()]
            
            if len(ids) != len(exprs):
                self.add_error(f"Assignment count mismatch: {len(ids)} variables, {len(exprs)} values", ctx)
                return
            
            for i, (name, expr_type) in enumerate(zip(ids, exprs)):
                if expr_type is None:
                    continue
                    
                current_type = self.scope.lookup_var(name)
                if current_type is None:
                    self.scope.define_var(name, expr_type, ctx.start.line)
                else:
                    if not self.is_compatible(current_type, expr_type):
                        self.add_error(
                            f"Type mismatch for variable '{name}': cannot assign {expr_type} to {current_type}",
                            ctx.expr_list().expr()[i]
                        )

    def visitId_list(self, ctx):
        return [id_node.getText() for id_node in ctx.ID()]

    def visitExpr_list(self, ctx):
        types = []
        for expr in ctx.expr():
            types.append(self.visit(expr))
        return types

    def visitFor_stmt(self, ctx):
        var_name = ctx.ID(0).getText()
        
        if ctx.expr(0) and ctx.expr(1):
            start_type = self.visit(ctx.expr(0))
            end_type = self.visit(ctx.expr(1))
            
            if start_type and start_type != "int":
                self.add_error(f"FOR range start must be integer, got {start_type}", ctx.expr(0))
            if end_type and end_type != "int":
                self.add_error(f"FOR range end must be integer, got {end_type}", ctx.expr(1))
            
            var_type = "int"
        elif ctx.ID(1):
            collection_name = ctx.ID(1).getText()
            table = self.scope.lookup_table(collection_name)
            if table:
                var_type = list(table.values())[0] if table else "int"
            else:
                self.add_error(f"Unknown table '{collection_name}'", ctx)
                var_type = "int"
        
        old_scope = self.scope
        self.scope = SymbolTable(parent=old_scope)
        self.scope.define_var(var_name, var_type, ctx.start.line)
        
        for stmt in ctx.statement():
            self.visit(stmt)
        
        self.scope = old_scope

    def visitWhile_stmt(self, ctx):
        cond_type = self.visit(ctx.condition())
        if cond_type and cond_type != "bool":
            self.add_error(f"WHILE condition must be boolean, got {cond_type}", ctx.condition())
        
        old_scope = self.scope
        self.scope = SymbolTable(parent=old_scope)
        for stmt in ctx.statement():
            self.visit(stmt)
        self.scope = old_scope

    def visitIf_stmt(self, ctx):
        cond_type = self.visit(ctx.condition())
        if cond_type and cond_type != "bool":
            self.add_error(f"IF condition must be boolean, got {cond_type}", ctx.condition())
        
        old_scope = self.scope
        self.scope = SymbolTable(parent=old_scope)
        
        then_stmts = ctx.statement()
        for stmt in then_stmts:
            self.visit(stmt)
        
        self.scope = old_scope
        
        if ctx.ELSE():
            old_scope = self.scope
            self.scope = SymbolTable(parent=old_scope)
            
            for stmt in ctx.statement():
                self.visit(stmt)
            
            self.scope = old_scope

    def visitSwitch_stmt(self, ctx):
        expr_type = self.visit(ctx.expr())
        
        for child in ctx.children:
            if isinstance(child, DashSQLParser.Case_stmtContext):
                self.visit(child)
            elif isinstance(child, DashSQLParser.Default_stmtContext):
                self.visit(child)
        
        return None

    def visitCase_stmt(self, ctx):
        if ctx.expr():
            case_expr_type = self.visit(ctx.expr())
        
        old_scope = self.scope
        self.scope = SymbolTable(parent=old_scope)
        
        for stmt in ctx.statement():
            self.visit(stmt)
        
        self.scope = old_scope
        return None

    def visitDefault_stmt(self, ctx):
        old_scope = self.scope
        self.scope = SymbolTable(parent=old_scope)
        
        for stmt in ctx.statement():
            self.visit(stmt)
        
        self.scope = old_scope
        return None

    def visitFunction_def(self, ctx):
        func_name = ctx.ID().getText()

        params = []
        if ctx.param_list():
            for p in ctx.param_list().param_def():
                p_name = p.ID().getText()
                p_type = self.visit(p.type_name())
                params.append((p_name, p_type))

        return_type = None

        func_info = FunctionInfo(
            name=func_name,
            params=params,
            return_type=return_type,
            line=ctx.start.line
        )

        self.scope.define_function(func_name, func_info)

        old_scope = self.scope
        self.scope = SymbolTable(parent=old_scope)

        for p_name, p_type in params:
            self.scope.define_var(p_name, p_type)

        old_current = self.current_function
        self.current_function = func_name

        for stmt in ctx.statement():
            self.visit(stmt)

        self.current_function = old_current
        self.scope = old_scope

        return None

    def visitParam_list(self, ctx):
        return []

    def visitParam_def(self, ctx):
        return (ctx.ID().getText(), self.visit(ctx.type_name()))

    def visitReturn_stmt(self, ctx):
        if not self.current_function:
            self.add_error("return outside function or reactive column", ctx)
            return None

        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            return expr_type

        return None

    def visitFunction_call_stmt(self, ctx):
        return self.visit(ctx.function_call())

    def visitFunction_call(self, ctx):
        func_name = ctx.ID().getText()
        arg_exprs = ctx.expr_list().expr() if ctx.expr_list() else []
        arg_count = len(arg_exprs)

        current = self.scope
        all_funcs = []
        while current:
            if func_name in current.functions:
                all_funcs.extend(current.functions[func_name])
            current = current.parent

        matching_funcs = [f for f in all_funcs if len(f.params) == arg_count]

        if not matching_funcs:
            self.add_error(f"Unknown function '{func_name}' with {arg_count} arguments", ctx)
            return "bool"

        func_info = matching_funcs[0]

        for i, arg_ctx in enumerate(arg_exprs):
            if i < len(func_info.params):
                expected = func_info.params[i][1]
                actual = self.visit(arg_ctx)
                if actual and not self.is_compatible(expected, actual):
                    self.add_error(
                        f"Argument {i+1} type mismatch in '{func_name}': expected {expected}, got {actual}",
                        arg_ctx
                    )

        return func_info.return_type or "bool"

    def visitIsExpr(self, ctx):
        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))
        return "bool"

    def visitComparisonExpr(self, ctx):
        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))

        if t1 and t2:
            if self.is_numeric(t1) and self.is_numeric(t2):
                pass
            elif t1 != t2:
                if not ((t1 == "string" and t2 == "string") or
                        (t1 == "date" and t2 == "string") or
                        (t2 == "date" and t1 == "string")):
                    op = ctx.getChild(1).getText()
                    self.add_error(
                        f"Incompatible types for comparison '{op}': {t1} and {t2}",
                        ctx
                    )
        return "bool"

    def visitAddSubExpr(self, ctx):
        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))

        if self.is_numeric(t1) and self.is_numeric(t2):
            return self.promote(t1, t2) or "int"
        if t1 == "bool" and self.is_numeric(t2):
            return t2 if t2 != "bool" else "int"
        if t2 == "bool" and self.is_numeric(t1):
            return t1 if t1 != "bool" else "int"

        if t1 == "string" and t2 == "string" and ctx.PLUS():
            return "string"

        if t1 and t2:
            if not (t1 == "string" and t2 == "string" and ctx.PLUS()):
                self.add_error(
                    f"Invalid operation: cannot apply '{ctx.getChild(1).getText()}' to {t1} and {t2}",
                    ctx
                )
        return "int"

    def visitMulDivExpr(self, ctx):
        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))

        def normalize_numeric(t):
            if t in ("int", "float", "bool"):
                return t
            return None

        n1 = normalize_numeric(t1)
        n2 = normalize_numeric(t2)

        if ctx.MOD():
            if n1 in ("int", "bool") and n2 in ("int", "bool"):
                return "int"
            if t1 and t2:
                self.add_error(f"MOD operation requires integers or bool, got {t1} and {t2}", ctx)
            return "int"

        # Обычные * и /
        if n1 and n2:
            if "float" in (t1, t2):
                return "float"
            return "int"

        if t1 and t2:
            self.add_error(
                f"Invalid operation: cannot apply '{ctx.getChild(1).getText()}' to {t1} and {t2}",
                ctx
            )
        return "int"

    def visitNotExpr(self, ctx):
        expr_type = self.visit(ctx.expr())
        if expr_type and expr_type != "bool":
            self.add_error(f"NOT operation requires boolean, got {expr_type}", ctx)
        return "bool"

    def visitArrayAccessExpr(self, ctx):
        name = ctx.ID().getText()
        index_type = self.visit(ctx.expr())
        
        if index_type and index_type != "int":
            self.add_error(f"Array index must be integer, got {index_type}", ctx.expr())
        
        var_type = self.scope.lookup_var(name)
        if not var_type:
            table = self.current_table_context
            if table and name in table:
                return table[name]
            self.add_error(f"Unknown variable '{name}'", ctx)
            return "string"
        
        return "string"

    def visitFunctionCallExpr(self, ctx):
        return self.visit(ctx.function_call())

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.expr():
            return self.visit(ctx.expr())
        
        if ctx.literal_value():
            return self.visit(ctx.literal_value())
        
        if ctx.ID():
            name = ctx.ID().getText()
            
            var_type = self.scope.lookup_var(name)
            if var_type:
                return var_type
            
            if self.current_table_context and name in self.current_table_context:
                return self.current_table_context[name]
            
            table = self.scope.lookup_table(name)
            if table:
                return "table"
            
        return None

    def visitLiteral_value(self, ctx):
        if ctx.INTEGER():
            return "int"
        elif ctx.FLOAT_NUM():
            return "float"
        elif ctx.STRING_LIT():
            return "string"
        elif ctx.TRUE_LIT() or ctx.FALSE_LIT():
            return "bool"
        return None

    def visitCondition(self, ctx):
        for expr_ctx in ctx.expr():
            expr_type = self.visit(expr_ctx)
            pass
        return "bool"

    def visitSimpleColumnDef(self, ctx):
        col_name = ctx.ID().getText()
        col_type = self.visit(ctx.type_name())
        
        if ctx.EQUALS():
            expr_type = self.visit(ctx.expr())
            if expr_type and not self.is_compatible(col_type, expr_type):
                self.add_error(
                    f"Type mismatch in column '{col_name}': expected {col_type}, got {expr_type}",
                    ctx.expr()
                )
        
        return col_type

    def visitReactiveColumnDef(self, ctx):
        col_name = ctx.ID().getText()
        col_type = self.visit(ctx.type_name())
        return col_type

    def visitColumn_def_list(self, ctx):
        for col_def in ctx.column_def():
            self.visit(col_def)
        return None

    def visitWhere_condition(self, ctx):
        return self.visit(ctx.condition())

    def visitWhere_from_condition(self, ctx):
        var_name = ctx.ID(0).getText()
        table_name = ctx.ID(1).getText()
        
        table = self.scope.lookup_table(table_name)
        if table:
            col_type = list(table.values())[0] if table else "int"
            self.scope.define_var(var_name, col_type, ctx.start.line)
        
        return None

    def visitInsert_row(self, ctx):
        ids = [id_node.getText() for id_node in ctx.id_list().ID()]
        expr_types = [self.visit(expr) for expr in ctx.expr_list().expr()]
        return list(zip(ids, expr_types))


def analyze_semantics(tree):
    analyzer = SemanticAnalyzer()
    analyzer.visit(tree)
    return analyzer.errors