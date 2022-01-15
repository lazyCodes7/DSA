class Solution:
    def compute_longest_lp(self, needle):
        len_arr = 0 # length of the previous longest prefix suffix
        lps = [0 for i in range(len(needle))]
        lps[0] = 0 # lps[0] is always 0
        i = 1

        while i < len(needle):
            if needle[i]== needle[len_arr]:
                len_arr += 1
                lps[i] = len_arr
                i += 1
            else:
                if len_arr != 0:
                    len_arr = lps[len_arr-1]

                else:
                    lps[i] = 0
                    i += 1
        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        if(needle == ""):
            return 0
        lps_arr = self.compute_longest_lp(needle)
        #print(lps_arr)
        j = 0
        i = 0
        while(i<len(haystack)):
            #print("I: " + str(i))
            #print("J: " + str(j))
            if(haystack[i] == needle[j]):
                i+=1
                j+=1
                if(j == len(needle)):
                    return i-j
            else:
                if(j == 0):
                    i+=1

                else:
                    j = lps_arr[j-1]    
        return -1