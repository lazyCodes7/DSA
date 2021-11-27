import copy
class Solution:
    def solutionRecursive(self, nums, idx = 0, return_list = [[]], temp_list = []):
        if(idx == len(nums)):
            return
        else:
            while(idx<len(nums)):
                curr_idx = idx
                temp_list.append(nums[idx])
                subset = copy.deepcopy(temp_list)
                return_list.append(subset)
                Solution.solutionRecursive(self, nums, idx+1, return_list, temp_list)
                while(idx<len(nums) and nums[curr_idx]==nums[idx]):
                    idx+=1
                
                temp_list.pop()
        
        return return_list
                
                        
    def subsetsWithDup(self, nums):
        nums.sort()
        return self.solutionRecursive(nums)
sol = Solution()
print(sol.subsetsWithDup([0]))