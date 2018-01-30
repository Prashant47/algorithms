# Introducing binary tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def pathsumfour(nums):
    
    struct = {}
    for node in nums:
        struct[node[:2]] = node[2:3]

    graph = {}    
    for node in nums:
        h,t = node[0], node[1]
        left, right = h + str(2*int(t)-1), h + str(2*int(t))
        
        #nei = [ struct[left] if left in struct else None , struct[right] if right in struct else None  ]
        nei = [ struct[left] if left in struct else None , struct[right] if right in struct else None  ]
        
        nei = [ for i in (left,right) struct[i] if i in struct else None ]

        graph[node[2]] = nei
    print(graph)

         
            
# Create a root node
root = Node(5)
root.left = Node(3)
root.right = Node(8)
nums = ["115","213","224"]
pathsumfour(nums)
