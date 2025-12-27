# Generated from ./DashSQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DashSQLParser import DashSQLParser
else:
    from DashSQLParser import DashSQLParser

# This class defines a complete listener for a parse tree produced by DashSQLParser.
class DashSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by DashSQLParser#program.
    def enterProgram(self, ctx:DashSQLParser.ProgramContext):
        pass

    # Exit a parse tree produced by DashSQLParser#program.
    def exitProgram(self, ctx:DashSQLParser.ProgramContext):
        pass


    # Enter a parse tree produced by DashSQLParser#statement.
    def enterStatement(self, ctx:DashSQLParser.StatementContext):
        pass

    # Exit a parse tree produced by DashSQLParser#statement.
    def exitStatement(self, ctx:DashSQLParser.StatementContext):
        pass


    # Enter a parse tree produced by DashSQLParser#simple_stmt.
    def enterSimple_stmt(self, ctx:DashSQLParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#simple_stmt.
    def exitSimple_stmt(self, ctx:DashSQLParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#compound_stmt.
    def enterCompound_stmt(self, ctx:DashSQLParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#compound_stmt.
    def exitCompound_stmt(self, ctx:DashSQLParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#function_def.
    def enterFunction_def(self, ctx:DashSQLParser.Function_defContext):
        pass

    # Exit a parse tree produced by DashSQLParser#function_def.
    def exitFunction_def(self, ctx:DashSQLParser.Function_defContext):
        pass


    # Enter a parse tree produced by DashSQLParser#param_list.
    def enterParam_list(self, ctx:DashSQLParser.Param_listContext):
        pass

    # Exit a parse tree produced by DashSQLParser#param_list.
    def exitParam_list(self, ctx:DashSQLParser.Param_listContext):
        pass


    # Enter a parse tree produced by DashSQLParser#param_def.
    def enterParam_def(self, ctx:DashSQLParser.Param_defContext):
        pass

    # Exit a parse tree produced by DashSQLParser#param_def.
    def exitParam_def(self, ctx:DashSQLParser.Param_defContext):
        pass


    # Enter a parse tree produced by DashSQLParser#simpleAssignment.
    def enterSimpleAssignment(self, ctx:DashSQLParser.SimpleAssignmentContext):
        pass

    # Exit a parse tree produced by DashSQLParser#simpleAssignment.
    def exitSimpleAssignment(self, ctx:DashSQLParser.SimpleAssignmentContext):
        pass


    # Enter a parse tree produced by DashSQLParser#multiAssignment.
    def enterMultiAssignment(self, ctx:DashSQLParser.MultiAssignmentContext):
        pass

    # Exit a parse tree produced by DashSQLParser#multiAssignment.
    def exitMultiAssignment(self, ctx:DashSQLParser.MultiAssignmentContext):
        pass


    # Enter a parse tree produced by DashSQLParser#id_list.
    def enterId_list(self, ctx:DashSQLParser.Id_listContext):
        pass

    # Exit a parse tree produced by DashSQLParser#id_list.
    def exitId_list(self, ctx:DashSQLParser.Id_listContext):
        pass


    # Enter a parse tree produced by DashSQLParser#expr_list.
    def enterExpr_list(self, ctx:DashSQLParser.Expr_listContext):
        pass

    # Exit a parse tree produced by DashSQLParser#expr_list.
    def exitExpr_list(self, ctx:DashSQLParser.Expr_listContext):
        pass


    # Enter a parse tree produced by DashSQLParser#return_stmt.
    def enterReturn_stmt(self, ctx:DashSQLParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#return_stmt.
    def exitReturn_stmt(self, ctx:DashSQLParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx:DashSQLParser.Create_table_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx:DashSQLParser.Create_table_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#column_def_list.
    def enterColumn_def_list(self, ctx:DashSQLParser.Column_def_listContext):
        pass

    # Exit a parse tree produced by DashSQLParser#column_def_list.
    def exitColumn_def_list(self, ctx:DashSQLParser.Column_def_listContext):
        pass


    # Enter a parse tree produced by DashSQLParser#simpleColumnDef.
    def enterSimpleColumnDef(self, ctx:DashSQLParser.SimpleColumnDefContext):
        pass

    # Exit a parse tree produced by DashSQLParser#simpleColumnDef.
    def exitSimpleColumnDef(self, ctx:DashSQLParser.SimpleColumnDefContext):
        pass


    # Enter a parse tree produced by DashSQLParser#reactiveColumnDef.
    def enterReactiveColumnDef(self, ctx:DashSQLParser.ReactiveColumnDefContext):
        pass

    # Exit a parse tree produced by DashSQLParser#reactiveColumnDef.
    def exitReactiveColumnDef(self, ctx:DashSQLParser.ReactiveColumnDefContext):
        pass


    # Enter a parse tree produced by DashSQLParser#type_name.
    def enterType_name(self, ctx:DashSQLParser.Type_nameContext):
        pass

    # Exit a parse tree produced by DashSQLParser#type_name.
    def exitType_name(self, ctx:DashSQLParser.Type_nameContext):
        pass


    # Enter a parse tree produced by DashSQLParser#insert_stmt.
    def enterInsert_stmt(self, ctx:DashSQLParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#insert_stmt.
    def exitInsert_stmt(self, ctx:DashSQLParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#where_from_condition.
    def enterWhere_from_condition(self, ctx:DashSQLParser.Where_from_conditionContext):
        pass

    # Exit a parse tree produced by DashSQLParser#where_from_condition.
    def exitWhere_from_condition(self, ctx:DashSQLParser.Where_from_conditionContext):
        pass


    # Enter a parse tree produced by DashSQLParser#insert_row.
    def enterInsert_row(self, ctx:DashSQLParser.Insert_rowContext):
        pass

    # Exit a parse tree produced by DashSQLParser#insert_row.
    def exitInsert_row(self, ctx:DashSQLParser.Insert_rowContext):
        pass


    # Enter a parse tree produced by DashSQLParser#update_stmt.
    def enterUpdate_stmt(self, ctx:DashSQLParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#update_stmt.
    def exitUpdate_stmt(self, ctx:DashSQLParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#update_assignment.
    def enterUpdate_assignment(self, ctx:DashSQLParser.Update_assignmentContext):
        pass

    # Exit a parse tree produced by DashSQLParser#update_assignment.
    def exitUpdate_assignment(self, ctx:DashSQLParser.Update_assignmentContext):
        pass


    # Enter a parse tree produced by DashSQLParser#write_stmt.
    def enterWrite_stmt(self, ctx:DashSQLParser.Write_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#write_stmt.
    def exitWrite_stmt(self, ctx:DashSQLParser.Write_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#select_stmt.
    def enterSelect_stmt(self, ctx:DashSQLParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#select_stmt.
    def exitSelect_stmt(self, ctx:DashSQLParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#column_list.
    def enterColumn_list(self, ctx:DashSQLParser.Column_listContext):
        pass

    # Exit a parse tree produced by DashSQLParser#column_list.
    def exitColumn_list(self, ctx:DashSQLParser.Column_listContext):
        pass


    # Enter a parse tree produced by DashSQLParser#where_condition.
    def enterWhere_condition(self, ctx:DashSQLParser.Where_conditionContext):
        pass

    # Exit a parse tree produced by DashSQLParser#where_condition.
    def exitWhere_condition(self, ctx:DashSQLParser.Where_conditionContext):
        pass


    # Enter a parse tree produced by DashSQLParser#join_stmt.
    def enterJoin_stmt(self, ctx:DashSQLParser.Join_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#join_stmt.
    def exitJoin_stmt(self, ctx:DashSQLParser.Join_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#filter_stmt.
    def enterFilter_stmt(self, ctx:DashSQLParser.Filter_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#filter_stmt.
    def exitFilter_stmt(self, ctx:DashSQLParser.Filter_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#sort_stmt.
    def enterSort_stmt(self, ctx:DashSQLParser.Sort_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#sort_stmt.
    def exitSort_stmt(self, ctx:DashSQLParser.Sort_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#for_stmt.
    def enterFor_stmt(self, ctx:DashSQLParser.For_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#for_stmt.
    def exitFor_stmt(self, ctx:DashSQLParser.For_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#while_stmt.
    def enterWhile_stmt(self, ctx:DashSQLParser.While_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#while_stmt.
    def exitWhile_stmt(self, ctx:DashSQLParser.While_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#if_stmt.
    def enterIf_stmt(self, ctx:DashSQLParser.If_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#if_stmt.
    def exitIf_stmt(self, ctx:DashSQLParser.If_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:DashSQLParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:DashSQLParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#caseIsStmt.
    def enterCaseIsStmt(self, ctx:DashSQLParser.CaseIsStmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#caseIsStmt.
    def exitCaseIsStmt(self, ctx:DashSQLParser.CaseIsStmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#caseExprStmt.
    def enterCaseExprStmt(self, ctx:DashSQLParser.CaseExprStmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#caseExprStmt.
    def exitCaseExprStmt(self, ctx:DashSQLParser.CaseExprStmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#default_stmt.
    def enterDefault_stmt(self, ctx:DashSQLParser.Default_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#default_stmt.
    def exitDefault_stmt(self, ctx:DashSQLParser.Default_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#function_call_stmt.
    def enterFunction_call_stmt(self, ctx:DashSQLParser.Function_call_stmtContext):
        pass

    # Exit a parse tree produced by DashSQLParser#function_call_stmt.
    def exitFunction_call_stmt(self, ctx:DashSQLParser.Function_call_stmtContext):
        pass


    # Enter a parse tree produced by DashSQLParser#notExpr.
    def enterNotExpr(self, ctx:DashSQLParser.NotExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#notExpr.
    def exitNotExpr(self, ctx:DashSQLParser.NotExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#arrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:DashSQLParser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#arrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:DashSQLParser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#addSubExpr.
    def enterAddSubExpr(self, ctx:DashSQLParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#addSubExpr.
    def exitAddSubExpr(self, ctx:DashSQLParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#functionCallExpr.
    def enterFunctionCallExpr(self, ctx:DashSQLParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#functionCallExpr.
    def exitFunctionCallExpr(self, ctx:DashSQLParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#atomExpr.
    def enterAtomExpr(self, ctx:DashSQLParser.AtomExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#atomExpr.
    def exitAtomExpr(self, ctx:DashSQLParser.AtomExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:DashSQLParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:DashSQLParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#isExpr.
    def enterIsExpr(self, ctx:DashSQLParser.IsExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#isExpr.
    def exitIsExpr(self, ctx:DashSQLParser.IsExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:DashSQLParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by DashSQLParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:DashSQLParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by DashSQLParser#atom.
    def enterAtom(self, ctx:DashSQLParser.AtomContext):
        pass

    # Exit a parse tree produced by DashSQLParser#atom.
    def exitAtom(self, ctx:DashSQLParser.AtomContext):
        pass


    # Enter a parse tree produced by DashSQLParser#function_call.
    def enterFunction_call(self, ctx:DashSQLParser.Function_callContext):
        pass

    # Exit a parse tree produced by DashSQLParser#function_call.
    def exitFunction_call(self, ctx:DashSQLParser.Function_callContext):
        pass


    # Enter a parse tree produced by DashSQLParser#literal_value.
    def enterLiteral_value(self, ctx:DashSQLParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by DashSQLParser#literal_value.
    def exitLiteral_value(self, ctx:DashSQLParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by DashSQLParser#condition.
    def enterCondition(self, ctx:DashSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by DashSQLParser#condition.
    def exitCondition(self, ctx:DashSQLParser.ConditionContext):
        pass



del DashSQLParser