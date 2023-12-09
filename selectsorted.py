def selectionSort(lista):
    for outer in range(len(lista)-1):  # Recorre la lista desde el primer elemento hasta el penúltimo
        min = outer  # Asigna el índice del elemento actual como el índice del mínimo inicialmente
        for inner in range(outer+1, len(lista)):  # Recorre la lista desde el siguiente elemento hasta el final
            if lista[inner] < lista[min]:  # Comprueba si encuentra un nuevo elemento mínimo
                min = inner  # Actualiza el índice del nuevo elemento mínimo encontrado
        lista[outer], lista[min] = lista[min], lista[outer]  # Intercambia el elemento mínimo con el elemento en la posición actual (leftmost)

# Ejemplo de uso
lista=[]
for i in 1,10:
    lista.append(int(input("digite: ")))
    
selectionSort(lista)
print("Lista ordenada:")
print(lista)
