def binarysearch(array,start,end,val):
    if start > end:  # terminating condition
        return False
    else:
        mid = (end +  start )// 2  # first check with middle element and decide the next half based on val of mid 
        if val == array[mid]:
            return True
        elif val < array[mid]:
            return binarysearch(array,start,mid - 1,val) # tail recursion
        elif val > array[mid]:
            return binarysearch(array,mid+1,end,val)

numbers = [2,3,5,6,23,8,12,34,15]
numbers.sort()
length = len(numbers)
print(binarysearch(numbers,0,length-1,6)
