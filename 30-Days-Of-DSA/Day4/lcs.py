class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = nums
        arr_dict = {}
        lcs = 0
        for i in range(len(arr)):
            try:
                arr_dict[arr[i]] += 1
                
            except:
                arr_dict[arr[i]] = 1
                
        
        for i in range(len(arr)):
            element = arr[i] - 1
            
            try:
                present = arr_dict[element]
                
            except:
                temp_lcs = 0
                element = arr[i]
                while(element in arr_dict.keys()):
                    temp_lcs+=1
                    element+=1
                    
                if(temp_lcs>lcs):
                    lcs = temp_lcs
                    
        return lcs
        