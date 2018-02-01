# Generating subsets using recursive approach 
# calls 2^n
def subset(arr,sub,i):
    if i == len(arr):
	    print(sub)
    else :
        subset(arr, sub[:], i+1) # call without adding one element in arr
        sub.append(arr[i])
        subset(arr, sub[:], i+1) # call adding one element in arr
		
arr = [1,2,3]
subset(arr,[],0)	
