# Función de Fibonacci con división de fibonacci.calls
def fibonacci(n):
    if n <= 0:
        # Contar llamada en el bloque if
        fibonacci.calls_if += 1
        return 0
    elif n == 1:
        # Contar llamada en el bloque else
        fibonacci.calls_else += 1
        return 1
    else:
        # Llamada recursiva
        return fibonacci(n - 1) + fibonacci(n - 2)

# Inicializar las variables de contador
fibonacci.calls_if = 0
fibonacci.calls_else = 0

# Ejemplo de uso
n = 5
resultado = fibonacci(n)
print("Resultado de Fibonacci:", resultado)
print("Número de llamadas en el bloque if:", fibonacci.calls_if)
print("Número de llamadas en el bloque else:", fibonacci.calls_else)