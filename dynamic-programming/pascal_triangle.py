# 
class Solution:

    def pascalOptimized(self,n):
        row = [0 for _ in range(n+1)] 

        row[0] = 1

        for i in range(n+1):
            for j in range(i,n+1):
                row[j] = row[j] + row[j-1]
            print(row)
        
    def pascal(self,n):
    
        memo = [[0]*n for _ in range(n) ]
        for row in range(n):
            for col in range(row+1):
                if row == col or col == 0:
                    memo[row][col] = 1
                else:
                    memo[row][col] = memo[row-1][col] + memo[row-1][col-1]
            print(memo[row][:col+1])
                    


if __name__ == "__main__":
    obj = Solution()
    obj.pascal(5)
