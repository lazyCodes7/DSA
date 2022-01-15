class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        k = len(b)//len(a)+3
        #print(k)
        for i in range(1, k):
            if b in (a*i):
                return i
        return -1