array = list(map(int, input().strip().split()))
n = len(array)

print(findMaxMin(n,array))




#Compare in Pairs (No of comparisons are less as compared to linear method.)
def findMaxMin(n, array):
	if(n%2==1):
		minElement = array[0]
		maxElement = array[1]
	else:
		if(array[0] == min(array[0],array[1])):
			minElement = array[0]
			maxElement = array[1]
		else:
			minElement = array[1]
			maxElement = array[0]
	if(n>1):
		for i in range(2,n-1):
			maxElement = max(maxElement,array[i+1])
			minElement = min(minElement,array[i])
	return(maxElement, minElement)