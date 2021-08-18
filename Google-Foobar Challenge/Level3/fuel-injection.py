def solution(n):
	steps = 0
	n = int(n)

	if(n==0):
		return 1
	while(n!=1):
		if(n%2 == 0):
			n = n/2
			steps+=1
		elif(n%2 == 1):
			first_outcome = (n-1)/2
			second_outcome = (n+1)/2
			if(first_outcome%2 == 0 or first_outcome == 1):
				n = n-1
				steps+=1

			elif(second_outcome%2 == 0 or second_outcome == 1):
				n = n+1
				steps+=1
			else:
				n = n-1
				steps+=1

	return steps

solution("13")
