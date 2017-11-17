# Inorder traversal without using stack and recursion 
# using Morris Traversal
#import inorder_with_stack

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
"""
# This solution modifies the give tree
def inorderWithOutStackNotInplace(root):
    if root == None:
        return
    current = root

    while current is not None:
        if current.left == None:
            print(current.val),
            current = current.right  # move to right node
        else: # means node has left subtree
            pre = current.left
            while pre.right != None: 
                pre = pre.right
            pre.right = current
            node = current
            current = current.left
            node.left = None 
"""
def inorderWithOutStack(root):
    if root == None:
        return
    
    current = root

    while current is not None:

        if current.left is None:
            print(current.val),
            current = current.right
        else:
            # Find inorder predecessor of current
            pre = current.left
            while (pre.right is not None and pre.right != current):
                pre = pre.right
            
            # make current as right child of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left

            # Revert the changes made in if part to restore the 
            # original tree i.e., fix the right child of predecssor
            else:
                pre.right = None
                print(current.val),
                current = current.right

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(12)
root.left.left.right = Node(19)
inorderWithOutStack(root)
#inorder_with_stack.inorderWithStack(root)
