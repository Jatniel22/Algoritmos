import arreglo
def custom_key(item):
    return item  # Suponiendo que los elementos son directamente comparables

# Crear una instancia de la clase
record_array = arreglo.OrderedRecordArray(10, custom_key)


# Ingresar datos utilizando el método insert()
record_array.insert(5)
record_array.insert(3)
record_array.insert(8)
record_array.insert(20)
record_array.insert(5)
record_array.insert(20)

# Imprimir los elementos utilizando el método traverse()
record_array.traverse()
arr=record_array.get_array()
tam=len(arr)
for i in 1,range(tam):
    elemento=record_array.get_array()
    if(elemento[i]==elemento[i-1]):
        record_array.delete()
        
record_array.traverse()
    