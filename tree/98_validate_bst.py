# Check weather given tree in binary search tree or not 

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def validateBST(root):
    return isValidBST(root,None,None)


def isValidBST(root, minvalue, maxvalue):    
    if root is None:
        return True
    
    if  ( minvalue is not None and root.val <= minvalue ) or ( maxvalue is not None and root.val >= maxvalue ):
        return False
    
    if not isValidBST(root.left, minvalue, root.val) or not isValidBST( root.right, root.val, maxvalue ):
        return False
    
    return True

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
print(validateBST(root))
