import heapq
l = [ 2, 4, 7, 12, 45, 23, 19, 29]

print(heapq.nlargest(3,l), heapq.nsmallest(3,l))