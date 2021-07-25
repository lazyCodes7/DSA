def copy(array,arr_len):
	new_arr = []
	for i in range(arr_len):
		new_arr.append(array[i])
	return new_arr

n_testcases = int(input())
for i in range(n_testcases):
	arr_len = int(input())
	arr = list(map(int, input().strip().split()))
	b = copy(arr, arr_len)
	unsorted_counter = 0
	arr.sort()
	for i in range(arr_len):
		if(b[i] != arr[i]):
			unsorted_counter+=1
	if(unsorted_counter>2):
		print("YES")
	else:
		print("NO")
