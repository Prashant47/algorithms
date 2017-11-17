# node definition
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def inorder(root):

    if root == None:
        return
    inorder(root.left)
    print(root.value),
    inorder(root.right)

def preorder(root):

    if root == None:
        return
    print(root.value),
    preorder(root.left)
    preorder(root.right)

def postorder(root):

    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value),


root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(7)
print ( "inorder: "),
inorder(root) 
print ("\npreorder: "),
preorder(root)
print ("\npostorder: "),
postorder(root)
