def solution(l, t):
	# Your code here
	array = l
	given_sum = t
	curr_element = array[0]
	curr_index = 0
	arr_len = len(array)
	array_sum = 0
	for i in range(0,arr_len):
		array_sum+=array[i]
		if(array_sum>given_sum):
			while(array_sum>given_sum and curr_index<=i and curr_index<arr_len):
				array_sum-=array[curr_index]
				curr_index+=1
		if(array_sum == given_sum):
			return [curr_index, i]
	if(given_sum == array_sum):

		return [curr_index, arr_len-1]
	
	return [-1,-1]
print(solution([1,1,7,9,9],7))