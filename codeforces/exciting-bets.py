n_testcases = int(input())
for i in range(n_testcases):
	a, b = input().split()
	a = int(a)
	b = int(b)
	if(a > b):
		try:
			num_diff = a-b
			mod_num = a%num_diff
			quotient = a // num_diff
			next_num = num_diff*(quotient + 1)
			next_num_diff = next_num - a
			final_ans = min(mod_num,next_num_diff)
			print("{} {}".format(a-b,final_ans))
		except:
			print("0 0")
	else:
		try:
			num_diff = b-a
			mod_num = a%num_diff
			quotient = a // num_diff
			next_num = num_diff*(quotient + 1)
			next_num_diff = next_num - a
			final_ans = min(mod_num,next_num_diff)
			print("{} {}".format(b-a, final_ans))
		except:
			print("0 0")