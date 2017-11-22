# Introducing binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def largestValues(root):
       
        maxvalues = []
        
        if root is None:
            return maxvalues
        parent = [root]
        # add parent nodes in each level
        while len(parent) > 0:
            maxvalues.append( max(node.val for node in parent) )
            # short comprehend 
            # for node in parent
            #     for child in (node.left,node.right)
            #           select child if child is not None
            parent = [ child for node in parent for child in (node.left,node.right) if child ]
            
        return maxvalues 

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
print(largestValues(root))
