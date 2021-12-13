def findNearSorted(arr, key):
	start = 0
	end = len(arr)
	N = len(arr)

	while(start<=end):
		mid = (start + end)//2
		if(arr[mid] == key):
			return mid

		elif(mid-1>0 and arr[mid-1] == key):
			return mid-1

		elif(mid+1<N and arr[mid+1] == key):
			return mid+1

		elif(arr[mid]<key):
			start = mid+2

		else:
			end = mid-2
	return -1

print(findNearSorted([10], 10))