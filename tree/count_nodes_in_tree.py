# count no of nodes in binary tree 

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def count(root):

    if root is None:
        return 0
    else:
        return count(root.left) + count(root.right) + 1

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(11)
print(count(root))
