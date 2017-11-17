# print nodes at distance k from root node

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def nodesKDistance(root,k):

    if root is None:
        return
    
    # at each call level decrease value of k by 1
    # when value of k is zero print the node
    if k is 0:
        print(root.val)
    else:
        nodesKDistance(root.left,k-1)
        nodesKDistance(root.right,k-1)


# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(11)
root.right.right = Node(13)
nodesKDistance(root,2)
