import sys
import bisect
def upper_bound(arr, element, start, end):
	while(start<end):
		mid = int((start + end)/2)
		if(arr[mid] > element):
			end = mid-1

		elif(arr[mid] == element):
			return mid+1

		else:
			start = mid+1
	return start
def median(matrix):
	min = sys.maxsize
	max = 0
	len_col = len(matrix[1])-1

	for i in range(len(matrix)):
		if(matrix[i][0]<min):
			min = matrix[i][0]

		if(matrix[i][len_col]>max):
			max = matrix[i][len_col]


	count = (len(matrix)*(len_col+1) + 1)/2
	print(count)

	while(min<max):
		mid = min + int(max+min)/2
		place = 0
		for i in range(len(matrix)):
			place+=upper_bound(matrix[i], mid, 0, len_col)

		print(place)

		if(place<count):
			min = mid+1

		else:
			max=mid-1

	return min
print(median([[1,3,5],[2,6,9],[3,6,9]]))


