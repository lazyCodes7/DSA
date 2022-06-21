class Solution:
    def solveRecursive(self, amount, coins, k, dp):
        if(dp[k][amount]!=-1):
            return dp[k][amount]
        if(amount == 0):
            return 0
        if(k == len(coins)):
            return float('inf')
        else:
            if(coins[k]<=amount):
                c1 = 1+Solution.solveRecursive(self, amount-coins[k], coins, k, dp)
                c2 = Solution.solveRecursive(self,amount, coins, k+1, dp)
                dp[k][amount] = min(c1, c2)
                return dp[k][amount]
                
            else:
                dp[k][amount] = Solution.solveRecursive(self, amount, coins, k+1, dp)
                return dp[k][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins)+1)]
        
        ans = self.solveRecursive(amount, coins, 0, dp)
        if(ans == float('inf')):
            return -1
        return ans