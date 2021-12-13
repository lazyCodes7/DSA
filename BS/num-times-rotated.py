def countRotations(arr):
	start = 0
	end = len(arr)
	N = len(arr)
	if(arr[start]<arr[end-1]):
		return 0

	else:
		while(start<=end):
			mid = (start + end)//2

			prev = (mid+N-1)%N
			nex = (mid+1)%N

			if(arr[mid]<=arr[prev] and arr[mid]<=arr[nex]):
				return mid

			elif(arr[mid]>=arr[start]):
				start = mid+1

			else:
				end = mid-1

print(countRotations([11,1,2,3,4]))
