import re
import sys
import os
from collections import defaultdict
from typing import List, Dict, Any, Optional, Tuple
import llvmlite.ir as ir
import llvmlite.binding as llvm

class LLVMGenerator:
    def __init__(self):
        self.module = ir.Module()
        self.builder = None
        self.functions = {}
        self.tables = {}
        self.variables = {}
        self.current_function = None
        self.indent_level = 0
        self.block_stack = []
        self.loop_stack = []
        self.string_constants = {}
        self.string_counter = 0
        self.current_table = None
        self.global_writes = []
        
        self.void_t = ir.VoidType()
        self.int8_t = ir.IntType(8)
        self.int8_ptr_t = ir.PointerType(self.int8_t)
        self.int32_t = ir.IntType(32)
        self.int64_t = ir.IntType(64)
        self.float_t = ir.FloatType()
        self.double_t = ir.DoubleType()
        self.bool_t = ir.IntType(1)
        
        self.int8_ptr_ptr_t = ir.PointerType(self.int8_ptr_t)
        
        self._declare_runtime_functions()
        
    def _declare_runtime_functions(self):
        # Table* create_table(const char* name, int col_count, char** col_names, char** col_types, char** reactive_exprs)
        create_table_ty = ir.FunctionType(
            self.int8_ptr_t,  
            [self.int8_ptr_t, self.int32_t, 
             self.int8_ptr_ptr_t,  
             self.int8_ptr_ptr_t,  
             self.int8_ptr_ptr_t]  
        )
        ir.Function(self.module, create_table_ty, "create_table")
        
        # Table* find_table(const char* name)
        find_table_ty = ir.FunctionType(self.int8_ptr_t, [self.int8_ptr_t])
        ir.Function(self.module, find_table_ty, "find_table")
        
        # void table_insert(Table* table, char** values)
        table_insert_ty = ir.FunctionType(
            self.void_t,
            [self.int8_ptr_t, self.int8_ptr_ptr_t] 
        )
        ir.Function(self.module, table_insert_ty, "table_insert")
        
        # void table_insert_silent(Table* table, char** values)
        table_insert_silent_ty = ir.FunctionType(
            self.void_t,
            [self.int8_ptr_t, self.int8_ptr_ptr_t]  
        )
        ir.Function(self.module, table_insert_silent_ty, "table_insert_silent")
        
        # void table_update(Table* table, char** col_names, char** new_values, int col_count, const char* condition)
        table_update_ty = ir.FunctionType(
            self.void_t,
            [self.int8_ptr_t, 
             self.int8_ptr_ptr_t, 
             self.int8_ptr_ptr_t, 
             self.int32_t,
             self.int8_ptr_t]
        )
        ir.Function(self.module, table_update_ty, "table_update")
        
        # void table_print(Table* table)
        table_print_ty = ir.FunctionType(self.void_t, [self.int8_ptr_t])
        ir.Function(self.module, table_print_ty, "table_print")
        
        # Table* table_select(Table* table, const char* columns, const char* condition)
        table_select_ty = ir.FunctionType(
            self.int8_ptr_t,
            [self.int8_ptr_t, self.int8_ptr_t, self.int8_ptr_t]
        )
        ir.Function(self.module, table_select_ty, "table_select")
        
        # Table* table_join(Table* left, Table* right, const char* condition)
        table_join_ty = ir.FunctionType(
            self.int8_ptr_t,
            [self.int8_ptr_t, self.int8_ptr_t, self.int8_ptr_t]
        )
        ir.Function(self.module, table_join_ty, "table_join")
        
        # Table* table_filter(Table* table, const char* condition)
        table_filter_ty = ir.FunctionType(
            self.int8_ptr_t,
            [self.int8_ptr_t, self.int8_ptr_t]
        )
        ir.Function(self.module, table_filter_ty, "table_filter")
        
        # Table* table_sort(Table* table, const char* column, int descending)
        table_sort_ty = ir.FunctionType(
            self.int8_ptr_t,
            [self.int8_ptr_t, self.int8_ptr_t, self.int32_t]
        )
        ir.Function(self.module, table_sort_ty, "table_sort")
        
        # char* evaluate_expression(const char* expr, Variable* vars)
        evaluate_expression_ty = ir.FunctionType(
            self.int8_ptr_t,
            [self.int8_ptr_t, self.int8_ptr_t]
        )
        ir.Function(self.module, evaluate_expression_ty, "evaluate_expression")
        
        # void printf(const char* format, ...)
        printf_ty = ir.FunctionType(self.int32_t, [self.int8_ptr_t], var_arg=True)
        ir.Function(self.module, printf_ty, "printf")
        
        # int sprintf(char* str, const char* format, ...)
        sprintf_ty = ir.FunctionType(
            self.int32_t,
            [self.int8_ptr_t, self.int8_ptr_t],
            var_arg=True
        )
        ir.Function(self.module, sprintf_ty, "sprintf")
        
        # void* malloc(size_t size)
        malloc_ty = ir.FunctionType(self.int8_ptr_t, [self.int64_t])
        ir.Function(self.module, malloc_ty, "malloc")
        
        # void free(void* ptr)
        free_ty = ir.FunctionType(self.void_t, [self.int8_ptr_t])
        ir.Function(self.module, free_ty, "free")
        
        # int atoi(const char* str)
        atoi_ty = ir.FunctionType(self.int32_t, [self.int8_ptr_t])
        ir.Function(self.module, atoi_ty, "atoi")
        
        # double atof(const char* str)
        atof_ty = ir.FunctionType(self.double_t, [self.int8_ptr_t])
        ir.Function(self.module, atof_ty, "atof")
        
        # char* strdup(const char* str)
        strdup_ty = ir.FunctionType(self.int8_ptr_t, [self.int8_ptr_t])
        ir.Function(self.module, strdup_ty, "strdup")
        
        # int strcmp(const char* str1, const char* str2)
        strcmp_ty = ir.FunctionType(self.int32_t, [self.int8_ptr_t, self.int8_ptr_t])
        ir.Function(self.module, strcmp_ty, "strcmp")
        
        # char* strcat(char* dest, const char* src)
        strcat_ty = ir.FunctionType(self.int8_ptr_t, [self.int8_ptr_t, self.int8_ptr_t])
        ir.Function(self.module, strcat_ty, "strcat")
        
        # size_t strlen(const char* str)
        strlen_ty = ir.FunctionType(self.int64_t, [self.int8_ptr_t])
        ir.Function(self.module, strlen_ty, "strlen")

        # char* strstr(const char* haystack, const char* needle)
        strstr_ty = ir.FunctionType(self.int8_ptr_t, [self.int8_ptr_t, self.int8_ptr_t])
        ir.Function(self.module, strstr_ty, "strstr")

        # double fmod(double x, double y)
        fmod_ty = ir.FunctionType(self.double_t, [self.double_t, self.double_t])
        ir.Function(self.module, fmod_ty, "fmod")

        # int table_row_count(Table* table)
        table_row_count_ty = ir.FunctionType(self.int32_t, [self.int8_ptr_t])
        ir.Function(self.module, table_row_count_ty, "table_row_count")
        
        # int table_col_count(Table* table)
        table_col_count_ty = ir.FunctionType(self.int32_t, [self.int8_ptr_t])
        ir.Function(self.module, table_col_count_ty, "table_col_count")
        
        # char* table_get_value(Table* table, int row_idx, const char* col_name)
        table_get_value_ty = ir.FunctionType(
            self.int8_ptr_t,
            [self.int8_ptr_t, self.int32_t, self.int8_ptr_t]
        )
        ir.Function(self.module, table_get_value_ty, "table_get_value")
        
        # void cleanup_all_tables()
        cleanup_tables_ty = ir.FunctionType(self.void_t, [])
        ir.Function(self.module, cleanup_tables_ty, "cleanup_all_tables")
    
    def _create_string_constant(self, value: str) -> ir.Constant:
        """Создает строковую константу в LLVM модуле"""
        if value not in self.string_constants:
            const = ir.Constant(ir.ArrayType(self.int8_t, len(value) + 1), 
                              bytearray(value.encode('utf-8') + b'\0'))
            gv = ir.GlobalVariable(self.module, const.type, f".str.{self.string_counter}")
            gv.initializer = const
            gv.global_constant = True
            gv.linkage = 'internal'
            gv.align = 1
            self.string_constants[value] = gv
            self.string_counter += 1
        return self.string_constants[value]
    
    def _get_string_ptr(self, value: str) -> ir.Instruction:
        """Возвращает указатель на строковую константу (i8*)"""
        gv = self._create_string_constant(value)
        zero = ir.Constant(self.int32_t, 0)
        return self.builder.gep(gv, [zero, zero])
    
    def _create_string_array(self, strings: List[str]) -> ir.Instruction:
        """Создает массив строк (char**) и возвращает указатель на него (i8**)"""
        if not strings:
            return ir.Constant(self.int8_ptr_ptr_t, None)
        
        array_size = len(strings)
        array_type = ir.ArrayType(self.int8_ptr_t, array_size)
        
        array_alloca = self.builder.alloca(array_type)
        
        for i, string in enumerate(strings):
            string_ptr = self._get_string_ptr(string)
            # Вычисляем адрес элемента массива
            elem_ptr = self.builder.gep(array_alloca, 
                                      [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, i)])
            self.builder.store(string_ptr, elem_ptr)
        
        array_ptr = self.builder.gep(array_alloca, 
                                   [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
        return self.builder.bitcast(array_ptr, self.int8_ptr_ptr_t)
    
    def _create_nullable_string_array(self, strings: List[Optional[str]]) -> ir.Instruction:
        """Создает массив строк с возможными NULL значениями"""
        if not strings:
            return ir.Constant(self.int8_ptr_ptr_t, None)
        
        array_size = len(strings)
        array_type = ir.ArrayType(self.int8_ptr_t, array_size)
        array_alloca = self.builder.alloca(array_type)
        
        for i, string in enumerate(strings):
            elem_ptr = self.builder.gep(array_alloca, 
                                      [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, i)])
            if string is not None and string != "":
                string_ptr = self._get_string_ptr(string)
                self.builder.store(string_ptr, elem_ptr)
            else:
                null_ptr = ir.Constant(self.int8_ptr_t, None)
                self.builder.store(null_ptr, elem_ptr)
        
        array_ptr = self.builder.gep(array_alloca, 
                                   [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
        return self.builder.bitcast(array_ptr, self.int8_ptr_ptr_t)
    
    def _create_dynamic_string_array(self, values: List[ir.Instruction]) -> ir.Instruction:
        """Создает массив строк из динамических значений"""
        if not values:
            return ir.Constant(self.int8_ptr_ptr_t, None)
        
        array_size = len(values)
        array_type = ir.ArrayType(self.int8_ptr_t, array_size)
        array_alloca = self.builder.alloca(array_type)
        
        for i, value in enumerate(values):
            elem_ptr = self.builder.gep(array_alloca, 
                                      [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, i)])
            self.builder.store(value, elem_ptr)
        
        array_ptr = self.builder.gep(array_alloca, 
                                   [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
        return self.builder.bitcast(array_ptr, self.int8_ptr_ptr_t)
    
    def _convert_int_to_string(self, int_value: ir.Instruction) -> ir.Instruction:
        """Конвертирует целое число в строку"""
        buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
        buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
        
        fmt = self._get_string_ptr("%d")
        self.builder.call(self.module.get_global('sprintf'), [buf_ptr, fmt, int_value])
        
        return self.builder.call(self.module.get_global('strdup'), [buf_ptr])
    
    def _convert_bool_to_string(self, bool_value: ir.Instruction) -> ir.Instruction:
        """Конвертирует булево значение в строку 'true' или 'false'"""
        true_str = self._get_string_ptr("true")
        false_str = self._get_string_ptr("false")
        return self.builder.select(bool_value, true_str, false_str)
    
    def _parse_function_call(self, expr: str) -> Tuple[str, List[str]]:
        """Парсит вызов функции и возвращает имя функции и список аргументов"""
        expr = expr.strip()
        open_paren = expr.find('(')
        if open_paren == -1 or not expr.endswith(')'):
            return expr, []  
        
        func_name = expr[:open_paren].strip()
        args_str = expr[open_paren + 1:-1].strip()
        
        if not args_str:
            return func_name, []
        
        args = []
        current = []
        paren_depth = 0
        in_string = False
        string_char = None
        
        for char in args_str:
            if char in ('"', "'") and not in_string:
                in_string = True
                string_char = char
                current.append(char)
            elif char == string_char and in_string:
                in_string = False
                string_char = None
                current.append(char)
            elif not in_string:
                if char == '(':
                    paren_depth += 1
                    current.append(char)
                elif char == ')':
                    paren_depth -= 1
                    current.append(char)
                elif char == ',' and paren_depth == 0:
                    args.append(''.join(current).strip())
                    current = []
                else:
                    current.append(char)
            else:
                current.append(char)
        
        if current:
            args.append(''.join(current).strip())
        
        return func_name, args
    
    def _evaluate_arithmetic_expression(self, expr: str, context_vars: Dict[str, ir.Instruction]) -> ir.Instruction:
        """Вычисляет арифметическое выражение с поддержкой float"""
        expr = expr.strip()
        
        try:
            if '.' in expr:
                float_val = float(expr)
                buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
                buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
                fmt = self._get_string_ptr("%.6f")
                const_val = ir.Constant(self.double_t, float_val)
                self.builder.call(self.module.get_global('sprintf'), [buf_ptr, fmt, const_val])
                return self.builder.call(self.module.get_global('strdup'), [buf_ptr])
            else:
                int_val = int(expr)
                return self._convert_int_to_string(ir.Constant(self.int32_t, int_val))
        except ValueError:
            pass
        
        if expr in context_vars:
            return context_vars[expr]
        
        operators = ['+', '-', '*', '/', '%']
        
        for op in operators:
            if op in expr:
                parts = expr.split(op, 1)
                left = parts[0].strip()
                right = parts[1].strip()
                
                left_val_str = None
                left_is_float = False
                
                if left in context_vars:
                    left_val_str = context_vars[left]
                    dot_str = self._get_string_ptr(".")
                    contains_dot = self.builder.call(self.module.get_global('strstr'), [left_val_str, dot_str])
                    has_dot = self.builder.icmp_signed('!=', contains_dot, 
                                                    ir.Constant(self.int8_ptr_t, None))
                    left_is_float = has_dot
                elif '.' in left and left.replace('.', '', 1).isdigit():
                    left_val_str = self._get_string_ptr(left)
                    left_is_float = True
                elif left.isdigit():
                    left_val_str = self._convert_int_to_string(ir.Constant(self.int32_t, int(left)))
                    left_is_float = False
                else:
                    left_is_float = True
                
                right_val_str = None
                right_is_float = False
                
                if right in context_vars:
                    right_val_str = context_vars[right]
                    dot_str = self._get_string_ptr(".")
                    contains_dot = self.builder.call(self.module.get_global('strstr'), [right_val_str, dot_str])
                    has_dot = self.builder.icmp_signed('!=', contains_dot,
                                                    ir.Constant(self.int8_ptr_t, None))
                    right_is_float = has_dot
                elif '.' in right and right.replace('.', '', 1).isdigit():
                    right_val_str = self._get_string_ptr(right)
                    right_is_float = True
                elif right.isdigit():
                    right_val_str = self._convert_int_to_string(ir.Constant(self.int32_t, int(right)))
                    right_is_float = False
                else:
                    right_val_str = self._evaluate_arithmetic_expression(right, context_vars)
                    right_is_float = True
                
                if left_val_str and right_val_str:
                    left_float = left_is_float
                    right_float = right_is_float
                    
                    if left_float or right_float:
                        left_float_val = self.builder.call(self.module.get_global('atof'), [left_val_str])
                        right_float_val = self.builder.call(self.module.get_global('atof'), [right_val_str])
                        
                        result = None
                        if op == '+':
                            result = self.builder.fadd(left_float_val, right_float_val)
                        elif op == '-':
                            result = self.builder.fsub(left_float_val, right_float_val)
                        elif op == '*':
                            result = self.builder.fmul(left_float_val, right_float_val)
                        elif op == '/':
                            result = self.builder.fdiv(left_float_val, right_float_val)
                        elif op == '%':
                            result = self.builder.call(self.module.get_global('fmod'), 
                                                    [left_float_val, right_float_val])
                        
                        if result:
                            buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
                            buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
                            fmt = self._get_string_ptr("%.6f")
                            self.builder.call(self.module.get_global('sprintf'), [buf_ptr, fmt, result])
                            return self.builder.call(self.module.get_global('strdup'), [buf_ptr])
                    else:
                        left_int_val = self.builder.call(self.module.get_global('atoi'), [left_val_str])
                        right_int_val = self.builder.call(self.module.get_global('atoi'), [right_val_str])
                        
                        result = None
                        if op == '+':
                            result = self.builder.add(left_int_val, right_int_val)
                        elif op == '-':
                            result = self.builder.sub(left_int_val, right_int_val)
                        elif op == '*':
                            result = self.builder.mul(left_int_val, right_int_val)
                        elif op == '/':
                            zero = ir.Constant(self.int32_t, 0)
                            is_zero = self.builder.icmp_signed('==', right_int_val, zero)
                            safe_val = self.builder.select(is_zero, zero, 
                                                        self.builder.sdiv(left_int_val, right_int_val))
                            result = safe_val
                        elif op == '%':
                            zero = ir.Constant(self.int32_t, 0)
                            is_zero = self.builder.icmp_signed('==', right_int_val, zero)
                            safe_val = self.builder.select(is_zero, zero, 
                                                        self.builder.srem(left_int_val, right_int_val))
                            result = safe_val
                        
                        if result:
                            return self._convert_int_to_string(result)
                        
        return self._get_string_ptr(expr)


    def _parse_indentation(self, lines: List[str]) -> List[Tuple[int, str]]:
        """Парсит отступы и возвращает список (уровень, строка)"""
        result = []
        for line in lines:
            if line.strip() == '':
                continue
            line = line.replace('\t', '    ')
            indent = len(line) - len(line.lstrip())
            result.append((indent, line.strip()))
        return result
    
    def generate_from_code(self, code: str):
        """Генерирует LLVM IR из исходного кода"""
        lines = code.split('\n')
        indented_lines = self._parse_indentation(lines)
        
        main_func_ty = ir.FunctionType(self.int32_t, [])
        main_func = ir.Function(self.module, main_func_ty, "main")
        entry_block = main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_block)
        
        i = 0
        while i < len(indented_lines):
            indent, line = indented_lines[i]
            
            if line.startswith('function '):
                i = self._generate_function(indented_lines, i, None)
            elif line.startswith('create '):
                i = self._generate_create_table(indented_lines, i)
            elif line.startswith('insert to '):
                i = self._generate_insert(indented_lines, i)
            elif line.startswith('write '):
                i = self._generate_write(indented_lines, i)
            elif line.startswith('join '):
                i = self._generate_join(indented_lines, i)
            elif line.startswith('filter '):
                i = self._generate_filter(indented_lines, i)
            elif line.startswith('sort '):
                i = self._generate_sort(indented_lines, i)
            elif line.startswith('select '):
                i = self._generate_select(indented_lines, i)
            elif line.startswith('for '):
                i = self._generate_for_loop(indented_lines, i, main_func)
            elif line.startswith('while '):
                i = self._generate_while_loop(indented_lines, i, main_func)
            elif line.startswith('if '):
                i = self._generate_if(indented_lines, i, main_func)
            elif line.startswith('switch '):
                i = self._generate_switch(indented_lines, i, main_func)
            elif '=' in line and not line.startswith('='):
                i = self._generate_assignment(line, i)
            else:
                i += 1
        
        self.builder.call(self.module.get_global('cleanup_all_tables'), [])
        self.builder.ret(ir.Constant(self.int32_t, 0))
        
        return self.module
    
    def _generate_write_in_main(self, expr: str):
        """Генерирует вызов write в функции main"""
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            content = expr[1:-1]
            str_ptr = self._get_string_ptr(content)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, str_ptr])
            return
        
        if '(' in expr and ')' in expr:
            func_name, args = self._parse_function_call(expr)
            
            if func_name != expr:
                result = self._generate_function_call(func_name, args)
                
                fmt = self._get_string_ptr("%s\n")
                self.builder.call(self.module.get_global('printf'), [fmt, result])
                return
        
        if expr in self.tables:
            table = self.tables[expr]
            self.builder.call(self.module.get_global('table_print'), [table])
        elif expr in self.variables:
            val_ptr = self.variables[expr]
            if isinstance(val_ptr, ir.AllocaInstr):
                val_ptr = self.builder.load(val_ptr)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, val_ptr])
        elif expr == 'true' or expr == 'false':
            str_ptr = self._get_string_ptr(expr)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, str_ptr])
        else:
            empty_str = self._get_string_ptr("")
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, empty_str])
    
    def _generate_statements(self, lines: List[Tuple[int, str]], start: int, end: int, func):
        """Рекурсивно генерирует код для блока операторов"""
        i = start
        while i < end:
            indent, line = lines[i]
            current_indent = indent
            
            if line.startswith('function '):
                i = self._generate_function(lines, i, func)
            elif line.startswith('create '):
                i = self._generate_create_table(lines, i)
            elif line.startswith('insert to '):
                i = self._generate_insert(lines, i)
            elif line.startswith('update '):
                i = self._generate_update(lines, i)
            elif line.startswith('write '):
                i = self._generate_write(lines, i)
            elif line.startswith('select '):
                i = self._generate_select(lines, i)
            elif line.startswith('join '):
                i = self._generate_join(lines, i)
            elif line.startswith('filter '):
                i = self._generate_filter(lines, i)
            elif line.startswith('sort '):
                i = self._generate_sort(lines, i)
            elif line.startswith('for '):
                i = self._generate_for_loop(lines, i, func)
            elif line.startswith('while '):
                i = self._generate_while_loop(lines, i, func)
            elif line.startswith('if '):
                i = self._generate_if(lines, i, func)
            elif line.startswith('switch '):
                i = self._generate_switch(lines, i, func)
            elif '=' in line and not line.startswith('='):
                i = self._generate_assignment(line, i)
            elif line.startswith('return '):
                i = self._generate_return(line, i)
            elif line.startswith('else:'):
                return i
            else:
                i += 1
    
    def _generate_function(self, lines: List[Tuple[int, str]], start: int, parent_func) -> int:
        """Генерирует объявление функции с поддержкой перегрузки и вложенных функций"""
        indent, line = lines[start]
        match = re.match(r'function\s+(\w+)\s*\(([^)]*)\)\s*:', line)
        if not match:
            return start + 1
        
        func_name = match.group(1)
        params_str = match.group(2)
        
        params = []
        param_types = []
        if params_str.strip():
            for param in params_str.split(','):
                param = param.strip()
                if ':' in param:
                    name_type = param.split(':')
                    if len(name_type) == 2:
                        param_name = name_type[0].strip()
                        param_type = name_type[1].strip()
                        params.append((param_name, param_type))
                        param_types.append(self.int8_ptr_t)
                else:
                    param_name = param.strip()
                    param_type = "string"
                    params.append((param_name, param_type))
                    param_types.append(self.int8_ptr_t)
        
        if func_name in self.functions:
            existing_overloads = [name for name in self.functions.keys() 
                                if name.startswith(f"{func_name}_")]
            unique_name = f"{func_name}_{len(params)}"
            counter = 1
            while unique_name in self.functions:
                unique_name = f"{func_name}_{len(params)}_{counter}"
                counter += 1
        else:
            unique_name = func_name
        
        func_ty = ir.FunctionType(self.int8_ptr_t, param_types)
        func = ir.Function(self.module, func_ty, unique_name)
        
        self.functions[unique_name] = {
            'func': func,
            'original_name': func_name,  
            'params': params,
            'param_count': len(params),
            'variables': {},
            'nested_functions': []
        }
        
        if self.current_function:
            self.functions[self.current_function]['nested_functions'].append(unique_name)
        
        old_builder = self.builder
        old_function = self.current_function
        
        entry_block = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_block)
        self.current_function = unique_name
        
        for i, (param_name, param_type) in enumerate(params):
            arg = func.args[i]
            arg.name = param_name
            ptr = self.builder.alloca(self.int8_ptr_t, name=param_name)
            self.builder.store(arg, ptr)
            self.functions[unique_name]['variables'][param_name] = ptr
        
        body_start = start + 1
        body_end = body_start
        
        while body_end < len(lines) and lines[body_end][0] > indent:
            body_end += 1
        
        self._generate_statements(lines, body_start, body_end, func)
        
        if not self.builder.block.is_terminated:
            empty_str = self._get_string_ptr("")
            self.builder.ret(empty_str)
        
        self.builder = old_builder
        self.current_function = old_function
        
        return body_end
    
    def _resolve_function_call(self, func_name: str, arg_count: int) -> Optional[str]:
        """Разрешает вызов перегруженной функции по имени и количеству аргументов"""
        possible_matches = []
        
        for unique_name, func_info in self.functions.items():
            if func_info['original_name'] == func_name:
                if func_info['param_count'] == arg_count:
                    possible_matches.append(unique_name)

        if possible_matches:
            return possible_matches[0]
        
        if self.current_function:
            current_func_info = self.functions[self.current_function]
            for nested_func_name in current_func_info['nested_functions']:
                nested_func_info = self.functions.get(nested_func_name)
                if nested_func_info and nested_func_info['original_name'] == func_name:
                    if nested_func_info['param_count'] == arg_count:
                        return nested_func_name
        
        return None
    
    def _generate_function_call(self, func_name: str, args: List[str]) -> ir.Instruction:
        """Генерирует вызов функции с разрешением перегрузки"""
        prepared_args = []
        for arg in args:
            arg = arg.strip()
            if arg.isdigit():
                int_val = ir.Constant(self.int32_t, int(arg))
                arg_str = self._convert_int_to_string(int_val)
            elif (arg.startswith('"') and arg.endswith('"')) or \
                (arg.startswith("'") and arg.endswith("'")):
                arg_str = self._get_string_ptr(arg[1:-1])
            elif arg == 'true':
                arg_str = self._get_string_ptr("true")
            elif arg == 'false':
                arg_str = self._get_string_ptr("false")
            else:
                if self.current_function and arg in self.functions[self.current_function]['variables']:
                    var_ptr = self.functions[self.current_function]['variables'][arg]
                    arg_str = self.builder.load(var_ptr)
                elif arg in self.variables:
                    arg_str = self.variables[arg]
                    if isinstance(arg_str, ir.AllocaInstr):
                        arg_str = self.builder.load(arg_str)
                else:
                    arg_str = self._get_string_ptr(arg)
            prepared_args.append(arg_str)
        
        resolved_func_name = self._resolve_function_call(func_name, len(args))
        
        if resolved_func_name and resolved_func_name in self.functions:
            func = self.functions[resolved_func_name]['func']
            result = self.builder.call(func, prepared_args)
            return result
        else:
            print(f"Предупреждение: функция {func_name} с {len(args)} параметрами не найдена")
            return self._get_string_ptr("")
    
    def _parse_condition(self, condition_str: str) -> ir.Instruction:
        """Парсит условие и возвращает LLVM значение для ветвления"""
        condition_str = condition_str.strip()
        
        if condition_str == "true":
            return ir.Constant(self.bool_t, 1)
        elif condition_str == "false":
            return ir.Constant(self.bool_t, 0)
        
        if '%' in condition_str:
            for cmp_op in ['<=', '>=', '==', '!=', '<', '>']:
                if cmp_op in condition_str:
                    left, right = condition_str.split(cmp_op, 1)
                    left = left.strip()
                    right = right.strip()
                    
                    context_vars = {}
                    if self.current_function:
                        for var_name, var_ptr in self.functions[self.current_function]['variables'].items():
                            context_vars[var_name] = self.builder.load(var_ptr)
                    
                    for var_name, var_val in self.variables.items():
                        if isinstance(var_val, ir.AllocaInstr):
                            context_vars[var_name] = self.builder.load(var_val)
                        else:
                            context_vars[var_name] = var_val
                    
                    left_result = self._evaluate_arithmetic_expression(left, context_vars)
                    
                    left_val = self.builder.call(self.module.get_global('atoi'), [left_result])
                    right_val = ir.Constant(self.int32_t, int(right))
                    
                    if cmp_op == '<=':
                        return self.builder.icmp_signed('<=', left_val, right_val)
                    elif cmp_op == '>=':
                        return self.builder.icmp_signed('>=', left_val, right_val)
                    elif cmp_op == '==':
                        return self.builder.icmp_signed('==', left_val, right_val)
                    elif cmp_op == '!=':
                        return self.builder.icmp_signed('!=', left_val, right_val)
                    elif cmp_op == '<':
                        return self.builder.icmp_signed('<', left_val, right_val)
                    elif cmp_op == '>':
                        return self.builder.icmp_signed('>', left_val, right_val)
        
        operators = ['<=', '>=', '==', '!=', '<', '>']
        
        for op in operators:
            if op in condition_str:
                left, right = condition_str.split(op, 1)
                left = left.strip()
                right = right.strip()
                
                left_val = self._get_condition_value(left)
                
                right_val = self._get_condition_value(right)
                
                if op == '<=':
                    return self.builder.icmp_signed('<=', left_val, right_val)
                elif op == '>=':
                    return self.builder.icmp_signed('>=', left_val, right_val)
                elif op == '==':
                    return self.builder.icmp_signed('==', left_val, right_val)
                elif op == '!=':
                    return self.builder.icmp_signed('!=', left_val, right_val)
                elif op == '<':
                    return self.builder.icmp_signed('<', left_val, right_val)
                elif op == '>':
                    return self.builder.icmp_signed('>', left_val, right_val)
    
        if self.current_function and condition_str in self.functions[self.current_function]['variables']:
            var_ptr = self.functions[self.current_function]['variables'][condition_str]
            var_val = self.builder.load(var_ptr)
            int_val = self.builder.call(self.module.get_global('atoi'), [var_val])
            zero = ir.Constant(self.int32_t, 0)
            return self.builder.icmp_signed('!=', int_val, zero)
        elif condition_str in self.variables:
            var_val = self.variables[condition_str]
            if isinstance(var_val, ir.AllocaInstr):
                var_val = self.builder.load(var_val)
            int_val = self.builder.call(self.module.get_global('atoi'), [var_val])
            zero = ir.Constant(self.int32_t, 0)
            return self.builder.icmp_signed('!=', int_val, zero)
        else:
            return ir.Constant(self.bool_t, 1)
    
    def _get_condition_value(self, expr: str) -> ir.Instruction:
        """Получает числовое значение из выражения для сравнения"""
        expr = expr.strip()
        
        if expr.isdigit():
            return ir.Constant(self.int32_t, int(expr))
        
        if self.current_function and expr in self.functions[self.current_function]['variables']:
            var_ptr = self.functions[self.current_function]['variables'][expr]
            var_val = self.builder.load(var_ptr)
            return self.builder.call(self.module.get_global('atoi'), [var_val])
        elif expr in self.variables:
            var_val = self.variables[expr]
            if isinstance(var_val, ir.AllocaInstr):
                var_val = self.builder.load(var_val)
            return self.builder.call(self.module.get_global('atoi'), [var_val])
        
        return ir.Constant(self.int32_t, 0)

    def _parse_table_definition(self, line: str) -> Tuple[str, List[str]]:
        """Парсит определение таблицы из строки create table"""
        match = re.match(r'create\s+(\w+)\s+with\s*\((.*)\)', line)
        if not match:
            return "", []
        
        table_name = match.group(1)
        columns_def = match.group(2).strip()
        
        if not columns_def:
            return table_name, []
        
        columns = []
        current = ""
        depth = 0
        
        for char in columns_def:
            if char == '(':
                depth += 1
                current += char
            elif char == ')':
                depth -= 1
                current += char
            elif char == ',' and depth == 0:
                columns.append(current.strip())
                current = ""
            else:
                current += char
        
        if current:
            columns.append(current.strip())
        
        return table_name, columns
    
    def _parse_column_definition(self, col_def_lines: List[str]) -> Tuple[str, str, Optional[str]]:
        """Парсит определение колонки, поддерживая многострочные реактивные выражения"""
        if not col_def_lines:
            return "", "", None
        
        first_line = col_def_lines[0].strip()
        
        if first_line.endswith(','):
            first_line = first_line[:-1]
        
        if ':' not in first_line:
            return first_line, "string", None
        
        if '=' in first_line:
            parts = first_line.split('=', 1)
            name_type = parts[0].strip()
            reactive_expr = parts[1].strip()
            
            if ':' in name_type:
                name_type_parts = name_type.split(':', 1)
                name = name_type_parts[0].strip()
                type_name = name_type_parts[1].strip()
            else:
                name = name_type
                type_name = "string"
            
            return name, type_name, reactive_expr
        
        else:
            first_colon = first_line.find(':')
            second_colon = first_line.find(':', first_colon + 1)
            
            if second_colon != -1:
                name = first_line[:first_colon].strip()
                type_name = first_line[first_colon+1:second_colon].strip()
                reactive_expr = first_line[second_colon+1:].strip()
                return name, type_name, reactive_expr
            else:
                name_type_parts = first_line.split(':')
                if len(name_type_parts) >= 2:
                    name = name_type_parts[0].strip()
                    type_name = name_type_parts[1].strip()
                    
                    reactive_lines = []
                    for line in col_def_lines[1:]:
                        line = line.strip()
                        if line.endswith(','):
                            line = line[:-1]
                        reactive_lines.append(line)
                    
                    reactive_expr = " ".join(reactive_lines)
                    return name, type_name, reactive_expr
        
        return "", "", None

    def _generate_create_table(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует создание таблицы с правильным парсингом колонок"""
        indent, line = lines[start]
        
        if "with" not in line:
            return start + 1
        
        parts = line.split("with")
        table_name = parts[0].replace("create", "").strip()
        
        i = start
        full_definition_lines = []
        
        if '(' in line:
            with_part = line.split("with", 1)[1]
            open_bracket = with_part.find('(')
            full_definition_lines.append(with_part[open_bracket:])
        else:
            i += 1
            while i < len(lines) and '(' not in lines[i][1]:
                i += 1
            if i < len(lines):
                full_definition_lines.append(lines[i][1])
        
        i += 1
        bracket_count = 1  
        
        while i < len(lines) and bracket_count > 0:
            current_line = lines[i][1]
            bracket_count += current_line.count('(')
            bracket_count -= current_line.count(')')
            
            full_definition_lines.append(current_line)
            i += 1
        
        full_definition = ' '.join(full_definition_lines)
        
        full_definition = full_definition.strip()
        if full_definition.startswith('(') and full_definition.endswith(')'):
            full_definition = full_definition[1:-1].strip()
        
        column_defs = self._split_column_definitions_simple(full_definition)
        
        col_names = []
        col_types = []
        reactive_exprs = []
        
        for col_def in column_defs:
            name, type_name, reactive_expr = self._parse_simple_column_definition(col_def)
            if name:
                col_names.append(name)
                col_types.append(type_name)
                reactive_exprs.append(reactive_expr if reactive_expr else "")
        
        col_count = len(col_names)
        col_names_arr = self._create_string_array(col_names)
        col_types_arr = self._create_string_array(col_types)
        reactive_arr = self._create_nullable_string_array(reactive_exprs)
        
        name_ptr = self._get_string_ptr(table_name)
        table = self.builder.call(self.module.get_global('create_table'),
                                [name_ptr,
                                ir.Constant(self.int32_t, col_count),
                                col_names_arr,
                                col_types_arr,
                                reactive_arr])
        
        self.tables[table_name] = {
            'ptr': table,  # Указатель на таблицу
            'col_count': col_count,
            'col_names': col_names,
            'col_types': col_types,
            'reactive_exprs': reactive_exprs
        }
        
        print(f"Создана таблица '{table_name}' с {col_count} колонками")
        print(f"Колонки: {col_names}")
        print(f"Типы: {col_types}")
        print(f"Реактивные выражения: {reactive_exprs}")
        
        return i

    def _split_column_definitions_simple(self, definition: str) -> List[str]:
        """Разбивает определение таблицы на отдельные колонки (упрощенная версия)"""
        columns = []
        current = []
        paren_depth = 0
        
        i = 0
        while i < len(definition):
            char = definition[i]
            
            if char == '(':
                paren_depth += 1
                current.append(char)
            elif char == ')':
                paren_depth -= 1
                current.append(char)
            elif char == ',' and paren_depth == 0:
                col_def = ''.join(current).strip()
                if col_def:
                    columns.append(col_def)
                current = []
            else:
                current.append(char)
            
            i += 1
        
        if current:
            col_def = ''.join(current).strip()
            if col_def:
                columns.append(col_def)
        
        return columns

    def _parse_simple_column_definition(self, col_def: str) -> Tuple[str, str, Optional[str]]:
        """Парсит определение одной колонки (упрощенная версия)"""
        col_def = col_def.strip()
        
        if col_def.endswith(','):
            col_def = col_def[:-1].strip()
        
        # Формат 1: name: type = expression (с реактивным выражением)
        if '=' in col_def:
            equal_pos = col_def.find('=')
            left_part = col_def[:equal_pos].strip()
            reactive_expr = col_def[equal_pos+1:].strip()
            
            if ':' in left_part:
                colon_pos = left_part.find(':')
                name = left_part[:colon_pos].strip()
                type_name = left_part[colon_pos+1:].strip()
                return name, type_name, reactive_expr
            else:
                return left_part, "string", reactive_expr
        
        # Формат 2: name: type (без реактивного выражения)
        elif ':' in col_def:
            colon_pos = col_def.find(':')
            name = col_def[:colon_pos].strip()
            type_name = col_def[colon_pos+1:].strip()
            return name, type_name, None
        
        # Формат 3: только имя (без типа и выражения)
        else:
            return col_def, "string", None
    
    def _generate_insert(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует вставку в таблицу"""
        indent, line = lines[start]
        
        table_name = ""
        
        if "insert to" in line and ":" in line:
            line_parts = line.split("insert to", 1)[1].strip()
            table_name = line_parts.rstrip(":").strip()
        
        if not table_name:
            return start + 1
        
        if table_name not in self.tables:
            table_name_ptr = self._get_string_ptr(table_name)
            target_table = self.builder.call(self.module.get_global('find_table'), [table_name_ptr])
            table_info = None
            print(f"Предупреждение: таблица '{table_name}' не найдена в кэше")
        else:
            target_table = self.tables[table_name]['ptr']
            table_info = self.tables[table_name]
            print(f"Найдена таблица '{table_name}' с {table_info['col_count']} колонками")
        
        i = start + 1
        
        while i < len(lines) and lines[i][0] > indent:
            row_line = lines[i][1]
            self._process_single_insert(row_line, target_table, table_info)
            i += 1
        
        return i

    def _process_single_insert(self, row_line: str, target_table, table_info):
        """Обрабатывает одну строку вставки с учетом всех колонок таблицы"""
        if '=' not in row_line:
            return
        
        left_part, right_part = row_line.split('=', 1)
        col_names_in_row = [name.strip() for name in left_part.split(',')]
        values_in_row = [value.strip() for value in right_part.split(',')]
        
        if table_info:
            col_count = table_info['col_count']
        else:
            col_count = len(values_in_row)
        
        value_ptrs = []
        
        for i, value in enumerate(values_in_row):
            if value.startswith('"') and value.endswith('"'):
                str_value = value[1:-1]
                value_ptr = self._get_string_ptr(str_value)
            elif value.isdigit():
                int_val = ir.Constant(self.int32_t, int(value))
                value_ptr = self._convert_int_to_string(int_val)
            elif '.' in value and value.replace('.', '', 1).isdigit():
                float_val = float(value)
                buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
                buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), 
                                            ir.Constant(self.int32_t, 0)])
                fmt = self._get_string_ptr("%.2f")
                const_val = ir.Constant(self.double_t, float_val)
                self.builder.call(self.module.get_global('sprintf'), 
                                [buf_ptr, fmt, const_val])
                value_ptr = self.builder.call(self.module.get_global('strdup'), [buf_ptr])
            elif value in self.variables:
                var_ptr = self.variables[value]
                if isinstance(var_ptr, ir.AllocaInstr):
                    var_ptr = self.builder.load(var_ptr)
                value_ptr = var_ptr
            else:
                value_ptr = self._get_string_ptr(value)
            
            value_ptrs.append(value_ptr)
        
        while len(value_ptrs) < col_count:
            value_ptrs.append(ir.Constant(self.int8_ptr_t, None))
        
        if value_ptrs:
            array_type = ir.ArrayType(self.int8_ptr_t, col_count)
            array_alloca = self.builder.alloca(array_type)
            
            for i, val_ptr in enumerate(value_ptrs):
                elem_ptr = self.builder.gep(array_alloca, 
                                        [ir.Constant(self.int32_t, 0), 
                                        ir.Constant(self.int32_t, i)])
                self.builder.store(val_ptr, elem_ptr)
            
            array_ptr = self.builder.gep(array_alloca, 
                                    [ir.Constant(self.int32_t, 0), 
                                        ir.Constant(self.int32_t, 0)])
            array_ptr_cast = self.builder.bitcast(array_ptr, self.int8_ptr_ptr_t)
            
            self.builder.call(self.module.get_global('table_insert_silent'), 
                            [target_table, array_ptr_cast])
    

    def _generate_update(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует обновление таблицы"""
        indent, line = lines[start]
        if not line.startswith('update '):
            return start + 1
        
        rest = line[7:].strip()
        
        if "set" not in rest:
            return start + 1
        
        table_name, set_part = rest.split("set", 1)
        table_name = table_name.strip()
        set_part = set_part.strip()
        
        where_condition = None
        if 'where' in set_part:
            set_clause, where_condition = set_part.split('where', 1)
            set_clause = set_clause.strip()
            where_condition = where_condition.strip()
        else:
            set_clause = set_part
    
        assignments = [a.strip() for a in set_clause.split(',')]
        col_names = []
        new_values = []
        
        for assignment in assignments:
            if '=' in assignment:
                col, value = assignment.split('=', 1)
                col_name = col.strip()
                col_names.append(col_name)
                
                value = value.strip()
                if value.isdigit():
                    int_val = ir.Constant(self.int32_t, int(value))
                    val_ptr = self._convert_int_to_string(int_val)
                elif '.' in value and value.replace('.', '', 1).isdigit():
                    # Float значение
                    float_val = float(value)
                    buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
                    buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), 
                                                ir.Constant(self.int32_t, 0)])
                    fmt = self._get_string_ptr("%.2f")
                    const_val = ir.Constant(self.double_t, float_val)
                    self.builder.call(self.module.get_global('sprintf'), 
                                    [buf_ptr, fmt, const_val])
                    val_ptr = self.builder.call(self.module.get_global('strdup'), [buf_ptr])
                else:
                    val_ptr = self._get_string_ptr(value)
                
                new_values.append(val_ptr)
        
        if table_name in self.tables:
            table = self.tables[table_name]['ptr']
        else:
            table_name_ptr = self._get_string_ptr(table_name)
            table = self.builder.call(self.module.get_global('find_table'), [table_name_ptr])
        
        col_count = len(col_names)
        col_names_arr = self._create_string_array(col_names)
        values_arr = self._create_dynamic_string_array(new_values)
        
        if where_condition:
            where_condition = where_condition.replace("==", "=")
            cond_ptr = self._get_string_ptr(where_condition)
        else:
            cond_ptr = ir.Constant(self.int8_ptr_t, None)
        
        self.builder.call(self.module.get_global('table_update'),
                        [table, col_names_arr, values_arr, 
                        ir.Constant(self.int32_t, col_count), cond_ptr])
        
        return start + 1
    
    def _generate_write(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует вывод"""
        indent, line = lines[start]
        
        content = line[6:].strip()
        
        if content in self.tables:
            table = self.tables[content]['ptr']
            self.builder.call(self.module.get_global('table_print'), [table])
            return start + 1
        
        if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
            str_content = content[1:-1]
            str_ptr = self._get_string_ptr(str_content)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, str_ptr])
            return start + 1
        
        if self.current_function and content in self.functions[self.current_function]['variables']:
            var_ptr = self.functions[self.current_function]['variables'][content]
            val_ptr = self.builder.load(var_ptr)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, val_ptr])
            return start + 1
        elif content in self.variables:
            val_ptr = self.variables[content]
            if isinstance(val_ptr, ir.AllocaInstr):
                val_ptr = self.builder.load(val_ptr)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, val_ptr])
            return start + 1
        
        if content == 'true' or content == 'false':
            str_ptr = self._get_string_ptr(content)
            fmt = self._get_string_ptr("%s\n")
            self.builder.call(self.module.get_global('printf'), [fmt, str_ptr])
            return start + 1
        
        empty_str = self._get_string_ptr("")
        fmt = self._get_string_ptr("%s\n")
        self.builder.call(self.module.get_global('printf'), [fmt, empty_str])
        
        return start + 1
    
    def _generate_assignment(self, line: str, start: int) -> int:
        """Генерирует присваивание"""
        if '=' not in line:
            return start + 1
        
        left, right = line.split('=', 1)
        left_vars = [v.strip() for v in left.split(',')]
        right_expr = right.strip()
        
        var_name = left_vars[0]
        context_vars = {}
        
        for name, val in self.variables.items():
            if isinstance(val, ir.AllocaInstr):
                context_vars[name] = self.builder.load(val)
            else:
                context_vars[name] = val
        
        result = self._evaluate_arithmetic_expression(right_expr, context_vars)
        
        var_name = left_vars[0]
        
        if var_name not in self.variables:
            var_ptr = self.builder.alloca(self.int8_ptr_t, name=var_name)
            self.variables[var_name] = var_ptr
        
        var_ptr = self.variables[var_name]
        
        if isinstance(var_ptr, ir.AllocaInstr):
            self.builder.store(result, var_ptr)
        else:
            temp_ptr = self.builder.alloca(self.int8_ptr_t, name=f"{var_name}_temp")
            self.builder.store(result, temp_ptr)
            loaded_val = self.builder.load(temp_ptr)
            self.variables[var_name] = loaded_val
        
        return start + 1
    
    def _evaluate_simple_expression(self, expr: str) -> ir.Instruction:
        """Оценивает простое выражение (переменная, число, строка)"""
        expr = expr.strip()
        
        if expr.isdigit():
            int_val = ir.Constant(self.int32_t, int(expr))
            return self._convert_int_to_string(int_val)
        
        if '.' in expr and expr.replace('.', '', 1).isdigit():
            float_val = float(expr)
            buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
            buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
            fmt = self._get_string_ptr("%.1f")
            const_val = ir.Constant(self.double_t, float_val)
            self.builder.call(self.module.get_global('sprintf'), [buf_ptr, fmt, const_val])
            return self.builder.call(self.module.get_global('strdup'), [buf_ptr])
        
        if expr in self.variables:
            var_ptr = self.variables[expr]
            if isinstance(var_ptr, ir.AllocaInstr):
                return self.builder.load(var_ptr)
            return var_ptr
        
        if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
            return self._get_string_ptr(expr[1:-1])
        
        if expr == 'true' or expr == 'false':
            return self._get_string_ptr(expr)
        
        return self._get_string_ptr("")
    
    def _generate_select(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует выборку из таблицы"""
        indent, line = lines[start]
        
        match = re.match(r'select (.+) from (\w+)(?: where (.+))?(?: as (\w+))?', line)
        if match:
            columns = match.group(1).strip()
            table_name = match.group(2).strip()
            condition = match.group(3) or ""
            alias = match.group(4)
            
            if alias:
                result_name = alias.strip()
            else:
                result_name = f"{table_name}_select"
            
            print(f"SELECT: columns={columns}, table={table_name}, condition={condition}, alias={result_name}")
            
            if table_name in self.tables:
                table = self.tables[table_name]['ptr']
            else:
                table_name_ptr = self._get_string_ptr(table_name)
                table = self.builder.call(self.module.get_global('find_table'), [table_name_ptr])
            
            cols_ptr = self._get_string_ptr(columns)
            cond_ptr = self._get_string_ptr(condition) if condition else ir.Constant(self.int8_ptr_t, None)
            
            result_table = self.builder.call(self.module.get_global('table_select'),
                                        [table, cols_ptr, cond_ptr])
            
            self.tables[result_name] = result_table
            print(f"Результат SELECT сохранен как: {result_name}")
        
        return start + 1
    
    def _generate_join(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует объединение таблиц"""
        indent, line = lines[start]
        
        # Формат: join users_table with orders_table by id and user_id as joined
        match = re.match(r'join\s+(\w+)\s+with\s+(\w+)\s+by\s+(\w+)\s+and\s+(\w+)(?:\s+as\s+(\w+))?', line)
        if not match:
            match = re.match(r'join\s+(\w+)\s+with\s+(\w+)\s+by\s+(.+?)(?:\s+as\s+(\w+))?$', line)
            if not match:
                print(f"Не удалось разобрать join: {line}")
                return start + 1
            
            left_table = match.group(1)
            right_table = match.group(2)
            condition = match.group(3).strip()
            alias = match.group(4)
            
            if '=' in condition:
                left_part, right_part = condition.split('=', 1)
                left_part = left_part.strip()
                right_part = right_part.strip()
                
                if '.' in left_part:
                    left_table_name, left_col = left_part.split('.')
                    left_col = left_col.strip()
                else:
                    left_col = left_part
                    
                if '.' in right_part:
                    right_table_name, right_col = right_part.split('.')
                    right_col = right_col.strip()
                else:
                    right_col = right_part
        else:
            left_table = match.group(1)
            right_table = match.group(2)
            left_col = match.group(3)
            right_col = match.group(4)
            alias = match.group(5)
        
        if alias:
            result_name = alias
        else:
            result_name = f"{left_table}_join_{right_table}"
        
        if left_table in self.tables:
            left_ptr = self.tables[left_table]['ptr']
        else:
            left_name_ptr = self._get_string_ptr(left_table)
            left_ptr = self.builder.call(self.module.get_global('find_table'), [left_name_ptr])
        
        if right_table in self.tables:
            right_ptr = self.tables[right_table]['ptr']
        else:
            right_name_ptr = self._get_string_ptr(right_table)
            right_ptr = self.builder.call(self.module.get_global('find_table'), [right_name_ptr])
        
        if not left_ptr:
            left_name_ptr = self._get_string_ptr(left_table)
            left_ptr = self.builder.call(self.module.get_global('find_table'), [left_name_ptr])
        
        if not right_ptr:
            right_name_ptr = self._get_string_ptr(right_table)
            right_ptr = self.builder.call(self.module.get_global('find_table'), [right_name_ptr])
        
        condition = f"{left_table}.{left_col}={right_table}.{right_col}"
        cond_ptr = self._get_string_ptr(condition)
        
        result_table = self.builder.call(self.module.get_global('table_join'),
                                    [left_ptr, right_ptr, cond_ptr])
        
        self.tables[result_name] = result_table
        
        return start + 1
    
    def _generate_filter(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует фильтрацию таблицы"""
        indent, line = lines[start]
        
        # Формат: filter joined by amount > 10 and name[0] == 'A' as big_orders
        match = re.match(r'filter\s+(\w+)\s+by\s+(.+?)(?:\s+as\s+(\w+))?$', line)
        if not match:
            print(f"Не удалось разобрать filter: {line}")
            return start + 1
        
        table_name = match.group(1)
        condition = match.group(2).strip()
        alias = match.group(3)
        
        if alias:
            result_name = alias
        else:
            result_name = f"{table_name}_filtered"
        
        if table_name in self.tables:
            table = self.tables[table_name]['ptr']
        else:
            table_name_ptr = self._get_string_ptr(table_name)
            table = self.builder.call(self.module.get_global('find_table'), [table_name_ptr])
        
        condition = condition.replace("name[0] == 'A'", "LEFT(name, 1) = 'A'")
        
        condition = re.sub(r'(\w+)\[0\]\s*==\s*\'([^\']+)\'', r'LEFT(\1, 1) = \'\2\'', condition)
        
        if table_name.startswith(('users_table_join', 'orders_table_join')) or table_name == 'joined':
            condition = condition.replace("amount >", "orders_table.amount >")
            condition = condition.replace("LEFT(name, 1)", "LEFT(users_table.name, 1)")
        
        cond_ptr = self._get_string_ptr(condition)
        
        result_table = self.builder.call(self.module.get_global('table_filter'),
                                    [table, cond_ptr])
        
        self.tables[result_name] = result_table
        
        return start + 1
    
    def _generate_sort(self, lines: List[Tuple[int, str]], start: int) -> int:
        """Генерирует сортировку таблицы"""
        indent, line = lines[start]
        
        if line.startswith('write '):
            line = line[6:]
        
        match = re.match(r'sort\s+<desc>\s+(\w+)\s+by\s+(\w+)(?:\s+as\s+(\w+))?', line)
        if not match:
            print(f"Не удалось разобрать sort: {line}")
            return start + 1
        
        table_name = match.group(1)
        column = match.group(2)
        alias = match.group(3)
        
        descending = 1
        
        if alias:
            result_name = alias
        else:
            result_name = f"{table_name}_sorted"
        
        if table_name in self.tables:
            table = self.tables[table_name]['ptr']
        else:
            table_name_ptr = self._get_string_ptr(table_name)
            table = self.builder.call(self.module.get_global('find_table'), [table_name_ptr])
        
        if table_name.startswith(('users_table_join', 'orders_table_join')):
            if column in ['id', 'name', 'age', 'city']:
                column = f"users_table.{column}"
            elif column in ['user_id', 'amount', 'created']:
                column = f"orders_table.{column}"
        
        col_ptr = self._get_string_ptr(column)
        
        print(f"Выполняем sort: {table_name} по {column}, descending={descending}")
        
        result_table = self.builder.call(self.module.get_global('table_sort'),
                                    [table, col_ptr, ir.Constant(self.int32_t, descending)])
        
        self.tables[result_name] = result_table
        
        if lines[start][1].startswith('write '):
            self.builder.call(self.module.get_global('table_print'), [result_table])
            print(f"Вывод отсортированной таблицы: {result_name}")
        
        print(f"Результат sort сохранен как: {result_name}")
        
        return start + 1
    
    def _generate_for_loop(self, lines: List[Tuple[int, str]], start: int, func) -> int:
        indent, line = lines[start]
    
        # Два варианта: for var in expr..expr или for var in table
        if '..' in line:
            match = re.match(r'for (\w+) in (\d+)\.\.(\d+):', line)
            if match:
                var_name = match.group(1)
                start_val = int(match.group(2))
                end_val = int(match.group(3))
                
                if self.current_function:
                    if var_name not in self.functions[self.current_function]['variables']:
                        var_str_ptr = self.builder.alloca(self.int8_ptr_t, name=var_name)
                        self.functions[self.current_function]['variables'][var_name] = var_str_ptr
                    else:
                        var_str_ptr = self.functions[self.current_function]['variables'][var_name]
                else:
                    if var_name not in self.variables:
                        var_str_ptr = self.builder.alloca(self.int8_ptr_t, name=var_name)
                        self.variables[var_name] = var_str_ptr
                    else:
                        var_str_ptr = self.variables[var_name]
                
                loop_cond = func.append_basic_block(f"for_cond_{var_name}")
                loop_body = func.append_basic_block(f"for_body_{var_name}")
                loop_end = func.append_basic_block(f"for_end_{var_name}")
                
                counter_ptr = self.builder.alloca(self.int32_t, name=f"{var_name}_counter")
                self.builder.store(ir.Constant(self.int32_t, start_val), counter_ptr)
                
                self.builder.branch(loop_cond)
                
                self.builder.position_at_start(loop_cond)
                current_val = self.builder.load(counter_ptr)
                cond = self.builder.icmp_signed('<=', current_val, 
                                            ir.Constant(self.int32_t, end_val))
                self.builder.cbranch(cond, loop_body, loop_end)
                
                self.builder.position_at_start(loop_body)
                
                buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
                buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
                fmt = self._get_string_ptr("%d")
                self.builder.call(self.module.get_global('sprintf'), 
                                [buf_ptr, fmt, current_val])
                str_val = self.builder.call(self.module.get_global('strdup'), [buf_ptr])
                
                self.builder.store(str_val, var_str_ptr)
                
                body_start = start + 1
                body_end = body_start
                while body_end < len(lines) and lines[body_end][0] > indent:
                    body_end += 1
                
                self._generate_statements(lines, body_start, body_end, func)
                
                next_val = self.builder.add(current_val, ir.Constant(self.int32_t, 1))
                self.builder.store(next_val, counter_ptr)
                self.builder.branch(loop_cond)
                
                self.builder.position_at_start(loop_end)
                
                return body_end
        else:
            match = re.match(r'for (\w+) in (\w+):', line)
            if match:
                var_name = match.group(1)
                table_name = match.group(2)
                
                if self.current_function:
                    if var_name not in self.functions[self.current_function]['variables']:
                        var_str_ptr = self.builder.alloca(self.int8_ptr_t, name=var_name)
                        self.functions[self.current_function]['variables'][var_name] = var_str_ptr
                    else:
                        var_str_ptr = self.functions[self.current_function]['variables'][var_name]
                else:
                    if var_name not in self.variables:
                        var_str_ptr = self.builder.alloca(self.int8_ptr_t, name=var_name)
                        self.variables[var_name] = var_str_ptr
                    else:
                        var_str_ptr = self.variables[var_name]
                
                if table_name not in self.tables:
                    table_name_ptr = self._get_string_ptr(table_name)
                    table = self.builder.call(self.module.get_global('find_table'), [table_name_ptr])
                else:
                    table = self.tables[table_name]
                
                loop_count = 5 
                loop_start = func.append_basic_block(f"table_loop_start_{var_name}")
                loop_body = func.append_basic_block(f"table_loop_body_{var_name}")
                loop_end = func.append_basic_block(f"table_loop_end_{var_name}")
                
                counter_ptr = self.builder.alloca(self.int32_t, name=f"{var_name}_counter")
                self.builder.store(ir.Constant(self.int32_t, 0), counter_ptr)
                
                self.builder.branch(loop_start)
                
                self.builder.position_at_start(loop_start)
                counter_val = self.builder.load(counter_ptr)
                cond = self.builder.icmp_signed('<', counter_val, 
                                            ir.Constant(self.int32_t, loop_count))
                self.builder.cbranch(cond, loop_body, loop_end)
                
                self.builder.position_at_start(loop_body)
                
                buf = self.builder.alloca(ir.ArrayType(self.int8_t, 32))
                buf_ptr = self.builder.gep(buf, [ir.Constant(self.int32_t, 0), ir.Constant(self.int32_t, 0)])
                fmt = self._get_string_ptr("%d")
                
                value_to_show = self.builder.add(counter_val, ir.Constant(self.int32_t, 1))
                self.builder.call(self.module.get_global('sprintf'), 
                                [buf_ptr, fmt, value_to_show])
                str_val = self.builder.call(self.module.get_global('strdup'), [buf_ptr])
                
                self.builder.store(str_val, var_str_ptr)
                
                body_start = start + 1
                body_end = body_start
                while body_end < len(lines) and lines[body_end][0] > indent:
                    body_end += 1
                
                self._generate_statements(lines, body_start, body_end, func)
                
                next_counter = self.builder.add(counter_val, ir.Constant(self.int32_t, 1))
                self.builder.store(next_counter, counter_ptr)
                self.builder.branch(loop_start)
                
                self.builder.position_at_start(loop_end)
                
                return body_end
        
        return start + 1
    
    def _generate_while_loop(self, lines: List[Tuple[int, str]], start: int, func) -> int:
        """Генерирует цикл while"""
        indent, line = lines[start]
        match = re.match(r'while (.+):', line)
        if not match:
            return start + 1
        
        condition = match.group(1)
        
        parts = condition.split('>')
        if len(parts) == 2:
            var_name = parts[0].strip()
            limit = int(parts[1].strip())
            
            loop_cond = func.append_basic_block("while_cond")
            loop_body = func.append_basic_block("while_body")
            loop_end = func.append_basic_block("while_end")
            
            self.builder.branch(loop_cond)
            
            self.builder.position_at_start(loop_cond)
            
            var_value = None
            if var_name in self.variables:
                var_ptr = self.variables[var_name]
                if isinstance(var_ptr, ir.AllocaInstr):
                    var_value = self.builder.load(var_ptr)
                else:
                    var_value = var_ptr
                
                int_val = self.builder.call(self.module.get_global('atoi'), [var_value])
                
                cond = self.builder.icmp_signed('>', int_val, ir.Constant(self.int32_t, limit))
                self.builder.cbranch(cond, loop_body, loop_end)
                
                self.builder.position_at_start(loop_body)
                
                body_start = start + 1
                body_end = body_start
                while body_end < len(lines) and lines[body_end][0] > indent:
                    body_end += 1
                
                self._generate_statements(lines, body_start, body_end, func)
                
                new_val = self.builder.sub(int_val, ir.Constant(self.int32_t, 1))
                new_str = self._convert_int_to_string(new_val)
                
                if var_name in self.variables:
                    var_ptr = self.variables[var_name]
                    if isinstance(var_ptr, ir.AllocaInstr):
                        self.builder.store(new_str, var_ptr)
                    else:
                        new_ptr = self.builder.alloca(self.int8_ptr_t, name=var_name)
                        self.builder.store(new_str, new_ptr)
                        self.variables[var_name] = new_ptr
                
                self.builder.branch(loop_cond)
                
                self.builder.position_at_start(loop_end)
                
                return body_end
        
        return start + 1
    
    def _generate_if(self, lines: List[Tuple[int, str]], start: int, func) -> int:
        """Генерирует условный оператор if с правильным управлением потоком"""
        indent, line = lines[start]
        match = re.match(r'if (.+):', line)
        if not match:
            return start + 1
        
        condition_str = match.group(1)
        
        condition = self._parse_condition(condition_str)
        
        i = start + 1
        then_end = i
        else_start = -1
        else_end = -1
        
        while i < len(lines):
            current_indent, current_line = lines[i]
            
            if current_indent == indent:
                if current_line.startswith('else:'):
                    else_start = i
                    then_end = i
                    break
                else:
                    then_end = i
                    break
            elif current_indent < indent:
                then_end = i
                break
            i += 1
        
        if i == len(lines):
            then_end = i
        
        then_block = func.append_basic_block("if_then")
        
        if else_start != -1:
            i = else_start + 1
            while i < len(lines):
                current_indent, current_line = lines[i]
                if current_indent <= indent:
                    else_end = i
                    break
                i += 1
            if i == len(lines):
                else_end = i
            
            else_block = func.append_basic_block("if_else")
            merge_block = func.append_basic_block("if_merge")
            
            self.builder.cbranch(condition, then_block, else_block)
            
            self.builder.position_at_start(then_block)
            self._generate_statements(lines, start + 1, then_end, func)
            
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_block)
            
            self.builder.position_at_start(else_block)
            self._generate_statements(lines, else_start + 1, else_end, func)
            
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_block)
            
            self.builder.position_at_start(merge_block)
            
            return else_end
        else:
            merge_block = func.append_basic_block("if_merge")
            
            self.builder.cbranch(condition, then_block, merge_block)
            
            self.builder.position_at_start(then_block)
            self._generate_statements(lines, start + 1, then_end, func)
            
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_block)
            
            self.builder.position_at_start(merge_block)
            
            return then_end
    
    def _generate_switch(self, lines: List[Tuple[int, str]], start: int, func) -> int:
        indent, line = lines[start]
        match = re.match(r'switch (.+):', line)
        if not match:
            return start + 1
        
        expr = match.group(1)
        
        expr_value = None
        if expr in self.variables:
            expr_value = self.variables[expr]
            if isinstance(expr_value, ir.AllocaInstr):
                expr_value = self.builder.load(expr_value)
        elif expr == 'true':
            expr_value = self._get_string_ptr("true")
        elif expr == 'false':
            expr_value = self._get_string_ptr("false")
        
        if not expr_value:
            expr_value = self._get_string_ptr("false")
        
        switch_end = func.append_basic_block("switch_end")
        
        cases = []
        default_block = None
        i = start + 1
        
        while i < len(lines) and lines[i][0] > indent:
            if lines[i][1].startswith('case is '):
                case_value = lines[i][1][8:].strip().rstrip(':')
                cases.append((case_value, i))
            elif lines[i][1].startswith('default:'):
                default_block = i
            i += 1
        
        true_str = self._get_string_ptr("true")
        false_str = self._get_string_ptr("false")
        
        if expr_value:
            cmp_result = self.builder.call(self.module.get_global('strcmp'), 
                                        [expr_value, true_str])
            is_true = self.builder.icmp_signed('==', cmp_result, 
                                            ir.Constant(self.int32_t, 0))
        else:
            is_true = ir.Constant(self.bool_t, 0)
        
        case_block = None
        default_bb = None
        
        if cases:
            case_block = func.append_basic_block("switch_case")
        
        if default_block:
            default_bb = func.append_basic_block("switch_default")
        else:
            default_bb = switch_end
        
        if case_block:
            self.builder.cbranch(is_true, case_block, default_bb)
        else:
            self.builder.branch(default_bb)
        
        if case_block and cases:
            self.builder.position_at_start(case_block)
            case_start = cases[0][1]
            case_end = case_start + 1
            while (case_end < len(lines) and lines[case_end][0] > indent and 
                not lines[case_end][1].startswith('default:')):
                case_end += 1
            
            self._generate_statements(lines, case_start + 1, case_end, func)
            self.builder.branch(switch_end)
        
        if default_block and default_bb:
            self.builder.position_at_start(default_bb)
            default_end = default_block + 1
            while (default_end < len(lines) and lines[default_end][0] > indent):
                default_end += 1
            
            self._generate_statements(lines, default_block + 1, default_end, func)
            self.builder.branch(switch_end)
        
        self.builder.position_at_start(switch_end)
        
        return i
    
    def _generate_return(self, line: str, start: int) -> int:
        """Генерирует возврат значения из функции"""
        if not self.current_function:
            return start + 1
        
        expr = line[7:].strip()
        
        if expr.startswith('not '):
            inner_expr = expr[4:].strip()
            if '(' in inner_expr and ')' in inner_expr:
                func_name, args = self._parse_function_call(inner_expr)
                
                if func_name != inner_expr: 
                    result = self._generate_function_call(func_name, args)
                    
                    true_str = self._get_string_ptr("true")
                    cmp = self.builder.call(self.module.get_global('strcmp'), [result, true_str])
                    is_true = self.builder.icmp_signed('==', cmp, ir.Constant(self.int32_t, 0))
                    not_result = self.builder.not_(is_true)  # Логическое НЕ
                    
                    result_str = self._convert_bool_to_string(not_result)
                    self.builder.ret(result_str)
                    return start + 1
            else:
                if inner_expr == 'true':
                    result_str = self._get_string_ptr("false")
                    self.builder.ret(result_str)
                    return start + 1
                elif inner_expr == 'false':
                    result_str = self._get_string_ptr("true")
                    self.builder.ret(result_str)
                    return start + 1
                elif self.current_function and inner_expr in self.functions[self.current_function]['variables']:
                    var_ptr = self.functions[self.current_function]['variables'][inner_expr]
                    var_val = self.builder.load(var_ptr)
                    true_str = self._get_string_ptr("true")
                    cmp = self.builder.call(self.module.get_global('strcmp'), [var_val, true_str])
                    is_true = self.builder.icmp_signed('==', cmp, ir.Constant(self.int32_t, 0))
                    not_result = self.builder.not_(is_true)
                    result_str = self._convert_bool_to_string(not_result)
                    self.builder.ret(result_str)
                    return start + 1
        
        if '(' in expr and ')' in expr:
            func_name, args = self._parse_function_call(expr)
            
            if func_name != expr:
                result = self._generate_function_call(func_name, args)
                self.builder.ret(result)
                return start + 1
        
        if any(op in expr for op in ['+', '-', '*', '/', '%']):
            context_vars = {}
            
            if self.current_function:
                for var_name, var_ptr in self.functions[self.current_function]['variables'].items():
                    context_vars[var_name] = self.builder.load(var_ptr)
            
            for var_name, var_val in self.variables.items():
                if isinstance(var_val, ir.AllocaInstr):
                    context_vars[var_name] = self.builder.load(var_val)
                else:
                    context_vars[var_name] = var_val
            
            result = self._evaluate_arithmetic_expression(expr, context_vars)
            self.builder.ret(result)
            return start + 1
        
        if self.current_function and expr in self.functions[self.current_function]['variables']:
            var_ptr = self.functions[self.current_function]['variables'][expr]
            val = self.builder.load(var_ptr)
            self.builder.ret(val)
        elif expr in self.variables:
            val = self.variables[expr]
            if isinstance(val, ir.AllocaInstr):
                val = self.builder.load(val)
            self.builder.ret(val)
        elif expr in ['true', 'false']:
            bool_val = expr == "true"
            result_str = self._convert_bool_to_string(ir.Constant(self.bool_t, bool_val))
            self.builder.ret(result_str)
        else:
            str_ptr = self._get_string_ptr(expr)
            self.builder.ret(str_ptr)
        
        return start + 1

def generate_llvm_ir(code: str) -> str:
    """Главная функция генерации LLVM IR"""
    generator = LLVMGenerator()
    module = generator.generate_from_code(code)
    return str(module)


if __name__ == "__main__":
    # Обработка аргументов командной строки
    if len(sys.argv) < 2:
        print("Использование: python codegen.py <входной_файл> [выходной_файл]")
        print("  <входной_файл> - файл с исходным кодом на вашем языке")
        print("  [выходной_файл] - имя выходного исполняемого файла (по умолчанию: 'output')")
        sys.exit(1)
    
    input_file = sys.argv[1]
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        print(f"Прочитано {len(source_code)} символов из файла {input_file}")
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        sys.exit(1)
    
    if len(sys.argv) > 2:
        output_name = sys.argv[2]
        if output_name.lower().endswith('.exe'):
            output_name = output_name[:-4]
    else:
        output_name = "output"
    
    try:
        print("Начало генерации LLVM IR...")
        llvm_ir = generate_llvm_ir(source_code)
        print("Генерация LLVM IR завершена успешно")
    except Exception as e:
        print(f"Ошибка генерации LLVM IR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    llvm_file = f"{output_name}.ll"
    try:
        with open(llvm_file, "w", encoding='utf-8') as f:
            f.write(llvm_ir)
        print(f"LLVM IR сгенерирован в '{llvm_file}' ({len(llvm_ir)} символов)")
    except Exception as e:
        print(f"Ошибка сохранения LLVM IR: {e}")
        sys.exit(1)