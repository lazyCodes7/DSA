def arrayReverse(array,n):
	array_iter = int((len(array)-1)/2)
	array_temp = None
	for i in range(array_iter):
		array_temp = array[i]
		array[i] = array[n-i-1]
		array[n-i-1] = array_temp
	return array
array = list(map(int, input().strip().split()))
n = len(array)
print(arrayReverse(array,n))

