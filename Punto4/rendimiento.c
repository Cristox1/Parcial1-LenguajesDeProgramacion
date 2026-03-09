#include <stdio.h>
#include <time.h>

long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int numero = 40; 
    
    clock_t inicio = clock();
    
    long long resultado = fibonacci(numero);
    
    clock_t fin = clock();
    double tiempo_gastado = (double)(fin - inicio) / CLOCKS_PER_SEC;
    
    printf("Resultado: ", resultado);
    printf("Tiempo de ejecucion: ", tiempo_gastado);
    
    return 0;
}