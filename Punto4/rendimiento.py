import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    numero = 40
    
    inicio = time.time()
    
    resultado = fibonacci(numero)
    
    fin = time.time()
    tiempo_gastado = fin - inicio
    
    print("Resultado", resultado)
    print("Tiempo de ejecucion:", tiempo_gastado)
