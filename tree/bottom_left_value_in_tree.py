# finding bottom left value if binary search tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def findBottomLeftValue(root):
        
    current = [] # contains nodes are current level
    parent = [] # contains nodes at previous level
    current.append(root)  # initializing with root
    # loop break condition:  no more elements to add i.e all leaf nodes in parent
    while len(current) > 0:
        parent = current
        current = []  # clearing current for next level 
        # for each node at previous level add it's children
        for node in parent:
            if node.left is not None:
                current.append(node.left)
            if node.right is not None:
                current.append(node.right)
    # always pick first element to get bottom left 
    return parent[0].val


# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.right.left = Node(10)
root.right.left.right = Node(11)
print(findBottomLeftValue(root))
