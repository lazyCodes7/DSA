def mcm(arr, i, j):
	if(i>=j):
		return 0 
	minimum = float('inf')
	for k in range(i, j):
		c1 = arr[0:k+1]
		c2 = arr[k+1:]

		res1 = mcm(arr, i, k)
		res2 = mcm(arr, k+1, j)
		minimum = min((res1 + res2 + arr[i-1]*arr[k]*arr[j]), minimum)

		
	return minimum

print(mcm([40, 20, 30, 1 0, 30], 1, 4))
