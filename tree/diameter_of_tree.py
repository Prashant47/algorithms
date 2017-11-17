# diameter of tree
# diameter is longest distance between two nodes of tree
# diameter does not need to pass from root

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left),height(root.right))

def diameter(root): 

    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    # it's max of two cases, if first argument is max that means diameter passes through 
    # root and if it's second argument then it's other case where diameter doesn't passes through root
    return max(1 + lheight + rheight, max(ldiameter,rdiameter))

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
print(diameter(root))
