def identity(x):
    return x

class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):
        self.__a = [None] * initialSize
        self.__nItems = 0
        self.__key = key

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if n >= 0 and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index " + str(n) + " is out of range")

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def find_first(self, key):
        lo = 0
        hi = self.__nItems - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__key(self.__a[mid]) == key:
                return mid
            elif self.__key(self.__a[mid]) < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def find_all(self, key):
        lo = self.find_first(key)
        hi = lo
        while hi < self.__nItems and self.__key(self.__a[hi]) == key:
            hi += 1
        return lo, hi

    def delete(self, item):
        lo, hi = self.find_all(self.__key(item))
        found = False
        for i in range(lo, hi):
            if self.__a[i] == item:
                found = True
                for j in range(i, self.__nItems - 1):
                    self.__a[j] = self.__a[j + 1]
                self.__nItems -= 1
                self.__a[self.__nItems] = None
                break
        return found

    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")
        j = self.find_first(self.__key(item))
        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item
        self.__nItems += 1

# Ejemplo de uso
class Record:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"Record({self.key}, {self.value})"

    def __lt__(self, other):
        return self.key < other.key

arr = OrderedRecordArray(10)

arr.insert(Record("clave1", "valor1"))
arr.insert(Record("clave2", "valor2"))
arr.insert(Record("clave1", "valor3"))

print(arr)
