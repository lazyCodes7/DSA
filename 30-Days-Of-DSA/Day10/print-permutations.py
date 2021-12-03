import copy
class Solution:
    def solveRecursive(self, i, nums, temp_list, return_list, visited):
        if(i == len(nums)):
            subset = copy.deepcopy(temp_list)
            return_list.append(subset)
        else:
            for j in range(len(nums)):
                #print(visited)
                if(visited[nums[j]] == False):
                    temp_list.append(nums[j])
                    visited[nums[j]] = True
                    Solution.solveRecursive(self,i+1, nums, temp_list, return_list, visited)
                    temp_list.pop()
                    visited[nums[j]] = False
        return return_list
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = {}
        for i in range(len(nums)):
            visited[nums[i]] = False
        
        res = self.solveRecursive(0,nums,[],[],visited)
        return res