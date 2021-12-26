def knows(matrix, A, B):
	return matrix[A][B]
def findCelebrity(matrix, n):
	stack = []
	for i in range(n):
		stack.append(i)


	A = stack.pop()
	B = stack.pop()

	while(len(stack)>1):
		if(knows(matrix, A, B)):
			A = stack.pop()

		else:
			B = stack.pop()


	if(len(stack) == 0):
		return -1

	else:
		C = stack.pop()

		if(knows(matrix, C, A)):
			C = A

		elif(knows(matrix, C, B)):
			C = B

	#print(C)

	for i in range(n):
		if(i!=C and (knows(matrix, C, i) or knows(matrix, i, C) == False)):
			return -1

	return C

matrix = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]

print(findCelebrity(matrix,4))
