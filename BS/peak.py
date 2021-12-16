def findPeak(arr):
	start = 0
	end = len(arr)-1

	while(start<=end):
		mid = (start + end)//2
		if(mid == 0 and arr[mid+1]<arr[mid]):
			return mid

		elif(mid == len(arr)-1 and arr[mid-1]<arr[mid]):
			return mid

		elif(arr[mid+1]<arr[mid] and arr[mid-1]<arr[mid]):
			return mid

		elif(arr[mid+1]>arr[mid]):
			start = mid+1

		elif(arr[mid-1]>arr[mid]):
			end = mid-1

	return -1

print(findPeak([1,2,3,4,1]))
