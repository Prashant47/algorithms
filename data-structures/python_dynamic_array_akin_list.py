# dynamic array similar to build-in list data structure in python

import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0   # current total numbers in array
        self._size = 1  # underlaying size of array, increased by double every time
        self._array = self._make_array(self._size) # underlaying static array

    def __len__(self): # returns length of array
        return self._n

    def __getitem__(self,k):  # this is for working of a[k] indexing operation over array 
        if not 0 <= k < self._n:
            raise IndexError('Index out of bound')
        return self._array[k]

    def append(self,val):  # append val at the end of array
        if self._n == self._size:
            self._resize(2 * self._size)
        self._array[self._n] = val
        self._n += 1

    def _resize(self,new_size): # resize the internal array to new_size
        temp = self._make_array(new_size)
        for i in range(self._n):
            temp[i] = self._array[i]
        self._array = temp
        self._size = new_size

    def _make_array(self,size):   # using cytypes for array
        return (size * ctypes.py_object)()

        
if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(3)
    arr.append(5)
    print(len(arr))
    print(arr[5])
