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
	    | conditional
	    | loop
	    | moveCommand
	    | penCommand
	    | gotoCommand
	    | pauseCommand
	    ;

conditional : ifConditional | ifElseConditional ;

ifConditional : 'if' condition '[' strict_ilist ']' ;

ifElseConditional : 'if' condition '[' strict_ilist ']' 'else' '[' strict_ilist ']' ;

loop : 'repeat' value '[' strict_ilist ']' ;

gotoCommand : 'goto' '(' expression ',' expression ')';

// Assignment now supports optional type annotations
assignment : VAR typeAnnotation? '=' expression
	   ;

// Type annotation syntax (e.g., :x int = 5)
typeAnnotation : type
               ;

// Type system - supports int, float, double, string, boolean
type : 'int'
     | 'float' 
     | 'double'
     | 'string'
     | 'boolean'
     ;

moveCommand : moveOp expression ;

moveOp : 'forward' | 'backward' | 'left' | 'right' ;

penCommand : 'penup' | 'pendown' ;

pauseCommand : 'pause' ;

// ============================================================================
// FIXED: Expression with CORRECT precedence
// Precedence (lowest to highest): +/-, */, unary-, atoms
// ============================================================================
expression : '(' expression ')'                 #parenExpr    // Highest: parentheses
        | value                                 #valueExpr    // Highest: literals/vars
        | unaryArithOp expression               #unaryExpr    // Higher: unary -
        | expression multiplicative expression  #mulExpr      // Higher: * /
        | expression additive expression        #addExpr      // Lowest: + -
 	   ;

multiplicative : MUL | DIV;

additive : PLUS | MINUS;

unaryArithOp : MINUS ;

PLUS     : '+' ;
MINUS    : '-' ;
MUL  	 : '*' ;
DIV      : '/' ;

// ============================================================================
// FIXED: Condition with proper precedence
// Precedence (lowest to highest): OR, AND, NOT, comparisons, atoms
// ============================================================================
condition : expression binCondOp expression     #comparisonCondition  // Higher than NOT
          | NOT condition                       #notCondition     // Higher than AND
          | condition AND condition             #andCondition     // Higher than OR
		  | condition OR condition              #orCondition       // Lowest
		  | value                               #atomicCondition  // Atomic (for booleans)
          | '(' condition ')'                   #parenCondition   // Override precedence
          | PENCOND                             #penCondition     // Atomic
          ;

binCondOp :  EQ | NEQ | LT | GT | LTE | GTE
	 ;

PENCOND : 'pendown?';

LT : '<' ;
GT : '>' ;
EQ : '==';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
AND: '&&';
OR : '||';
NOT: '!' ;

// value now includes all literal types
value : NUM          #numValue
      | FLOAT        #floatValue
      | DOUBLE       #doubleValue
      | STRING       #stringValue
      | BOOLEAN      #booleanValue
      | VAR          #varValue
      ;

// ============================================================================
// LEXER RULES (Tokens)
// ============================================================================

// NUM now explicitly represents integers only
NUM  : [0-9]+        ;

// Float literal (e.g., 3.5f or 3.5F)
FLOAT : [0-9]+ '.' [0-9]+ [fF] ;

// Double literal (e.g., 3.5 or 3.5d or 3.5D)
DOUBLE : [0-9]+ '.' [0-9]+ ([dD])?
       | [0-9]+ [dD]
       ;

// String literal (double-quoted)
STRING : '"' (~["\r\n\\] | '\\' .)* '"' ;

// Boolean literals
BOOLEAN : 'true' | 'false' ;

VAR  : ':'[a-zA-Z_] [a-zA-Z0-9]* ;

NAME : [a-zA-Z]+     ;

// ============================================================================
// COMMENTS (must come before Whitespace)
// ============================================================================

// Single-line comment: // comment text
LINE_COMMENT : '//' ~[\r\n]* -> skip ;

// Multi-line comment: /* comment text */
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

// ============================================================================
// WHITESPACE (must come last)
// ============================================================================

Whitespace: [ \t\n\r]+ -> skip;