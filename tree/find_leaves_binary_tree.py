#  Leaves of binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def findLeavesBinaryTree(root):
    
    final = []
    def findleaves(node):
        if node is None:
            return False

        left_node = findleaves(node.left)
        right_node = findleaves(node.right)

        if node.left is None and node.right is None:
            result.append(node.val)
            return True
        else:
            return False
                
        if left_node:
            node.left = None
        if right_node:
            node.right = None

    #while root:
    result = []
    findleaves(root)
    final.append(result)
        
    return final
# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
print(findLeavesBinaryTree(root))
