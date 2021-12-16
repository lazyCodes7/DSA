def findInfinite(arr, key):
	start = 0
	end = start+1

	while(arr[end]<key):
		start = end
		end = end*2



	while(start<=end):
		mid = start + (end - start)//2

		if(arr[mid] == key):
			return mid

		elif(arr[mid]>key):
			end = mid - 1

		else:
			start = mid+1

	return -1

print(findInfinite([1,2,3,4,5,6,7,8,9,10,11,23,24,45,67,89,90,92,98,100],25))
