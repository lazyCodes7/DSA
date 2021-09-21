def mergePalindrome(arr, n):
	n_of_merge = 0

	middle_index = int(n/2)

	i = 0

	j = n-1

	merge_counts = 0
	while(i<=j):
		if arr[i] == arr[j]:
			i += 1
			j -= 1

		elif(arr[i]>arr[j]):

			arr[j-1] = arr[j-1]+arr[j]
			merge_counts+=1
			j-=1

		elif(arr[i]<arr[j]):
			arr[i+1] = arr[i+1]+arr[i]
			merge_counts+=1
			i+=1

	print(merge_counts)

arr = [1, 4, 5, 9, 1]
n = len(arr)
mergePalindrome(arr, n)



