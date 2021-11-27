import sys
def mcm_tabulation(matrix):
	len_matrix = len(matrix)
	dp = [[0 for j in range(len_matrix)] for i in range(len_matrix)]

	for step in range(2, len_matrix):
		for i in range(1, len_matrix-step+1):
			j = i+step-1
			dp[i][j] = sys.maxsize
			for k in range(i,j):
				dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + matrix[i-1]*matrix[k]*matrix[j])

	return dp[1][len_matrix-1]

print(mcm_tabulation([10,30,5,60]))


