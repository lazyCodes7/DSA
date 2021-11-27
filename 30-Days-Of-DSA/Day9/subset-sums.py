#User function Template for python3
class Solution:
    def solveSums(self, arr, N, sum_arr = [], sum = 0, i = 0):
        if(i == N):
            sum_arr.append(sum)
            
        else:
            Solution.solveSums(self, arr, N, sum_arr, sum, i+1)
            Solution.solveSums(self, arr, N, sum_arr, sum+arr[i], i+1)
        return sum_arr
            
	def subsetSums(self, arr, N):
	    return self.solveSums(arr, N, [])