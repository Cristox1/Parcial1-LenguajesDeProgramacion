import sys
from antlr4 import *

from punto5Lexer import punto5Lexer
from punto5Parser import punto5Parser
from punto5Visitor import punto5Visitor

class EvaluadorFibo(punto5Visitor):
    def visitStat(self, ctx: punto5Parser.StatContext):
        limite = int(ctx.INT().getText())
        
        secuencia = []
        a, b = 0, 1
        
        while a <= limite: # calculamos la secuencia fibonacci
            secuencia.append(str(a))
            siguiente = a + b
            a = b
            b = siguiente
            
        print(", ".join(secuencia))
        return None

def main():
    print("Calculadora Fibonacci")
    print("Ejemplo: FIBO(NUMERO)")
    print("'salir' para terminar el programa.")
    
    while True:
        try:
            texto = input(">> ")
            if texto.strip().lower() == "salir":
                break
            if not texto.strip():
                continue
                
            input_stream = InputStream(texto)
            lexer = punto5Lexer(input_stream)
            stream = CommonTokenStream(lexer)
            
            parser = punto5Parser(stream)
            arbol = parser.stat() 
            
            if parser.getNumberOfSyntaxErrors() == 0:
                visitante = EvaluadorFibo()
                visitante.visit(arbol)
            else:
                print("Error ingrese FIBO(NUMERO)")
                
        except EOFError:
            break
        except Exception as e:
            print("Ocurrio un error")

if __name__ == '__main__':
    main()
