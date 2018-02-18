from collections import OrderedDict
import sys
import operator
# preserves the order of list
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# OrderedDict() internally used doubly linked list, when new item is inserted, it's get added at the end
# IMP:- OrderedDict() takes twice as much space as normal dict
ord_dict = OrderedDict()
normal_dict = dict()
print(sys.getsizeof(ord_dict), sys.getsizeof(normal_dict))


############### Finding max, min and sorting in dictionaries ###########
values = { 'a': 1, 'b':2, 'c':3, 'd':4}
# Approach-1
max_dict = max(values.items(),  key=operator.itemgetter(1))
min_dict = min(values.items(),  key=operator.itemgetter(1)) 
sorted_dict = sorted(values.items(),  key=operator.itemgetter(1))
print(max_dict,min_dict,sorted_dict)

# Approach-2
max_dict = max(zip(values.values(),values.keys()))
min_dict = min(zip(values.values(),values.keys()))
sorted_dict = sorted(zip(values.values(),values.keys()))
print(max_dict,min_dict,sorted_dict)

##################### Find common between two dictionaries ##############

a = {   'x' : 1,   'y' : 2,   'z' : 3}
b = {   'w' : 10,   'x' : 11,   'y' : 2}

print(set(a.items()) & set(b.items()))

# exclude some of the keys 
c = {  key:a[key] for key in set(a.keys()) - {'x','y'}  }
print(c)
