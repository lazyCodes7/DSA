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
        return string
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        text1 = str1
        text2 = str2
        string = self.longestCommonSubsequence(text1, text2)
        string = string[::-1]
        final_string = ""
        i = 0
        j = 0
        k = 0
        while(i<len(text1) and j<len(text2) and k<len(string)):
            if(text1[i] == string[k] and text2[j] == string[k]):
                final_string+=string[k]
                k+=1
                i+=1
                j+=1
            else:
                if(text1[i] != string[k]):
                    print(i)
                    final_string+=text1[i]
                    i+=1
                if(text2[j] != string[k]):
                    final_string += text2[j]
                    j+=1
                    
        while(i<len(str1)):
            final_string+=text1[i]
            i+=1
        while(j<len(str2)):
            final_string+=text2[j]
            j+=1
        
        return final_string