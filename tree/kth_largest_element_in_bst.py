# Introducing binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
# logic is to traverse inorder node
# and keep track of no of nodes visited

# The code first traverses down to the rightmost node which takes O(h) time, then traverses k elements in O(k) time. 
# Therefore overall time complexity is O(h + k).


class Solution:
    count = 0 
    def klargestNode(self,root,k):
    
        if root == None:
            return
        
        self.klargestNode(root.right,k)
        self.count += 1

        if self.count == k:
            print(root.val)
            return
        
        self.klargestNode(root.left,k)

    
# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.right.right = Node(11)
obj = Solution()
obj.klargestNode(root,2)
