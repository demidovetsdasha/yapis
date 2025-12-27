# Generated from ./DashSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DashSQLParser import DashSQLParser
else:
    from DashSQLParser import DashSQLParser

# This class defines a complete generic visitor for a parse tree produced by DashSQLParser.

class DashSQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DashSQLParser#program.
    def visitProgram(self, ctx:DashSQLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#statement.
    def visitStatement(self, ctx:DashSQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#simple_stmt.
    def visitSimple_stmt(self, ctx:DashSQLParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#compound_stmt.
    def visitCompound_stmt(self, ctx:DashSQLParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#function_def.
    def visitFunction_def(self, ctx:DashSQLParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#param_list.
    def visitParam_list(self, ctx:DashSQLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#param_def.
    def visitParam_def(self, ctx:DashSQLParser.Param_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#simpleAssignment.
    def visitSimpleAssignment(self, ctx:DashSQLParser.SimpleAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#multiAssignment.
    def visitMultiAssignment(self, ctx:DashSQLParser.MultiAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#id_list.
    def visitId_list(self, ctx:DashSQLParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#expr_list.
    def visitExpr_list(self, ctx:DashSQLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#return_stmt.
    def visitReturn_stmt(self, ctx:DashSQLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#create_table_stmt.
    def visitCreate_table_stmt(self, ctx:DashSQLParser.Create_table_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#column_def_list.
    def visitColumn_def_list(self, ctx:DashSQLParser.Column_def_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#simpleColumnDef.
    def visitSimpleColumnDef(self, ctx:DashSQLParser.SimpleColumnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#reactiveColumnDef.
    def visitReactiveColumnDef(self, ctx:DashSQLParser.ReactiveColumnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#type_name.
    def visitType_name(self, ctx:DashSQLParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#insert_stmt.
    def visitInsert_stmt(self, ctx:DashSQLParser.Insert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#where_from_condition.
    def visitWhere_from_condition(self, ctx:DashSQLParser.Where_from_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#insert_row.
    def visitInsert_row(self, ctx:DashSQLParser.Insert_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#update_stmt.
    def visitUpdate_stmt(self, ctx:DashSQLParser.Update_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#update_assignment.
    def visitUpdate_assignment(self, ctx:DashSQLParser.Update_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#write_stmt.
    def visitWrite_stmt(self, ctx:DashSQLParser.Write_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#select_stmt.
    def visitSelect_stmt(self, ctx:DashSQLParser.Select_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#column_list.
    def visitColumn_list(self, ctx:DashSQLParser.Column_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#where_condition.
    def visitWhere_condition(self, ctx:DashSQLParser.Where_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#join_stmt.
    def visitJoin_stmt(self, ctx:DashSQLParser.Join_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#filter_stmt.
    def visitFilter_stmt(self, ctx:DashSQLParser.Filter_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#sort_stmt.
    def visitSort_stmt(self, ctx:DashSQLParser.Sort_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#for_stmt.
    def visitFor_stmt(self, ctx:DashSQLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#while_stmt.
    def visitWhile_stmt(self, ctx:DashSQLParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#if_stmt.
    def visitIf_stmt(self, ctx:DashSQLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#switch_stmt.
    def visitSwitch_stmt(self, ctx:DashSQLParser.Switch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#caseIsStmt.
    def visitCaseIsStmt(self, ctx:DashSQLParser.CaseIsStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#caseExprStmt.
    def visitCaseExprStmt(self, ctx:DashSQLParser.CaseExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#default_stmt.
    def visitDefault_stmt(self, ctx:DashSQLParser.Default_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#function_call_stmt.
    def visitFunction_call_stmt(self, ctx:DashSQLParser.Function_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#notExpr.
    def visitNotExpr(self, ctx:DashSQLParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:DashSQLParser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#addSubExpr.
    def visitAddSubExpr(self, ctx:DashSQLParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:DashSQLParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#atomExpr.
    def visitAtomExpr(self, ctx:DashSQLParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:DashSQLParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#isExpr.
    def visitIsExpr(self, ctx:DashSQLParser.IsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:DashSQLParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#atom.
    def visitAtom(self, ctx:DashSQLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#function_call.
    def visitFunction_call(self, ctx:DashSQLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#literal_value.
    def visitLiteral_value(self, ctx:DashSQLParser.Literal_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DashSQLParser#condition.
    def visitCondition(self, ctx:DashSQLParser.ConditionContext):
        return self.visitChildren(ctx)



del DashSQLParser