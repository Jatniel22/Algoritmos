def bubbleSort(self):
    for last in range(self.__nItems - 1, 0, -1):
        # Primero, lleva el elemento más grande de izquierda a derecha
        for inner in range(last):
            if self.__a[inner] > self.__a[inner+1]:
                self.swap(inner, inner+1)
        
        # Luego, retrocede y lleva el elemento más pequeño de derecha a izquierda
        for inner in range(last - 1, 0, -1):
            if self.__a[inner] > self.__a[inner+1]:
                self.swap(inner, inner+1)
