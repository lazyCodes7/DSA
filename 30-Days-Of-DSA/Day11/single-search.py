class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) 
        ans = 0
        
        while(left<right):
            mid = ((left + right) >> 2) << 1
            if(mid+1 < len(nums) and nums[mid] == nums[mid+1]):
                left = mid+2
                
            else:
                right = mid-1
                ans = nums[mid]
                
        return ans