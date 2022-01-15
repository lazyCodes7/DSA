import numpy as np
class Solution:
    def __init__(self):
        self.result_str = ""
    def check(self, start, end, s, dp):
        #print("Palindrome: {}".format(string))
        if(s[start] == s[end]):
            if((start+1<len(s) and end-1>=0 and dp[start+1][end-1] == 1) or end-start <= 1):
                return True
            else:
                return False
        else:
            return False
    def solveRecursive(self, s, i, dp):
        
        if(i == len(s)):
            return self.result_str
        else:
            #print("Initial string: {}".format(s))
            for j in range(i,len(s)):
                string = s[i:j+1]
                #print("Result before: {}".format(self.result_str))
                #print("Partitioned string : {}".format(string))
                if(dp[i][j] == -1):
                    if(self.check(i,j,s,dp)):
                        dp[i][j]=1
                        #dp[j][i]=1
                        if(len(string)>len(self.result_str)):
                            self.result_str = string
                            #print("Result: {}".format(self.result_str))
                        Solution.solveRecursive(self, s, j+1, dp)
                    else:
                        dp[i][j]=0
                        #dp[j][i]=0


        #print("Result outside: {}".format(result_str))
        return self.result_str
            
                    
                    
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1] * (len(s)+1) for _ in range(len(s)+1)]
        return_str = self.solveRecursive(s,0,dp)
        return return_str
sol = Solution()
print((sol.longestPalindrome("aacabdkacaa")))