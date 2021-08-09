def mergeSort(arr, left, right, temp_arr):
    inv_count = 0
    
    if (left<right):
        
        mid = (left + right)//2
        
        inv_count += mergeSort(arr, left, mid, temp_arr)
        
        inv_count += mergeSort(arr, mid+1, right, temp_arr)
        
        inv_count += merge(arr, left, right, mid, temp_arr)
    
    return inv_count
        
def merge(arr, left, right, mid, temp_arr):
    i = left
    j = mid+1
    k = left
    
    inv_count = 0
    
    while i<=mid and j<=right:
        if(arr[i]<=arr[j]):
            temp_arr[k] = arr[i]
            k+=1
            i+=1

        else:
            temp_arr[k] = arr[j]
            inv_count+= (mid-i)+1
            j+=1
            k+=1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
        
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]  
    return inv_count
    
    
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        
        temp_arr = [0]*n
        
        left = 0
        
        right = n-1
        
        return mergeSort(arr, left, right, temp_arr)