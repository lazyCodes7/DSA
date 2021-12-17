def isValidPlacing(stalls, cows, distance):
	cord = stalls[0]
	count = 1
	for i in range(1, len(stalls)):
		if((stalls[i]-cord)>=distance):
			cord = stalls[i]
			count+=1
		if(count == cows):
			return True

	
	return False


def placeCows(stalls, cows):
	stalls.sort()
	start = stalls[0]
	end = stalls[len(stalls)-1]-stalls[0]
	res = 0
	while(start<=end):
		distance = (start + end)//2

		if(isValidPlacing(stalls, cows, distance)):
			res = distance
			start = distance+1

		else:
			end = distance-1

	return res

stalls = [1,2,4,6,8,9]
cows = 3
print(placeCows(stalls, cows))