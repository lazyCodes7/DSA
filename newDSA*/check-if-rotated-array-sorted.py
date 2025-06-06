class Solution:
    def check(self, nums: List[int]) -> bool:
        min_index = 0
        for i in range(len(nums)):
            if(nums[min_index]>nums[i]):
                min_index = i
        
        incursions = 0

        prevIndex = (min_index)%len(nums)
        currIndex = (min_index + 1)%len(nums)
        flag = True
        while(prevIndex!=min_index or flag):
            if(prevIndex == min_index):
                flag = False
            if(nums[currIndex]<nums[prevIndex]):
                incursions += 1
            prevIndex = (prevIndex+1)%len(nums)
            currIndex = (currIndex+1)%len(nums)
        if(incursions>1):
            return False
        return True
                



        