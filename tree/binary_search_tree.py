# Binary search tree Operations

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

# inserting in binary search tree
def insert(root,value):
    
    if root is None:
        root = Node(value)
    else:
        if root.val > value:
            if root.left is None:
                root.left = Node(value)
            else:
                insert(root.left, value)
        else: 
            if root.right is None:
                root.right = Node(value)
            else:
                insert(root.right,value)

# return the node given the value
def search(root,value):
    if root is None:
        return
    else:
        if root.val is value:
            return root
        else:
            if root.val > value:
                search(root.left)
            else:
                search(root.right)

def findSuccessor(node):
    if node.right is None:
        return
    else:
        current = node.right
        while current.left:
            current = current.left
        return current

def findPredecessor(node):
    if node.left is None:
        return
    else:
        current = node.left
        while current.right:
            current = current.right
        return current

#iterative delete solution
def delete(root,value):
    cur,prev = root,root

    # cur points to the node that is to be deleted
    # prev points to paraent of that node
    while cur is not None:
        if value < cur.val:
            prev = cur
            cur = cur.left
        else:
            if value > cur.val:
                prev = cur
                cur = cur.right
            else:
                break
    
    if cur.left is None and cur.right is None:  ## Leaf node case
        if prev.left is cur:   # release the cur node by setting its parent link to None 
            prev.left = None
        else:
            prev.right = None
    else:
        if cur.left is None or cur.right is None:  ## Single child case
            if prev.left is cur:
                prev.left = cur.left if cur.left is not None else cur.right
            else:
                prev.right = cur.left if cur.left is not None else cur.right 
        else:
            ## Two child Case
            successor = cur.right
            psuccessor = cur
            while successor.left is not None:
                psuccessor = successor
                successor = successor.left
            # replace successor with node to be deleted
            cur.val = successor.val
            # delete the successor node
            if psuccessor is cur:  # successor is right node of current node
                psuccessor.right = successor.right
            else: # successor is leftmost node in right subtree
                psuccessor.left = successor.right

def deleteRecursive(root,value):

    if root is None:
        return
    # if required node is less than current node
    if value < root.left:
        root.left = deleteRecursive(root.left,value)
    # if required node is greater than current node 
    elif value > root.right:
        root.right = deleteRecursive(root.right,value)
    # when you found the node that is to be deleted
    else:

        # the node to be deleted having only one child 
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # the node to be deleted having two child
        
        # find inorder successor of the node and replace with it
        current = root
        while current.left is not None:
            current = current.left

        # replace the key with inorder successor
        root.key = current.key

        root.right = deleteRecursive(root.right,current.key)

    return root


            
def inorder(root):
    if root is None: 
        return 
    else:
        inorder(root.left)
        print(root.val),
        inorder(root.right)
            

# Create BST 
root = Node(15) 
insert(root,7)
insert(root,12)
insert(root,19)
insert(root,5)
insert(root,10)
insert(root,11)
#insert(root,9)
inorder(root)
delete(root,7)
deleteRecursive(root,7)
print("\nAfter delete")
inorder(root)

