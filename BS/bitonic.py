def maxBitonic(arr):
	start = 0
	end = len(arr)-1

	while(start<=end):
		mid = (start + end)//2

		if(mid-1<0):
			return max(arr[start], arr[end])
		if(arr[mid-1]>arr[mid]):
			end = mid-1

		elif(arr[mid-1]<arr[mid]):
			start = mid+1


	return max(arr[start], arr[end])

print(maxBitonic([1,2]))