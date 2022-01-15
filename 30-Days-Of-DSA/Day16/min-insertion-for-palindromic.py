class Solution:
    # @param A : string
    # @return an integer

    def lps_solver(self, string):
        lps = [0 for i in range(len(string))]
        lps[0] = 0
        i = 1
        len_str = 0

        while(i<len(string)):
            if(string[i] == string[len_str]):
                len_str+=1
                lps[i] = len_str
                i+=1
            else:
                if(len_str == 0):
                    lps[i] = 0
                    i+=1
                else:
                    len_str = lps[len_str-1]
        return lps
    def checkPal(self, string):
        return string[::-1] == string
    def solve(self, A):
        j = len(A)

        string = A + "$" + A[::-1]
        
        lps = self.lps_solver(string)
        #print(lps)
        

        return len(A)-lps[-1]