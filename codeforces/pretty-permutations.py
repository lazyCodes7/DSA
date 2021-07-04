n_cases = int(input())
for i in range(n_cases):

	n_cats = int(input())
	cat_arr = []
	for i in range(n_cats):
		cat_arr.append(i+1)
	if(n_cats%2==0):
		for i in range(0,n_cats-1,2):
			temp = cat_arr[i]
			cat_arr[i]=cat_arr[i+1]
			cat_arr[i+1] = temp


	else:
		for i in range(0,n_cats-2,2):
			temp = cat_arr[i]
			cat_arr[i]=cat_arr[i+1]
			cat_arr[i+1] = temp
		if(n_cats>0):
			temp = cat_arr[n_cats-1]
			cat_arr[n_cats-1] = cat_arr[n_cats-2] 
			cat_arr[n_cats-2] = temp

	for i in range(n_cats):
		print(cat_arr[i], end=" ")

	print("")
