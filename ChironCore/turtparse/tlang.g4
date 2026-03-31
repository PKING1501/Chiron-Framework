grammar tlang;

// ============================================================================
// PARSER RULES
// ============================================================================

start : instruction_list EOF
      ;

instruction_list : (instruction)*
                 ;

strict_ilist : (instruction)+
             ;

instruction : assignment
            | arrayDecl
            | arrayAssignment
            | conditional
            | loop
            | moveCommand
            | penCommand
            | gotoCommand
            | pauseCommand
            ;

arrayDecl : VAR type '[' NUM ']' ;
arrayAssignment : VAR '[' expr ']' '=' expr ;

conditional : ifConditional | ifElseConditional ;

ifConditional : 'if' expr '[' strict_ilist ']' ;          // changed from condition
ifElseConditional : 'if' expr '[' strict_ilist ']' 'else' '[' strict_ilist ']' ; // changed

loop : 'repeat' value '[' strict_ilist ']' ;

gotoCommand : 'goto' '(' expr ',' expr ')' ;              // changed from expression

assignment : VAR typeAnnotation? '=' expr ;                // changed from expression

typeAnnotation : type ;

type : 'int' | 'float' | 'double' | 'string' | 'boolean' ;

moveCommand : moveOp expr ;                                // changed
moveOp : 'forward' | 'backward' | 'left' | 'right' ;

penCommand : 'penup' | 'pendown' ;

pauseCommand : 'pause' ;

// Unified expression grammar with precedence (lowest to highest)
expr : orExpr ;

orExpr : andExpr ( OR andExpr )* ;
andExpr : equalityExpr ( AND equalityExpr )* ;
equalityExpr : relationalExpr ( ( EQ | NEQ ) relationalExpr )* ;
relationalExpr : additiveExpr ( ( LT | GT | LTE | GTE ) additiveExpr )* ;
additiveExpr : multiplicativeExpr ( ( PLUS | MINUS ) multiplicativeExpr )* ;
multiplicativeExpr : unaryExpr ( ( MUL | DIV ) unaryExpr )* ;
unaryExpr : ( MINUS | NOT )? primary ;
primary : value                  #primaryValue
        | '(' expr ')'           #parenExpr
        | PENCOND                #penCondition
        | VAR '[' expr ']'       #arrayAccessExpr
        ;

value : NUM          #numValue
      | FLOAT        #floatValue
      | DOUBLE       #doubleValue
      | STRING       #stringValue
      | BOOLEAN      #booleanValue
      | VAR          #varValue
      ;

// ============================================================================
// LEXER RULES
// ============================================================================

PENCOND : 'pendown?' ;
LT : '<' ;
GT : '>' ;
EQ : '==' ;
NEQ : '!=' ;
LTE : '<=' ;
GTE : '>=' ;
AND : '&&' ;
OR : '||' ;
NOT : '!' ;
PLUS : '+' ;
MINUS : '-' ;
MUL : '*' ;
DIV : '/' ;

NUM  : [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+ [fF] ;
DOUBLE : [0-9]+ '.' [0-9]+ ([dD])? | [0-9]+ [dD] ;
STRING : '"' (~["\r\n\\] | '\\' .)* '"' ;
BOOLEAN : 'true' | 'false' ;
VAR  : ':'?[a-zA-Z_] [a-zA-Z_0-9]* ;
NAME : [a-zA-Z]+ ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
Whitespace : [ \t\n\r]+ -> skip ;