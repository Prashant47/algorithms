# 
# n => no of columns
# k => no of rows
# 
class Solution:

    def function(self,n,k):

        memo = [[0]*n for _ in range(k+1)] # added extra row for k = 0
        #print(memo) 
        for index in range(n): # nC0 = 1 for all n
            memo[0][index] = 1 
        # iterate col from 1 to end so accesss memo col as 1 less than usual to it to list
        for row in range(1,k+1):
            for col in range(1,n+1):
                if row == col:
                    memo[row][col-1] = 1
                elif col < row:
                    memo[row][col-1] = 0
                else:                        
                    memo[row][col-1] = memo[row][col-2] + memo[row-1][col-2]    
        #for temp in memo:
        #    print(temp)
        return memo[k][n-1]   

    def recursiveBionomialCoeff(self, n, k):
        if k == 0 or n == k:
            return 1
        else:
            return self.recursiveBionomialCoeff( n -1, k) + self.recursiveBionomialCoeff(n - 1, k - 1)    
if __name__ == "__main__":
    obj = Solution()
    print(obj.recursiveBionomialCoeff(4,3))
    print(obj.function(4,3))
