# Crear una instancia de la clase que contiene el método selectionSort
objeto = NombreClase()

# Asignar la lista o arreglo que se desea ordenar a la propiedad "__a" del objeto
objeto.__a = [64, 34, 25, 12, 22, 11, 90]

# Obtener el número de elementos en la lista
objeto.__nItems = len(objeto.__a)

# Llamar al método selectionSort para ordenar la lista
objeto.selectionSort()

# Imprimir la lista ordenada
print(objeto.__a)
