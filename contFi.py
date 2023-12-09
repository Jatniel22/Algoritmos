# Función de Fibonacci
def fibonacci(n):
    # Variable para contar las llamadas
    fibonacci.calls += 1
    if n <= 0:
        
        return 0
    elif n == 1:
        return 1
    else:
        #fibonacci.cont2+=1
        return fibonacci(n-1) + fibonacci(n-2)

# Inicializar la variable de contador
fibonacci.calls = 0
fibonacci.cont2 = 0

# Ejemplo de uso
n = 5
resultado = fibonacci(n)
print("Resultado de Fibonacci:", resultado)
print("en esta parte se llama :", fibonacci.calls)
#print("en esta oate se llama: ",fibonacci.cont2)