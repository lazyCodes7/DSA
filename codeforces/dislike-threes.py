n = int(input())
for i in range(n):
	x = int(input())

	start = 1

	match_x = 1

	while(match_x!=x):
		start+=1
		if(start%3 == 0 or start%10 == 3):
			continue

		else:
			match_x+=1

	print(start)

