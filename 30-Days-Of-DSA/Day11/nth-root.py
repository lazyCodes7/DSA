def nroot(high, low, power, number):
	if(high-low<1e-4):
		return high

	else:
		mid = (high+low)/2
		num = pow(mid, power)

		if(num == number):
			return mid

		elif(num>number):
			return nroot(mid, low, power, number)

		else:
			return nroot(high, mid, power, number)

print(nroot(16, 1, 2, 16))



