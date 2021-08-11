class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
	    
	    maxValue = arr[0]
	    minValue = arr[0]
	    maxProd = arr[0]
	    
	    for i in range(1,n):
	        
	        if(arr[i]<0):
	            maxValue, minValue = minValue, maxValue
	            
	        maxValue = max(arr[i], maxValue*arr[i])
	        
	        minValue = min(arr[i], minValue*arr[i])
	        
	        maxProd = max(maxProd, maxValue)
	        
	        

	    return maxProd