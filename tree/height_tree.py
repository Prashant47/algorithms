"""
Height:-  the number of nodes along the longest path 
from the root node down to the farthest leaf node
"""

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(13)
print(height(root))
