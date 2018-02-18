from collections import deque
# concept of bounded queue
# this can be done by using list of fixed size let's say [ 1, 2, 3]
# and two pointers front and rear
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
