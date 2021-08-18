def returnMinJumps(arr, n):
	j = 0
	jump = 0


	while(j<n-2):
		if(arr[j] == 0):
			if(j+2 >= n-1):
				jump+=1
				return jump
			if(arr[j+2] == 0):
				j = j+2
				jump+=1

			elif(arr[j+1] == 0):
				j = j+1
				jump+=1
			else:
				return 0

	


print(returnMinJumps([0,0,0,0,1,0], 6))









