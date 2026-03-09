%{
#include "punto3.tab.h" // <--- ¡AQUÍ ESTÁ EL CAMBIO!
#include <stdlib.h>
%}

%%

[ \t]+                   { /* Ignorar espacios y tabulaciones */ }
\n                       { return TOK_EOL; }  /* Salto de línea como fin de expresión */

"sqrt"|"SQRT"            { return TOK_SQRT; }

[0-9]+(\.[0-9]+)?        { yylval.val = atof(yytext); return TOK_NUM; }

"+"                      { return '+'; }
"-"                      { return '-'; }
"*"                      { return '*'; }
"/"                      { return '/'; }
"("                      { return '('; }
")"                      { return ')'; }

.                        { printf("Error lexico: Caracter no reconocido '%s'\n", yytext); }

%%

int yywrap() {
    return 1;
}
