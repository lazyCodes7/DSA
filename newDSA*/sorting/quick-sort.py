def partition(arr, low, high):
	i = low
	j = high
	pivot = arr[i]
	pivot_index = low
	while(i<=j):
		while(i<=j and arr[i]<=pivot):
			i+=1
		while(j>=i and arr[j]>=pivot):
			j-=1
		if(i<=j):
			arr[i], arr[j] = arr[j], arr[i]

	
	arr[j], arr[pivot_index] = arr[pivot_index], arr[j]
	print("inside partition")
	print(arr)
	return j

def quicksort(arr, low, high):
	if(low<high):
		partition_index = partition(arr, low, high)
		print(partition_index)
		quicksort(arr, low, partition_index)
		quicksort(arr, partition_index+1, high)

arr = [1,4,2,3]

quicksort(arr, 0, len(arr)-1)
print(arr)
