class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        if(len(strs) == 0):
            return ""
        elif(len(strs) == 1):
            return strs[0]
        else:
            string = strs[0]
            for j in range(0, len(string)):
                for i in range(1, len(strs)):
                    if(j>=len(strs[i]) or strs[i][j] != string[j]):
                        return strs[0][0:k]
                k = j+1

        return strs[0][0:k]