# balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def height(root):
    if root is None:
        return 0
    h = 1 + max ( height(root.left), height(root.right))


def check_balanced(root):

    if root is None:
        return True

    lheight = height(root.left)
    rheight = height(root.right)

    if abs(lheight-rheight) > 1:
        return False
    else:
        check_balanced(root.left) and check_balanced(root.right)

# Create a root node
root = Node(5)
root.left = Node(3)
root.left.left = Node(1)
root.left.left.left = Node(11)
root.right = Node(8)
print(check_balanced(root))
