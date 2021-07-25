n_testcases = int(input())
for i in range(n_testcases):
	arr_len = int(input())
	a = list(map(int, input().strip().split()))
	b = list(map(int, input().strip().split()))
	c = []
	flag = 0
	if(sum(a) != sum(b)):
		print(-1)
	else:
		final_indexes = []
		no_operations = 0
		for j in range(arr_len):
			c.append(b[j]-a[j])
		# Checking the output after subtracting
		#print(c)
		currIndex = 0
		newIndex = 1
		counter = 1
		while(counter!=arr_len and currIndex<arr_len and newIndex<arr_len):
			if(c[currIndex] > 0 and c[newIndex]<0):
				if(c[currIndex] == -(c[newIndex])):
					for k in range(c[currIndex]):
						c[currIndex]-=1
						c[newIndex]+=1
						final_indexes.append((newIndex+1, currIndex+1))
						no_operations +=1
					currIndex+=1
					newIndex+=1
				elif(c[currIndex] < -(c[newIndex])):
					for k in range(c[currIndex]):
						c[currIndex]-=1
						c[newIndex]+=1
						final_indexes.append((newIndex+1, currIndex+1))
						no_operations +=1
					currIndex+=1
				elif(c[currIndex] > -(c[newIndex])):
					number_to_go_till = -(c[newIndex])
					for i in range(number_to_go_till):
						c[currIndex]-=1
						c[newIndex]+=1
						final_indexes.append((newIndex+1, currIndex+1))
						no_operations +=1
					newIndex+=1
				else:
					newIndex+=1
			elif(c[currIndex] < 0 and c[newIndex] > 0):
				if(c[newIndex] == -(c[currIndex])):
					for k in range(c[newIndex]):
						c[currIndex]+=1
						c[newIndex]-=1
						final_indexes.append((currIndex+1, newIndex+1))
						no_operations +=1
					currIndex+=1
					newIndex+=1
				elif(c[newIndex] < -(c[currIndex])):
					for k in range(c[newIndex]):
						c[currIndex]+=1
						c[newIndex]-=1
						final_indexes.append((currIndex+1, newIndex+1))
						no_operations +=1
					newIndex+=1
				elif(c[newIndex] > -(c[currIndex])):
					number_to_go_till = -(c[currIndex])
					for i in range(number_to_go_till):
						c[currIndex]+=1
						c[newIndex]-=1
						final_indexes.append((currIndex+1, newIndex+1))
						no_operations +=1
					currIndex+=1	
				else:
					newIndex+=1
			elif(c[currIndex] == 0):
				counter+=1
				currIndex+=1
			else:
				newIndex+=1
		if(no_operations == 0):
			print(0)
		else:
			print(no_operations)
			for i in range(len(final_indexes)):
				print(final_indexes[i][0], final_indexes[i][1])






