class Solution:
    def solveRecursive(self, nums, target, n, dp):
        if(dp[target][n]!=-1):
            return dp[target][n]
        if(target == 0):
            return True
        if(n == len(nums)):
            return False
        else:
            if(nums[n]<=target):
                c_1 = Solution.solveRecursive(self, nums, target - nums[n], n+1, dp)
                c_2 = Solution.solveRecursive(self, nums, target, n+1, dp)
                dp[target][n] = c_1 or c_2
            else:
                dp[target][n] = Solution.solveRecursive(self, nums, target, n+1, dp)
                

            return dp[target][n]
        
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2 == 1):
            return False
        else:
            target = int(sum(nums)/2)
            dp = [[-1 for i in range(len(nums)+1)] for j in range(target+1)]
            return self.solveRecursive(nums, target, 0, dp)
        