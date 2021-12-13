def findCeil(arr, key):
	start = 0
	end = len(arr)-1
	N = len(arr)
	res = 0

	while(start<=end):
		mid = (start + end)//2
		#print(mid)
		if(arr[mid] == key):
			return arr[mid]

		elif(arr[mid]<key):
			start = mid+1

		else:
			res = arr[mid]
			end = mid-1

	return res

print(findCeil([1,2,3,4,5,9], 6))
