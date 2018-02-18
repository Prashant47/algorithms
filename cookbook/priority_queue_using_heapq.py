# implementing priority queue using heapq
import heapq

class Item:
    def __init__(self,name):
        self._name = name
    
    def __str__(self):
         return 'Item({!r})'.format(self._name)



class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority): # pushing -priority as it's min queue, pushing index to make tuple unique as even the element having same priority it will check
                                    # for index which will definately different and higher gets priority
        heapq.heappush(self._queue, (-priority, self._index, item ))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)
    


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('foo1'), 8)
    q.push(Item('foo2'), 5)
    q.push(Item('foo3'), 3)

    print(q._queue)
    print(q.pop())
