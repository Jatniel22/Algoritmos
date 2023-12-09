class Array(object):
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially

    def __len__(self): # Special def for len()
        return self.__nItems # Return number of items

    def get(self, n): # Return the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds
            return self.__a[n] # Only return item if in bounds

    def set(self, n, value): # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds
            self.__a[n] = value # Only set item if in bounds

    def insert(self, item): # Insert item at end
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1 # Increment number of items

    def find(self, item): # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found
                return j # Then return index to item
        return -1 # Not found -> return -1

    def search(self, item): # Search for item
        return self.get(self.find(item)) # Return item if found

    def delete(self, item): # Delete first occurrence of an item
        for j in range(self.__nItems): # Of current items
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from right over 1
                    self.__a[k] = self.__a[k+1]
                return True # Return success flag
        return False # Made it here, so couldn't find the item

    def traverse(self, function=print): # Traverse all items and apply a function
        for j in range(self.__nItems):
            function(self.__a[j])
    def deleteMaxnum(self):
        if self.__nItems == 0:
            return None  # Retorna None si el array está vacío
        
        max_value = self.__a[0]  # Suponemos que el primer elemento es el máximo inicialmente
        
        for i in range(1, self.__nItems):
            if isinstance(self.__a,()) and self.__a[i] > max_value:
                max_value = self.__a[i]
        
        return max_value
        
        
        
arreglo=Array(5)
arreglo.insert(10)
arreglo.insert(20)
arreglo.insert(30)

# Obtener el tamaño del array
print("Tamaño del array:", len(arreglo))  # Output: Tamaño del array: 3

# Obtener un elemento en una posición específica
element = arreglo.get(1)
print("Elemento en la posición 1:", element)  # Output: Elemento en la posición 1: 20

# Modificar un elemento en una posición específica
arreglo.set(2, 40)

# Recorrer los elementos del array y mostrarlos en la consola
def print_element(element):
    print(element)

arreglo.traverse(print_element)  # Output: 10, 20, 40
max=arreglo.deleteMaxnum()
print("el numero mas alto es: ",max)
arreglo.delete(max)