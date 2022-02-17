import copy
class Solution:
	# @param A : integer
	# @return a list of strings
	def solveRecursive(self, return_list, temp_list, open_cnt, close_cnt, n, curr_open_cnt):
		if(open_cnt == n and close_cnt == n):
			subset = copy.deepcopy(temp_list)
			return_list.append("".join(temp_list))
		else:
			if(open_cnt<n):
				temp_list.append("(")
				Solution.solveRecursive(self, return_list, temp_list, open_cnt+1, close_cnt, n, curr_open_cnt+1)
				temp_list.pop()
			if(curr_open_cnt != 0 and close_cnt<n):
				temp_list.append(")")
				Solution.solveRecursive(self, return_list, temp_list, open_cnt, close_cnt+1, n, curr_open_cnt-1)
				temp_list.pop()
		return return_list
	def generateParenthesis(self, A):
		ans = self.solveRecursive([],[],0,0,A,0)
		return ans