# sum of left leaves 

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        result = 0
        # check for leave in left subtree
        if root.left:
            if root.left.left is None and root.left.right is None:   # find left leaves add to result
                result += root.left.val
            else:
                result += self.sumOfLeftLeaves(root.left)    # didn't find continue the search in left subtree
        
        # check for leaf leavles in right subtree recursively
        result += self.sumOfLeftLeaves(root.right)
        
        return result

# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
print(Solution().sumOfLeftLeaves(root))
