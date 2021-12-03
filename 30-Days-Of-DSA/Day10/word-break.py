class Solution:
    def checkword(self, word, dictionary):
        if(word in dictionary):
            return True

        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.solveRecursive(wordDict, s, {})
        

    def solveRecursive(self, dictionary, string, memo):
        if(string in memo):
            return memo[string]
        if(string == ""):
            return True

        else:
            for i in range(1,len(string)+1):
                if(self.checkword(string[:i], dictionary)):
                    memo[string[i:]] = Solution.solveRecursive(self,dictionary,string[i:],memo)
                    if(memo[string[i:]]):
                        return True
        return False