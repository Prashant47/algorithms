# Introducing binary tree

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# Create a root node
root = Node(5)

root.left = Node(3)
root.right = Node(8)
"""
        5
    /       \
    3       8
/   \    /      \
None None None  None

"""
