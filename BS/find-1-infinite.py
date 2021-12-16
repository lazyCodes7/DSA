def findInfinite(arr):
	start = 0
	end = start+1

	while(arr[end]!=1):
		start = end
		end = end*2

	print(start)
	print(end)
	res = 0
	while(start<=end):
		mid = start + (end - start)//2

		if(arr[mid] == 1):
			res = mid
			end = mid - 1

		elif(arr[mid] == 0):
			start = mid+1

	return res

print(findInfinite([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]))
