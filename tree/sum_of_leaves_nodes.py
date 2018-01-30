# sume of all leaves in tree 

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def sumAllLeaves(root):
    
    if root.left is None or root.right is None:
        return 0

    if root.left.left is None and root.left.right is None:
        return root.val

    return sumAllLeaves(root.left) + sumAllLeaves(root.right)
        
if __name__ == "__main__":
    # Create a root node
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(4)
    root.right.right = Node(8)
    print(sumAllLeaves(root))
