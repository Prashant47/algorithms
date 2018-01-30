# print path to leaves

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def printPathToLeaves(root,path):

    if root is None:
        return

    # append the current node in list
    path.append(root.val)

    # you have reached to leave now print the content
    if root.left is None and root.right is None:
        print(path)
    else:
        # current node is not leave so call recursively to left and right trees
        printPathToLeaves(root.left,path[:]) # passing list by value not by reference path[:] creates new object
        printPathToLeaves(root.right,path[:])


# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(7)
root.left.right = Node(9)
printPathToLeaves(root,[])
