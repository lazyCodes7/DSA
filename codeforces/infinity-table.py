n = int(input())
for i in range(n):
	k = int(input())
	required_num = 1

	j = 0

	leftmost = 1

	top_leftmost = 1

	temp_leftmost = 1

	allowed_leftmost = 1

	if(k == 1):
		print("1, 1")
	
	else:
		for required_num in range(2,k+1):
			if(allowed_leftmost>0):
				allowed_leftmost-=1
				if(required_num == k):
					print("{}, {}".format(j+1, leftmost+1))
					break
				j+=1

			elif(allowed_leftmost == 0 and leftmost >= 0):
					if(required_num == k):
						print("{}, {}".format(j+1, leftmost+1))
						break
					leftmost-=1

			if(leftmost == -1):
				top_leftmost +=1
				leftmost = top_leftmost
				temp_leftmost += 1
				allowed_leftmost = temp_leftmost
				j = 0






	
