class Solution:
    def k_symbol(self, n, k):
        if(n == 1 and k == 1):
            return 0
        else:
            mid = (2**(n-1))/2
            if(k<=mid):
                return Solution.k_symbol(self, n-1, k)
            else:
                res = Solution.k_symbol(self, n-1, k-mid)
                if(res == 0):
                    return 1
                else:
                    return 0
    def kthGrammar(self, n: int, k: int) -> int:
        res = self.k_symbol(n, k)
        return res