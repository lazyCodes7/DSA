def median(arr1, arr2, n1, n2):
	i = 0
	j = 0

	m = -1
	n = -1

	count = 0

	arr_len = int((n1+n2)/2)

	print(arr_len)

	while(count<arr_len+1):
		count+=1

		if(i == n1):
			n = m
			m = arr2[j]
			j+=1

		elif(j == n2):
			n = m
			m = arr1[i]
			i+=1

		elif(arr1[i]>=arr2[j]):
			n = m
			m = arr2[j]
			j+=1

		elif(arr1[i]<=arr2[j]):
			n = m
			m = arr1[i]
			i+=1

		print("n:"+str(n))
		print("m:"+str(m))

	if(n1 == n2):
		return (n+m)/2

	else:
		return m



def medianRecurse(arr1, arr2, n):
	if n == 0:
		return -1

	# 1 element in each => median of
	# sorted arr made of two arrays will   
	elif n == 1:
	# be sum of both elements by 2
		return (arr1[0]+arr2[0])/2
	elif(n == 2):
		return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1]))/2

	else:
		m1 = sum(arr1[:n])/n
		m2 = sum(arr2[:n])/n

	if m1 > m2:

		if n % 2 == 0:
			return medianRecurse(arr1[:int(n / 2) + 1],arr2[int(n / 2) - 1:], int(n / 2) + 1)
		else:
			return medianRecurse(arr1[:int(n / 2) + 1],arr2[int(n / 2):], int(n / 2) + 1)

	else:
		if n % 2 == 0:
			return medianRecurse(arr1[int(n / 2 - 1):],arr2[:int(n / 2 + 1)], int(n / 2) + 1)
		else:
			return medianRecurse(arr1[int(n / 2):],arr2[0:int(n / 2) + 1], int(n / 2) + 1)

ar1 = [1, 2, 3, 4]
ar2 = [5,6,7]
n1 = len(ar1)
n2 = len(ar2)
print("Median is ", medianRecurse(ar1, ar2, n1, n2))