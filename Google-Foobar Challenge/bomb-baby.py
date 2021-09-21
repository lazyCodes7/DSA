def solution(x,y):
	x, y = int(x), int(y)
	steps = 0

	if(x==1 and y==1):
		return str(0)

	while((x>0 and y>0) and (x!=y)):
		if(x>y):
			steps += int(x/y)
			x = x%y

		else:
			steps+= int(y/x)
			y = y%x
			


		if(x==1 or y==1):
			if(x==1):
				steps += int(y/x)-1

			else:
				steps += int(x/y)-1
			return str(steps)

	return "impossible"

print(solution(4,2))

