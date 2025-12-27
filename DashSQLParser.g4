parser grammar DashSQLParser;

options {
    tokenVocab = DashSQLLexer;
}

program
    : statement* EOF
    ;

statement
    : simple_stmt
    | compound_stmt
    ;

simple_stmt
    : create_table_stmt
    | insert_stmt
    | update_stmt
    | write_stmt
    | select_stmt
    | join_stmt
    | filter_stmt
    | sort_stmt
    | assignment_stmt
    | function_call_stmt
    | return_stmt
    ;

compound_stmt
    : if_stmt
    | for_stmt
    | while_stmt
    | switch_stmt
    | function_def
    ;

// Функция
function_def
    : FUNCTION ID LPAREN param_list? RPAREN COLON statement+
    ;

param_list
    : param_def (COMMA param_def)*
    ;

param_def
    : ID COLON type_name
    ;

// Присваивание
assignment_stmt
    : ID EQUALS expr                           # simpleAssignment
    | id_list EQUALS expr_list                 # multiAssignment
    ;

id_list
    : ID (COMMA ID)*
    ;

expr_list
    : expr (COMMA expr)*
    ;
    
// Return
return_stmt
    : RETURN expr
    ;

// Create table
create_table_stmt
    : CREATE ID WITH LPAREN column_def_list RPAREN
    ;

column_def_list
    : column_def (COMMA column_def)*
    ;

column_def
    : ID COLON type_name (EQUALS expr)?                  # simpleColumnDef
    | ID COLON type_name EQUALS COLON statement+         # reactiveColumnDef
    ;

type_name
    : INT_TYPE | STRING_TYPE | FLOAT_TYPE | DATE_TYPE | BOOL_TYPE
    ;

// Insert
insert_stmt
    : INSERT TO ID (where_from_condition)? COLON insert_row+
    ;

where_from_condition
    : WHERE ID FROM ID
    ;

insert_row
    : id_list EQUALS expr_list
    ;

// Update
update_stmt
    : UPDATE ID SET update_assignment (COMMA update_assignment)* (WHERE condition)?
    ;

update_assignment
    : ID EQUALS expr
    ;

// Write
write_stmt
    : WRITE expr
    | WRITE LPAREN expr RPAREN
    ;

// Select
select_stmt
    : SELECT column_list FROM ID where_condition? (AS ID)?
    ;

column_list
    : MULT
    | ID (COMMA ID)*
    ;

where_condition
    : WHERE condition
    ;

// Join
join_stmt
    : JOIN ID WITH ID BY ID AND ID (AS ID)?
    ;

// Filter
filter_stmt
    : FILTER ID BY condition (AS ID)?
    ;

// Sort
sort_stmt
    : SORT LT DESC GT? ID BY ID (AS ID)?
    | SORT ID BY ID (AS ID)?
    ;

// For
for_stmt
    : FOR ID IN expr DOT2 expr COLON statement+
    | FOR ID IN ID COLON statement+
    ;

// While
while_stmt
    : WHILE condition COLON statement+
    ;

// If
if_stmt
    : IF condition COLON statement+ (ELSE COLON statement+)?
    ;

// Switch - ИСПРАВЛЕНО
switch_stmt
    : SWITCH expr COLON (case_stmt | default_stmt)+
    ;

// ОСНОВНОЕ ИСПРАВЛЕНИЕ: добавлена поддержка case is expr
case_stmt
    : CASE IS expr COLON statement+   # caseIsStmt
    | CASE expr COLON statement+      # caseExprStmt
    ;

default_stmt
    : DEFAULT COLON statement+
    ;

// Вызов функции как statement
function_call_stmt
    : function_call
    ;

// Выражения
expr
    : expr IS expr                                    # isExpr
    | expr (GT | LT | GTE | LTE | EQ | NEQ) expr     # comparisonExpr
    | expr (PLUS | MINUS) expr                       # addSubExpr
    | expr (MULT | DIV | MOD) expr                   # mulDivExpr
    | NOT expr                                       # notExpr
    | ID LBRACKET expr RBRACKET                      # arrayAccessExpr
    | function_call                                  # functionCallExpr
    | atom                                           # atomExpr
    ;

atom
    : LPAREN expr RPAREN
    | literal_value
    | ID
    ;

function_call
    : ID LPAREN expr_list? RPAREN
    ;

literal_value
    : INTEGER
    | FLOAT_NUM
    | STRING_LIT
    | TRUE_LIT
    | FALSE_LIT
    ;

condition
    : expr (AND expr)*
    | expr (OR expr)*
    ;