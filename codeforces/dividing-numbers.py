from math import gcd,sqrt
def prime(n):
	i = 2
	dt = 0
	while i*i <= n:
		if n%i == 0:
			dt += 1
			n//=i
		else:
			if i==2:
				i+=1
			else:
				i+=2
 
	if n!=1:
		dt += 1
 
	return dt
n = int(input())
for i in range(n):
	a,b,k = input().split()
	a = int(a)
	b = int(b)
	k = int(k)
	if(a%b == 0 or b%a == 0 and a!=b):
		divisor = 1
	else:
		divisor = 2
	expo_a = prime(a)
	expo_b = prime(b)
	total_sum = expo_a + expo_b
	if(k>total_sum):
		print("NO")
	elif(a==b):
		if(k==0):
			print("YES")
		else:
			if(a==1):
				print("NO")
			else:
				if(k>1):
					print("YES")
				else:
					print("NO")
	elif(divisor == 1):
		if(k == 1 or k > 1):
			print("YES")
		else:
			print("NO")
	else:
		if(k>1):
			print("YES")
		else:
			print("NO")



