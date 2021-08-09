class Solution:
    def getPairsCount(self, arr, n, k):
        m = [0]*(10**6)
        final_count = 0
        
        for i in range(n):
            m[arr[i]] +=1
            
        for i in range(n):
            try:
                final_count += m[k-arr[i]]
            except:
                final_count = final_count
            
            if(k-arr[i] == arr[i]):
                final_count-=1
        return int(final_count/2)