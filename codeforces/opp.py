n = int(input())

for i in range(n):
	input_str = input()

	a,b,c = input_str.split()

	a, b, c= int(a), int(b), int(c)

	no_of_element = abs(a-b)*2

	diff = abs(a-b)

	if((max(a, b) or min(a, b)) > no_of_element):
		print(-1)

	else:
		if(c>no_of_element):
			print(-1)

		else:
			if(c+diff <= no_of_element):
				print(c+diff)

			else:
				print(c-diff)