# using queue level order traversal

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    
    if root == None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.value),
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
            
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.right = Node(7)
root.left.left = Node(9)
levelOrderTraversal(root)
