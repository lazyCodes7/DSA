import math
MOD = (10**9)+7
n = int(input())
for i in range(n):
	m = int(input())
	lcm = 1
	ans = 2
	prev = 0
	curr = 0
	n_values = 0
	if(m == 1):
		print(ans)
	else:
		for j in range(2,42):
			prev = m // lcm
			print("Prev: {} ".format(prev))
			lcm = int((lcm*j) // (math.gcd(lcm, j)))
			curr = m //lcm
			print("Curr: {} ".format(curr))

			n_values = (prev - curr) % MOD

			ans = (ans + (j*n_values)%MOD)%MOD
		print(ans)
	print(ans)


