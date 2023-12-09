def borbuja(x):
    n = len(x)
    
    # Recorrer todos los elementos de la lista
    for i in range(n):
        
        # Realizar el último i elementos ya están en su posición correcta
        for j in range(0, n-i-1):
            
            # Comparar elementos adyacentes
            if x[j] > x[j+1]:
                # Intercambiar elementos si están en el orden incorrecto
                x[j], x[j+1] = x[j+1], x[j]

# Ejemplo de uso
lista = [5, 3, 8, 2, 10,90,6]
borbuja(lista)
print(lista)
