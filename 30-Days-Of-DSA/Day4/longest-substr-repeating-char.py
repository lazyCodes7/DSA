class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        visited = {}
        count = 0
        
        for i in range(len(s)):
            visited[s[i]] = -1
            
        l = 0
        r = 0
        
        while(r<len(s)):
            if(visited[s[r]] == -1):
                visited[s[r]] = r
                count = r-l+1
                maxCount = max(count, maxCount)
                
            elif(visited[s[r]]>=0):
                if(l>visited[s[r]]):
                    visited[s[r]] = r
                    count = r-l+1        
                    maxCount = max(count, maxCount)
                
                    
                else:
                    l=visited[s[r]]+1
                    visited[s[r]] = r
                    count = r-l+1        
                    maxCount = max(count, maxCount)
            r+=1
        return maxCount