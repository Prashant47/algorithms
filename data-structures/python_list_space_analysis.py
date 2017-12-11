"""
list uses dynamic allocation inside, this can be evident from fixed size of object when new elements are added.
Internally it allocates memeory greater than it requested. 
"""
import sys
test_list = []
iteration = 25
for i in range(iteration):
    n = len(test_list)
    size = sys.getsizeof(test_list)  # get the size of given object
    print("Length of list: {0}, size of list in bytes: {1}".format(n,size))
    test_list.append(i)
