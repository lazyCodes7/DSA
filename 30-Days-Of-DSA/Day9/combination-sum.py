import copy
from collections import Counter
class Solution:
    def solveRecursive(self, candidates, target, return_list = [], temp_list = [], i = 0):
        if(target == 0):
            return True
        elif(target<0 or i == len(candidates)):
            return None
        else:
            temp_list.append(candidates[i])
            res = Solution.solveRecursive(self, candidates, target-candidates[i], return_list, temp_list, i)
            if(isinstance(res, bool)):
                subset = copy.deepcopy(temp_list)
                return_list.append(subset)
            temp_list.pop()
            res = Solution.solveRecursive(self, candidates, target, return_list, temp_list, i+1)
            if(isinstance(res, bool)):
                subset = copy.deepcopy(temp_list)
                return_list.append(subset)
            
        return return_list
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = self.solveRecursive(candidates, target, return_list = [], temp_list = [],i = 0)
        #print(res)
        return res