def convertNegPos(arr,n):
	i = 1
	j = 1
	arr.sort()
	while(arr[j]<0):
		if(j == n-1):
			break
		j+=1
	while(arr[i]<0 and j<n):
		arr[i], arr[j] = arr[j], arr[i]

		i+=2
		j+=1
	return arr

array = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(convertNegPos(array, len(array)))
