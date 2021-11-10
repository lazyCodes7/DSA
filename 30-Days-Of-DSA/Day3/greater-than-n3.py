import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1=0
        cnt2=0
        major1 = 0
        major2 = 0
        for i in range(len(nums)):
            if(major1 == nums[i]):
                cnt1+=1
                
            elif(major2 == nums[i]):
                cnt2+=1
                
            elif(cnt1 == 0):
                major1 = nums[i]
                cnt1+=1
                
            elif(cnt2 == 0):
                major2 = nums[i]
                cnt2+=1
                
            else:
                cnt1-=1
                cnt2-=1
        final_cnt1 = 0
        final_cnt2 = 0
        
        print(major1)
        print(major2)
        for i in range(len(nums)):
            if(nums[i] == major1):
                final_cnt1+=1
                
            elif(nums[i] == major2):
                final_cnt2+=1
                
        print(final_cnt1)
        print(final_cnt2)
        final_cnt1 = final_cnt1 > len(nums)/3.0
        final_cnt2 = final_cnt2 > len(nums)/3.0
        print(final_cnt1)
        print(final_cnt2)
        
        if(final_cnt1 and final_cnt2):
            return [major1, major2]
        else:
            if(final_cnt1):
                return [major1]
            elif(final_cnt2):
                return [major2]
            else:
                return []