def findCelebrity(M, n):
	i = 0
	j = n-1

	while(i<j):
		if(M[i][j] == 1):
			i+=1

		else:
			j-=1

	candidate = i


	for i in range(n):
		if(candidate!=i and (M[i][candidate]!=1 or M[candidate][i] == 1)):
			return -1

	return candidate

matrix = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
print(findCelebrity(matrix,4))
