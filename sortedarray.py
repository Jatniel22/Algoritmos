class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            return self.__a[n]  # Only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            self.__a[n] = value  # Only set item if in bounds

    def swap(self, j, k):  # Swap the values at two indices
        if 0 <= j < self.__nItems and 0 <= k < self.__nItems:  # Check if indices are in bounds
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Insert item at the end
        if self.__nItems >= len(self.__a):  # If array is full
            raise Exception("Array overflow")  # Raise exception
        self.__a[self.__nItems] = item  # Item goes at current end
        self.__nItems += 1  # Increment number of items

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found
                return j  # Then return index to element
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # Return item if found

    def delete(self, item):  # Delete first occurrence of an item
        for j in range(self.__nItems):  # Of an item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from right over 1
                    self.__a[k] = self.__a[k + 1]
                return True  # Return success flag
        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items and apply a function
        for j in range(self.__nItems):  # And apply a function
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket
                ans += ", "  # Separate items with comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def bubbleSort(self):  # Sort comparing adjacent vals
        for last in range(self.__nItems - 1, 0, -1):  # And bubble up
            for inner in range(last):  # Inner loop goes up to last
                if self.__a[inner] > self.__a[inner + 1]:  # If elem less than adjacent value, swap
                    self.swap(inner, inner + 1)

    def selectionSort(self):  # Sort by selecting min and swapping min to leftmost
        for outer in range(self.__nItems - 1):  # And swapping min to leftmost
            min_index = outer  # Assume min is leftmost
            for inner in range(outer + 1, self.__nItems):  # Hunt to right
                if self.__a[inner] < self.__a[min_index]:  # If we find new min
                    min_index = inner  # Update the min index
            # __a[min] is the smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min_index)  # Swap leftmost and min

    def insertionSort(self):  # Sort by repeated inserts
        for outer in range(1, self.__nItems):  # Mark one element
            temp = self.__a[outer]  # Store marked elem in temp
            inner = outer  # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner - 1]:  # If marked elem smaller, then shift elem to right
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1
            self.__a[inner] = temp  # Move marked elem to 'hole'
    def parimpar(self):
        cont=True
        conta=0
        while cont:
            
            cont=False
            for last in range(0,self.__nItems-1,2):  # And bubble up
                    for inner in range(last):  # Inner loop goes up to last
                        if self.__a[inner] > self.__a[inner + 1]:  # If elem less than adjacent value, swap
                            self.swap(inner, inner + 1)
                            cont=True
            for last in range(1,self.__nItems,2):  # And bubble up
                    for inner in range(last):  # Inner loop goes up to last
                        if self.__a[inner] > self.__a[inner + 1]:  # If elem less than adjacent value, swap
                            self.swap(inner, inner + 1)
                            cont=True
            conta+=1
        
        print(conta)
        
        
        
             