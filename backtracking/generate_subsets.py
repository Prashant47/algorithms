# Generate all subsets 
# adding each element in one row, i.e for cur_comb call recursively for adding element and not adding element
# complexity 2^n
class Solution:

    def generateSubsets(self,arr,cur_comb,n):
        if n  == 0:  # base condition to end 
            print(cur_comb)
        else:
            self.generateSubsets(arr,cur_comb, n - 1)
            cur_comb.append(arr[n-1])
            self.generateSubsets(arr,cur_comb, n - 1)
            cur_comb.pop()  # otherwise we have to send seperate copy to each call


if __name__ == "__main__":
    obj = Solution()
    arr = [1,2,3]
    obj.generateSubsets(arr,[],len(arr))
