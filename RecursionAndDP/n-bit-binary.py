class Solution:
    def solveRecursive(self, return_list, ans, one_cnt, zero_cnt, N):
        if((one_cnt + zero_cnt)>=N):
            return_list.append(ans)
        else:
            if(one_cnt<N):
                Solution.solveRecursive(self, return_list, ans+"1", one_cnt+1, zero_cnt, N)
            if(one_cnt>zero_cnt):
                Solution.solveRecursive(self, return_list, ans+"0", one_cnt, zero_cnt+1, N)
        return return_list
                
	def NBitBinary(self, N):
	    ans = self.solveRecursive([],"",0,0,N)
	    return ans