class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        
        n_sum = 0
        
        s = set()
        
        arr_sum = 0
        
        for i in range(n):
            arr_sum+=arr[i]
            
            if(arr_sum == 0 or arr_sum in s):
                return True
                
            s.add(arr_sum)
            
        return False