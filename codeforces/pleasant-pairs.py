n = int(input())
for i in range(n):
	element_count = 0
	len_arr = int(input())
	array = list(map(int, input().strip().split()))
	for k in range(0,len_arr):
		for j in range(array[k]-k-2,len_arr,array[k]):
			if((array[k]*array[j] == k+j+2) and k<j):
				element_count+=1
 
	print(element_count)