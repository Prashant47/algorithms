# Longest Palindromic Subsequence
class Solution:

    def lps(self,S):
        memo = [[0]*len(S) for _ in range(len(S))]
    
        for i in range(len(S)): # setting diagonal elements to 1, single characters are always one lenght palindrome
            memo[i][i] = 1
        # For accessing only upper traingular values keep 3 variables index is for creating i and j 
        # index 2, ...., n +1
        # i 0, ...., n - index + 1  => row
        # j i + index - 1   => col
        for index in range(2,len(S)+1):
            for i in range(len(S)-index+1):
                j =  i + index - 1 
                if S[i] == S[j] and index == 2: #special case for first digonal as values memo[i+1][j-1] might not be available, handle this sepraely
                    memo[i][j] = 2
                elif S[i] == S[j]:
                    memo[i][j] = memo[i+1][j-1] + 2
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j-1])

        return memo[0][len(S) -1] 



if __name__ == "__main__":
    obj = Solution()
    print(obj.lps("BABCBAB"))
