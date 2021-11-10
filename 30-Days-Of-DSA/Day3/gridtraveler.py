class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solvePath(m,n)
        
        
    def solvePath(self, m, n, memo = {}):
        key = str(m) + "," + str(n)
        if(key in memo.keys()):
            return memo[key]
        if(m == 0 or n == 0):
            return 0
        
        elif(m==1 and n==1):
            return 1
        
        else:
            ans = Solution.solvePath(self,m-1,n,memo) + Solution.solvePath(self,m,n-1,memo)
            memo[key] = ans    
        return memo[key]