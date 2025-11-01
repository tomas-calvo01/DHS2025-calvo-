grammar compiler;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] + ('.' [0-9]+)?  ;

PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
CA : '[' ;
CC : ']' ;
PYC : ';' ;
COMA : ',' ;
ASIG : '=' ;
SUMA : '+' ;
RESTA : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
MENOR : '<' ;
MAYOR : '>' ;
MENOREQ : '<=' ;
MAYOREQ : '>=' ;
EQUAL : '==' ;
NEQUAL : '!=' ;
AND : '&&' ;
OR : '||' ;
NOT : '!' ;

NUMERO : DIGITO+ ;

VOID : 'void';
INT : 'int' ;
DOUBLE : 'double' ;
FLOAT : 'float';
IF : 'if' ;
ELSE : 'else' ;
FOR : 'for' ;
WHILE : 'while' ;
RETURN : 'return' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;


programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
              |
              ;

instruccion : asignacion
            | declaracion
            | iif
            | iwhile
            | bloque
            | ifor
            | funcion
            |returnstmt
            |llamada
            ;

bloque : LLA instrucciones LLC ;

iwhile : WHILE PA opal PC instruccion ;

iif : IF PA opal PC instruccion ielse ;

ielse : ELSE instruccion
           |
           ;

ifor : FOR PA (asignacionFor | declaracionFor) PYC (opal) PYC (asignacionFor) PC bloque ;

asignacionFor : ID ASIG opal
              | ID INCREMENTO
              | ID DECREMENTO
          ;

declaracionFor: tipo ID inic listavar ;

declaracion : tipo ID inic listavar PYC ;

listavar: COMA ID inic listavar
        |
        ;

inic : ASIG opal
     |
     ;

tipo : INT
     | DOUBLE
     | FLOAT
     ;

asignacion : ID ASIG opal PYC
          | ID (INCREMENTO | DECREMENTO) PYC
          
          ;
INCREMENTO : '++' ;
DECREMENTO : '--' ;

opal : exp
     ;

exp : term e ;

e : SUMA term e
  | RESTA term e
  |
  ;

term : factor t
     | factor l
     ;

t : MULT factor t
  | DIV factor t
  | MOD factor t
  |
  ;


factor :  NUMERO
       | ID
       | call
       |PA exp PC
       ;

l : EQUAL factor
  | NEQUAL factor
  | MENOR factor
  | MENOREQ factor
  | MAYOR factor
  | MAYOREQ factor
  | AND factor
  | OR factor
  | NOT factor
  ;

call : ID PA argumentos PC ;

argumentos : exp (COMA exp)* 
                 | 
                 ;
funcion : (tipo | VOID)ID PA parametros PC bloque 
         | (tipo | VOID) ID PA parametros PC PYC
         ;

parametros : tipo ID (COMA tipo ID)* |
                 ;



returnstmt
     : RETURN opal PYC
     ;
 
llamada
    : call PYC
    ;
    
