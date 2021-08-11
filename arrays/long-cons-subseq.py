class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        mapped_arr = [0]*(10**5 + 1)
        
        max_seq = 0
        
        curr_seq = 0
        
        for i in range(len(arr)):
            
            mapped_arr[arr[i]] +=1
            
        for i in range(max(arr) + 1):
            if(mapped_arr[i] > 0):
                curr_seq+=1
                
            else:
                curr_seq=0
            
            if(curr_seq > max_seq):
                max_seq = curr_seq
                
        return max_seq