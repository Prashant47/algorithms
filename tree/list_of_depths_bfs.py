# Creates a linked list of all the nodes at each depth using DFS

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

# parent contains nodes in previous level
# current contains nodes in this level
def levelListBFS(root,lists):

    current = []
    if root is None:
        return
    else:
        current.append(root)
        while len(current) is not 0:
            lists.append(current)
            parent = current
            current = []
            for node in parent:
                if node.left is not None:
                    current.append(node.left)
                if node.right is not None:
                    current.append(node.right)
    return lists

def printLists(lists):

    for i in lists:
        for j in i:
            print j.val,
        print("\n")


# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)


lists = []
levelListBFS(root,lists)
printLists(lists)
