class Solution:
    def solveRecursive(self, text1, text2, i, j, dp, string = ""):
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(i == 0 or j ==0):
            return ""
        elif(text1[i-1] == text2[j-1]):
            dp[i][j] = text1[i-1]+Solution.solveRecursive(self, text1, text2, i-1, j-1, dp)
        else:
            c1 = Solution.solveRecursive(self, text1, text2, i-1, j, dp, string) 
            c2 = Solution.solveRecursive(self, text1, text2, i, j-1, dp, string)
            
            if(len(c1)>len(c2)):
                dp[i][j] = c1
            else:
                dp[i][j] = c2
                
    
        return dp[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        string = self.solveRecursive(text1, text2, len(text1), len(text2), dp)
        return len(string)