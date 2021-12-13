def findNextAlpha(arr, key):
	start = 0
	end = len(arr)-1
	N = len(arr)
	res = -1

	while(start<=end):
		mid = (start + end)//2
		#print(mid)
		if(arr[mid]==key):
			start = mid+1

		elif(ord(arr[mid])<ord(key)):
			start = mid+1

		else:
			res = arr[mid]
			end = mid-1

	return res

print(findNextAlpha(["a","b","c","e","f","g"], "g"))