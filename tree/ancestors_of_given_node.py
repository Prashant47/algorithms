# print all ancestors of given node 
# Assumption: node that is be searched is unique

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def ancestors(root,target):

    if root is None:
        return False

    if root.val == target:
        return True
    
    # ancestors funtion returns true only when data is found,
    # So the true return is propogated upward till root printing the call stack
    # that have reached the target node.
    if ancestors(root.left,target) or ancestors(root.right,target): 
        print(root.val),
        return True

    return False

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(7)
ancestors(root,7)
