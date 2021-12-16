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


	if(arr[start]>arr[end]):
		return start
	else:
		return end

def search(arr, key):
	start = 0
	end = len(arr)-1

	while(start<=end):
		mid = (start + end)//2
		if(arr[mid] == key):
			return mid
		elif(arr[mid]>key):
			end = mid-1
		else:
			start = mid+1
	return -1
arr = [1,2,3,4,1,2]
pivot = maxBitonic(arr)
arr1 = arr[:pivot+1]
arr2 = arr[pivot+1:]
ele1 = search(arr1, 4)
ele2 = search(arr2, 4)
print(ele1)
print(ele2)



