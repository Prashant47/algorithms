# Creates a linked list of all the nodes at each depth using DFS

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
# depth started from 0 which maps to 0th index of lists
# at each level of iteration pass level + 1 
def levelListDFS(root,lists,level):

    if root is None:
        return
    if len(lists) is level:
        # this is the first time we have reached to depth of level,
        # so creating list for level and add the curret node in it
        temp = []
        lists.append(temp)

    lists[level].append(root)
    levelListDFS(root.left,lists,level+1)
    levelListDFS(root.right,lists,level+1)


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
levelListDFS(root,lists,0)
printLists(lists)
