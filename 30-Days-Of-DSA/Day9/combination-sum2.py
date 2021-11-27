import copy
class Solution:
    def solveRecursive(self, target, candidates, return_list = [], temp_list = [], i = 0):
        if(target == 0):
            return True
        elif(target<0 or i == len(candidates)):
            return None
        else:
            while(i<len(candidates)):
                curr_element = candidates[i]
                temp_list.append(candidates[i])
                res = Solution.solveRecursive(self, target-candidates[i],candidates,return_list,temp_list,i+1)
                if(isinstance(res, bool)):
                    subset = copy.deepcopy(temp_list)
                    return_list.append(subset)
                while(i<len(candidates) and curr_element == candidates[i]):
                    i+=1
                temp_list.pop()
                
        return return_list
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.solveRecursive(target, candidates, return_list = [], temp_list = [], i = 0)