# Introducing binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def countLeafNodes(root):
    
    if root == None:
        return 0
    
    if root.left == None and root.right == None:
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)

def countNonLeafNodes(root):
    
    if root == None:
        return 0

    if root.left == None or root.right == None:
        return 0
    else:
        return 1 + countNonLeafNodes(root.left) + countNonLeafNodes(root.right)



# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(11)
root.left.right = Node(11)
root.right.right = Node(19)
print(countLeafNodes(root))
print(countNonLeafNodes(root))
