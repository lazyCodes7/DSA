def minDiff(arr, key):
	start = 0
	end = len(arr)-1

	while(start<=end):
		mid = start + (end - start)//2
		#print(mid)
		#print(key-arr[mid])

		if(arr[mid] == key):
			return 0

		elif(arr[mid]<key):
			start = mid+1
			
		else:
			end = mid-1

	return min(abs(key-arr[start]), abs(key-arr[end]))


print(minDiff([1,2,3,4,5,7,10],6))