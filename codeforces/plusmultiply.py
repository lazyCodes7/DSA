n = int(input())
for i in range(n):
	m,a,b = input().split()
	m = int(m)
	a = int(a)
	b = int(b)
	flag = 0
	t = 1

	while(t<=m):
		if((m-t)%b == 0):
			flag = 1
			break
		if(a == 1):
			break
		t = t*a
	if(flag == 1):
		print("YES")
	else:
		print("NO")


