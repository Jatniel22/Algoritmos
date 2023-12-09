def identity(x):
    return x

class Mergesort(object):
    def __init__(self, unordered, key=identity):
        self.__arr = unordered
        self.__key = key
        n = len(unordered)
        self.__work = [None] * n  # Use a Python list as the work array
        self.mergesort(0, n)

    def mergesort(self, lo, hi):
        if lo + 1 >= hi:
            return
        mid = (lo + hi) // 2
        self.mergesort(lo, mid)
        self.mergesort(mid, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        i = lo
        j = mid
        for k in range(lo, hi):
            if i < mid and (j >= hi or self.__key(self.__arr[i]) <= self.__key(self.__arr[j])):
                self.__work[k] = self.__arr[i]
                i += 1
            else:
                self.__work[k] = self.__arr[j]
                j += 1
        for k in range(lo, hi):
            self.__arr[k] = self.__work[k]

# Example usage:
unordered = [54, 35, 73, 15, 19, 7]
sorted_array = Mergesort(unordered)
print(sorted_array._Mergesort__arr)  # Access the sorted array
