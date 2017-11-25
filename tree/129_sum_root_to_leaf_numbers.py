# sum of root to leaf numbers 

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    
    sumleaf = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumNumbersHelper(root,[])
        return self.sumleaf
        
    def sumNumbersHelper(self,root,path):
        
        if root is None:
            return      
        path.append(root.val)       
        if root.left is None and root.right is None:  # leaf found now add digits and add it to sum
            # pack digits in list to make a number
            add = ""
            for i in path:
                add += str(i)
            self.sumleaf += int(add)
            #self.sumleaf += int(''.join(map(str,path)))  # slow solution
        else:
            # node is not leaf so search in left and right subtree 
            self.sumNumbersHelper(root.left,path[:])  # passing list by value 
            self.sumNumbersHelper(root.right,path[:])


# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
print(Solution().sumNumbers(root))


