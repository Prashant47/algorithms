# Introducing binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.next = None
        self.val = val

def connect(root):

    if root is None:
        return
    # BFS
    queue = [root]
    
    while queue:
        size = len(queue)
        
        for i in range(size):
            node = queue.pop(0)
            
            if i + 1 != size:
                node.next = queue[i+1]
            else:
                node.next = None
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
connect(root)
