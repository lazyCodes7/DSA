class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        
        count = 1
        
        i = 1
        j = 0
        while(i<n and j<n):
            if(arr[i]<=dep[j]):
                count+=1
            
            else:
                j+=1
                
            i+=1
        return count