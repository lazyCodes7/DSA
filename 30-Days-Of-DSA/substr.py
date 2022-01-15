class Solution:
    def findNeedle(self, haystack, needle):
        if(needle == ""):
            return 0
        
        else:
            i = 0
            j = 0
            start_idx = -1
            
            while(j<len(haystack)):
                if(haystack[j] == needle[i]):
                    if(start_idx == -1):
                        start_idx = j
                    i+=1
                    if(i == len(needle)):
                        return start_idx
                
                else:
                    i = 0
                    start_idx = -1
                j+=1
                
            
            return -1
                    
    def strStr(self, haystack: str, needle: str) -> int:
        pos1 = self.findNeedle(haystack, needle)
        print(haystack[::-1])
        print(needle[::-1])
        pos2 = self.findNeedle(haystack[::-1], needle[::-1])
        print(pos2)
        if(pos2!=-1):
            pos2 = len(haystack) - pos2 - len(needle)
        
        if(min(pos1, pos2)!=-1):
            return min(pos1, pos2)
        else:
            return max(pos1, pos2)
sol = Solution()

print(sol.strStr("mississippi", "issip"))