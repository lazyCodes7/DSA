arr = list(map(int, input().split()))

i = 0
j = len(arr) - 1

while(i<j and j>0):
	if(arr[i]<0 and arr[j]>=0):
		i+=1
		j-=1
	elif(arr[i]>=0 and arr[j]<0):
		temp = arr[j]
		arr[j] = arr[i]
		arr[i] = temp
		i+=1
		j-=1
	elif(arr[i]>=0 and arr[j]>=0):
		j-=1
	elif(arr[i]<0 and arr[j]<0):
		i+=1
print(arr)