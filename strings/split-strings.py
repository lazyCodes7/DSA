def splitStrings(string):
	zero_count = 0
	one_count = 0 
	count = 0
	for i in range(len(string)):
		if(string[i] == "0"):
			zero_count+=1

		else:
			one_count+=1

		if(zero_count == one_count):
			count+=1

	if(count == 0):
		return -1

	return count

print(splitStrings("0101"))