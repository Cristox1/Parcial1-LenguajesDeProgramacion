%{
#include "punto3.tab.h" 
#include <stdlib.h>
%}

%%

[ \t]+                   {}
\n                       { return TOK_EOL; }  

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
