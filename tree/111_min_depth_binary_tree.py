# Introducing binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
