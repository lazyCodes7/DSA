class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def mergeSort(self, arr, left, right):
    	inversions = 0
    	mid = int((left+right)/2)
    
    	if(left<right):
    		inversions += Solution.mergeSort(self, arr, left, mid)
    		inversions += Solution.mergeSort(self, arr, mid+1, right)
    		inversions += Solution.merge(self, arr, left, mid, right)
    
    	return inversions

    def merge(self, arr, left, mid, right):
    	arr1 = arr[left:mid+1]
    	arr2 = arr[mid+1:right+1]
    	temp = []
    	inversions = 0
    	len_arr1 = (mid-left)+1
    	len_arr2 = right-mid
    	i = 0
    	j = 0
    	k = 0
    
    	while(i<len_arr1 and j<len_arr2):
    		if(arr1[i]>arr2[j]):
    			temp.append(arr2[j])
    			j+=1
    			inversions+=(len_arr1-i)
    
    		elif(arr1[i]<=arr2[j]):
    			temp.append(arr1[i])
    			i+=1
    	while(i<len_arr1):
    		temp.append(arr1[i])
    		i+=1
    
    	while(j<len_arr2):
    		temp.append(arr2[j])
    		j+=1
    
    	arr[left:right+1] = temp
    
    	return inversions
    def inversionCount(self, arr, n):
        return self.mergeSort(arr, 0, n-1)

arr = [4,2,3,5,1]
sol = Solution()
print(sol.inversionCount(arr, len(arr)))


