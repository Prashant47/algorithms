# Finding the max path sum in binary tree
# the path is connected can be from any node to any other node

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

# this has to be initialised to lowest min value in python.
# As we need deal with negative number we can not keep this value to zero
maxsum = float('-inf')    
def maxPathSum( root):
    global maxsum
    calculateMaxPathSum(root)
    return maxsum
    
def calculateMaxPathSum( root):        
    if root is None:
        return 0
    
    # key cases:
    # max path cab be single node e.g when all nodes are negative max path will be single node having less negative value
    # max path can be other than root also e.g if root is negative and all childs are positive
    
    global maxsum
    # if the values of are negative then zero them
    leftsum = max(calculateMaxPathSum(root.left),0)
    rightsum = max(calculateMaxPathSum(root.right),0)
    
    # max global variable always contains max value till that point of traversal in tree
    maxsum = max(maxsum , root.val + leftsum + rightsum)
    
    # returning value is crucial we are returing max of childs added with current value
    return root.val + max( leftsum , rightsum )


# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(11)
root.left.right = Node(14)
root.right.left = Node(17)
root.right.right = Node(19)
print(maxPathSum(root))
