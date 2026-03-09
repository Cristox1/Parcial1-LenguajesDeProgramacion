%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(const char *s);
int yylex(void);
extern FILE *yyin; 

double newton_raphson_sqrt(double S);/* Declaración del metodo Newton Raphson */
%}

%union { /* Los tokens van a manejar valores decimales */
    double val;
}

%token <val> TOK_NUM
%token TOK_SQRT TOK_EOL
%type <val> exp


%left '+' '-'
%left '*' '/'
%nonassoc UMINUS 

%%

/* Reglas Gramaticales */
calc:
    | calc exp TOK_EOL { printf("-> Resultado: %f\n", $2); }
    | calc TOK_EOL     {}
    | calc error TOK_EOL { yyerrok;}
    ;

exp:
    TOK_NUM                { $$ = $1; }
    | exp '+' exp          { $$ = $1 + $3; }
    | exp '-' exp          { $$ = $1 - $3; }
    | exp '*' exp          { $$ = $1 * $3; }
    | exp '/' exp          { 
        if($3 == 0) {
            yyerror("Error: Division por cero");
            $$ = 0;
        } else {
            $$ = $1 / $3; 
        }
    }
    | '-' exp %prec UMINUS { $$ = -$2; }
    | '(' exp ')'          { $$ = $2; }
    | TOK_SQRT '(' exp ')' { $$ = newton_raphson_sqrt($3); }
    ;

%%

double newton_raphson_sqrt(double S) {
    if (S < 0) {
        printf("\n[!] Error: No se puede calcular numeros negativos (%.2f)\n", S);
        return 0.0;
    }
    if (S == 0) return 0.0;
    
    double x_n = S; 
    double x_siguiente;
    double tolerancia = 0.000001; 
    int iteraciones = 0;
    
    while (1) {
        iteraciones++;
        x_siguiente = 0.5 * (x_n + (S / x_n)); // Formula de Newton-Raphson: x_(n+1) = 0.5 * (x_n + S / x_n)
        if (fabs(x_n - x_siguiente) < tolerancia) {
            break;
        }
        x_n = x_siguiente; // Actualizamos para la siguiente iteración
    }
       
    return x_siguiente;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error Sintactico: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Error");
        return 1;
    }

    FILE *archivo = fopen(argv[1], "r");
    if (!archivo) {
        printf("Error: No se pudo abrir el archivo: %s\n", argv[1]);
        return 1;
    }

    yyin = archivo;
    
    printf(" Caculadora que halla raices: =\n");
    
    yyparse(); 

    fclose(archivo);

    printf("Analisis finalizado.\n");
    return 0;
}
