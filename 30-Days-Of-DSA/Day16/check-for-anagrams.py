class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for i in range(len(s)):
            try:
                s_map[s[i]]+=1
            except:
                s_map[s[i]]=1
        for i in range(len(t)):
            try:
                if(s_map[t[i]]>0):
                    s_map[t[i]]-=1
                else:
                    return False
            except:
                return False
        for key in s_map.keys():
            if(s_map[key]!=0):
                return False
        return True