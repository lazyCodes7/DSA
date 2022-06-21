class Solution:
    def solveRecursive(self, n, cuts, k):
        if(n==0 or k == len(cuts)):
            return 0
        else:
            if(cuts[k]<n):
                
                c1 = n + Solution.solveRecursive(self, n-cuts[k], cuts, k)
                c2 = Solution.solveRecursive(self, n, cuts, k+1)
                return max(c1, c2)
                
            else:
                return Solution.solveRecursive(self, n, cuts, k+1)
                
                
    def minCost(self, n, cuts) -> int:
        return self.solveRecursive(n, cuts, 0)

obj = Solution()
obj.minCost(4, [1,3,4,5])