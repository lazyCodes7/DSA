def find2d(arr, key):
	i = 0
	j = len(arr)-1

	while(i>=0 and j>=0):
		if(key == arr[i][j]):
			return (i,j)
		elif(key>arr[i][j]):
			i+=1

		elif(key<arr[i][j]):
			j-=1

	return -1


arr = [
	[1,2,2],
	[2,3,4],
	[3,4,5]
]

print(find2d(arr, 3))