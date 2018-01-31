# 0-1 knapsack problem
# weight = [5,4,6,1]
# val =    [7,8,9,4]
# capacity = 10
class Solution:

    def bruteForceKnapsack(self, weight, val, capacity, item):
        
        if capacity == 0 or item == 0: # terminate condition
            return 0
        
        if weight[item - 1] > capacity: # pruning the subset tree if the weight is more than capacity cut down the branch
            return self.bruteForceKnapsack( weight, val, capacity, item - 1 ) # just call the not selecting branch 
        else:
            consider = val[item - 1] + self.bruteForceKnapsack( weight, val, capacity - weight[item - 1],item -1) 
            not_consider = self.bruteForceKnapsack( weight, val, capacity, item - 1 )
        return max(consider,not_consider) # max of either of two branchs

    def knapsackDP(self,weight,val,capacity,item):
        
        memo = [[0]*(capacity+1) for _  in range(item+1)]
        
        for wt in range(item+1):
            for cap in range(capacity+1):
                if wt == 0 or cap == 0:
                    memo[wt][cap] = 0
                elif weight[wt - 1 ] > cap:
                    memo[wt][cap] = memo[wt-1][cap] # consider above row i.et not considering current item but considering till last item
                else:
                    memo[wt][cap] = max(val[wt - 1] + memo[wt-1][cap - weight[wt-1]], memo[wt-1][cap] )
        for row in memo:
            print(row)
        return memo[wt][cap] 

if __name__ == "__main__":
    obj = Solution()
    #weight = [1,2,4,2,5]
    #val = [5,3,5,3,2]
    weight = [3,1,4,5]
    val =    [4,1,5,7]
    capacity = 7 
    item = len(val)
    print(obj.bruteForceKnapsack(weight,val,capacity,item))
    print(obj.knapsackDP(weight,val,capacity,item))
