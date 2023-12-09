
def identity(x):
    return x

class Mergesort(object):
    def __init__(self, unordered, key=identity):
        self.__arr = unordered  # Almacena la lista desordenada
        self.__key = key        # La función 'key' se utiliza para extraer claves de elementos
        n = len(unordered)
        self.__work = [None] * n  # Utiliza una lista de Python como arreglo de trabajo
        self.mergesort(0, n)

    def mergesort(self, lo, hi):
        if lo + 1 >= hi:  # Si la lista tiene 1 o menos elementos, no se hace nada
            return
        mid = (lo + hi) // 2  # Divide la lista en dos mitades
        self.mergesort(lo, mid)  # Ordena la primera mitad
        self.mergesort(mid, hi)  # Ordena la segunda mitad
        self.merge(lo, mid, hi)  # Combina las dos mitades ordenadas

    def merge(self, lo, mid, hi):
        i = lo
        j = mid
        for k in range(lo, hi):
            if i < mid and (j >= hi or self.__key(self.__arr[i]) <= self.__key(self.__arr[j])):
                # Compara y coloca el elemento más pequeño en 'self.__work'
                self.__work[k] = self.__arr[i]
                i += 1
            else:
                self.__work[k] = self.__arr[j]
                j += 1
        for k in range(lo, hi):
            self.__arr[k] = self.__work[k]  # Copia los elementos ordenados de 'self.__work' a 'self.__arr'

# Ejemplo de uso:
unordered = [54, 35, 73, 15, 19, 7]
sorted_array = Mergesort(unordered)  # Clase Mergesort se utiliza para ordenar la lista
print(sorted_array._Mergesort__arr)  # Acceder al arreglo ordenado
