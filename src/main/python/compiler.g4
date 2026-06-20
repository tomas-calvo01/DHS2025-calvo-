grammar compiler;

// ─── Fragments ───────────────────────────────────────────────────────────────
fragment LETRA  : [A-Za-z] ;
fragment DIGITO : [0-9] ;

// ─── Agrupadores ─────────────────────────────────────────────────────────────
PA   : '(' ;
PC   : ')' ;
LLA  : '{' ;
LLC  : '}' ;
CA   : '[' ;
CC   : ']' ;
PYC  : ';' ;
COMA : ',' ;

// ─── Operadores aritméticos ───────────────────────────────────────────────────
ASIG  : '=' ;
SUMA  : '+' ;
RESTA : '-' ;
MULT  : '*' ;
DIV   : '/' ;
MOD   : '%' ;

// ─── Operadores relacionales ──────────────────────────────────────────────────
MENOREQ : '<=' ;
MAYOREQ : '>=' ;
EQUAL   : '==' ;
NEQUAL  : '!=' ;
MENOR   : '<' ;
MAYOR   : '>' ;

// ─── Operadores lógicos ───────────────────────────────────────────────────────
AND : '&&' ;
OR  : '||' ;

// ─── Operadores de incremento/decremento ──────────────────────────────────────
INCREMENTO : '++' ;
DECREMENTO : '--' ;

// ─── Literales numéricos ──────────────────────────────────────────────────────
DECIMAL : DIGITO+ '.' DIGITO+ ;
NUMERO  : DIGITO+ ;

// ─── Palabras reservadas ──────────────────────────────────────────────────────
INT    : 'int' ;
DOUBLE : 'double' ;
FLOAT  : 'float' ;
IF     : 'if' ;
ELSE   : 'else' ;
FOR    : 'for' ;
WHILE  : 'while' ;
RETURN : 'return' ;

// ─── Identificadores ──────────────────────────────────────────────────────────
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

// ─── Ignorar whitespace ───────────────────────────────────────────────────────
WS   : [ \n\r\t] -> skip ;
OTRO : . ;


// ═══════════════════════════════════════════════════════════════════════════════
// REGLAS DEL PARSER
// ═══════════════════════════════════════════════════════════════════════════════

programa : instrucciones EOF ;

instrucciones
    : instruccion instrucciones
    |
    ;

instruccion
    : declaracion
    | asignacion
    | iif
    | iwhile
    | ifor
    | funcion
    | returnstmt
    | llamada
    | bloque
    ;

// ─── Bloque ───────────────────────────────────────────────────────────────────
bloque : LLA instrucciones LLC ;

// ─── While ────────────────────────────────────────────────────────────────────
iwhile : WHILE PA opal PC instruccion ;

// ─── If / else ────────────────────────────────────────────────────────────────
iif   : IF PA opal PC instruccion ielse ;
ielse : ELSE instruccion
      |
      ;

// ─── For ──────────────────────────────────────────────────────────────────────
ifor : FOR PA forInit PYC opal PYC asignacionFor PC bloque ;

forInit
    : tipo ID inic listaVarFor
    | listaAsignacionFor
    ;

listaVarFor
    : COMA ID inic listaVarFor
    |
    ;

listaAsignacionFor : asignacionFor (COMA asignacionFor)* ;

asignacionFor
    : ID ASIG opal
    | ID INCREMENTO
    | ID DECREMENTO
    | INCREMENTO ID
    | DECREMENTO ID
    ;

// ─── Declaración ─────────────────────────────────────────────────────────────
declaracion : tipo ID inic listavar PYC ;

listavar
    : COMA ID inic listavar
    |
    ;

inic
    : ASIG opal
    |
    ;

tipo
    : INT
    | DOUBLE
    | FLOAT
    ;

// ─── Asignación ───────────────────────────────────────────────────────────────
asignacion
    : ID ASIG opal PYC
    | ID INCREMENTO PYC
    | ID DECREMENTO PYC
    | INCREMENTO ID PYC
    | DECREMENTO ID PYC
    ;

// ─── Funciones ────────────────────────────────────────────────────────────────
funcion : tipo ID PA parametros PC bloque ;

parametros
    : tipo ID lista_param
    |
    ;

lista_param
    : COMA tipo ID lista_param
    |
    ;

// ─── Return ───────────────────────────────────────────────────────────────────
returnstmt : RETURN opal PYC ;

// ─── Llamada a función como instrucción ───────────────────────────────────────
llamada : call PYC ;

// ─── Expresiones ─────────────────────────────────────────────────────────────
opal : disyuncion ;

disyuncion : conjuncion dis ;

dis
    : OR conjuncion dis
    |
    ;

conjuncion : relacion con ;

con
    : AND relacion con
    |
    ;

relacion : exp l ;

exp : term e ;

e
    : SUMA  term e
    | RESTA term e
    |
    ;

term : factor t ;

t
    : MULT factor t
    | DIV  factor t
    | MOD  factor t
    |
    ;

l
    : MENOR   exp l
    | MAYOR   exp l
    | MENOREQ exp l
    | MAYOREQ exp l
    | EQUAL   exp l
    | NEQUAL  exp l
    |
    ;

// ─── Factor / llamada ─────────────────────────────────────────────────────────
factor
    : PA opal PC
    | RESTA factor
    | NUMERO
    | DECIMAL
    | call
    | ID
    ;

call : ID PA argumentos PC ;

argumentos
    : opal (COMA opal)*
    |
    ;