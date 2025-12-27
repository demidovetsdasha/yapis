lexer grammar DashSQLLexer;

NEWLINE: '\r'? '\n' -> skip;

CREATE  : 'create';
WITH    : 'with';
INSERT  : 'insert';
TO      : 'to';
WHERE   : 'where';
FROM    : 'from';
WRITE   : 'write';
SELECT  : 'select';
AS      : 'as';
JOIN    : 'join';
AND     : 'and';
OR      : 'or';
FILTER  : 'filter';
BY      : 'by';
SORT    : 'sort';
DESC    : 'desc';
UPDATE  : 'update';
SET     : 'set';
FOR     : 'for';
IN      : 'in';
WHILE   : 'while';
IF      : 'if';
ELSE    : 'else';
SWITCH  : 'switch';
CASE    : 'case';
IS      : 'is';
DEFAULT : 'default';
FUNCTION: 'function';
RETURN  : 'return';

INT_TYPE    : 'int';
STRING_TYPE : 'string';
FLOAT_TYPE  : 'float';
DATE_TYPE   : 'date';
BOOL_TYPE   : 'bool';

DOT2    : '..';
PLUS    : '+';
MINUS   : '-';
DIV     : '/';
MOD     : '%';
EQ      : '==';
NEQ     : '!=';
GTE     : '>=';
LTE     : '<=';
GT      : '>';
LT      : '<';
NOT     : 'not';
MULT    : '*';

LPAREN  : '(';
RPAREN  : ')';
LBRACKET: '[';
RBRACKET: ']';
COMMA   : ',';
COLON   : ':';
EQUALS  : '=';

TRUE_LIT  : 'true';
FALSE_LIT : 'false';

INTEGER
    : [0-9]+
    ;

FLOAT_NUM
    : [0-9]+ '.' [0-9]+
    ;

STRING_LIT
    : '"' (~["\r\n])* '"'
    | '\'' (~['\r\n])* '\''
    ;

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

WS
    : [ \t]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;