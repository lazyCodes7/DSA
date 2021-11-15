class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum = 0
        element_sum = 0
        maxones = 0
        for i in range(len(nums)):
            sum+=1
            element_sum+=nums[i]
            if(element_sum!=sum):
                maxones = max(element_sum, maxones)
                sum=0
                element_sum=0
                
        return max(maxones, element_sum)