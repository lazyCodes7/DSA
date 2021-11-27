import sys
def mcm(i, j, matrix, dp):
	if(i == j):
		return 0

	elif(dp[i][j]!=-1):
		return dp[i][j]

	else:
		dp[i][j] = sys.maxsize
		curr_min = sys.maxsize
		k = i
		while(k<j and k<len(matrix)):
			min_val = mcm(i, k, matrix, dp) + mcm(k+1, j, matrix, dp) + matrix[i-1]*matrix[k]*matrix[j]
			dp[i][j] = min(dp[i][j], min_val)
			k+=1

	return dp[i][j]

dp = [[-1 for i in range(5)] for i in range(5)]
matrix = [40,20,30,10,30]
print(mcm(1,len(matrix)-1,matrix,dp))