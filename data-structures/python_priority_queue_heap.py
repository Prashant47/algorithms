""" min oriented priority queue implemented with binary heap array based implementation """
from python_priority_queue import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):

    def _parent(self,j):
        return (j - 1) // 2

    def _left(self,j):
        return 2*j + 1

    def _right(self,j):
        return 2*j + 2

    def _has_left(self,j):
        return self._left(j) < len(self._data)

    def _has_right(self,j):
        return self._right(j) < len(self._data)

    def _swap(self,i,j):
        """ swap the elements at indices i and j """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)
    
    def _downheap(self,j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self.data[right] < self.data[left]: 
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)

    ########################## Public Methods #############################

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self,key,value):
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data) - 1 )

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[0]  # getting root element
        return (item._key,item._value)

if __name__ == "__main__":
    heapq = HeapPriorityQueue()
    heapq.add(3,4)
    heapq.add(8,21)
    heapq.add(2,3)
    heapq.add(4,5)
    print(heapq.min())
