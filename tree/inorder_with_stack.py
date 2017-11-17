# inorder with using stack

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def inorderWithStack(root):

    if root == None:
        return
    stack = []
    current = root

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            # if stack is not empty then pop print and move to left
            if (len(stack) > 0 ):
                node = stack.pop()
                print(node.val),
                current = node.right

            else:
                print("we are done") # quit condition: current is null and stack is empty
                break

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(12)
root.left.left.right = Node(19)
inorderWithStack(root)
