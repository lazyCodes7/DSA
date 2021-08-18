def solution(string):
	string_list = list(string)
	string_len = len(string_list)

	final_sum = 0

	direction_1 = 0

	direction_2 = 0
	try:

		start_index = string_list.index(">")
		for i in range(start_index,string_len):
			if(string_list[i] == ">"):
				if(direction_2>0):
					final_sum += direction_2*direction_1*2
					direction_2 = 0
				direction_1+=1

			if(string_list[i] == "<"):
				direction_2+=1

		if(direction_2>=0):
			final_sum += direction_1*direction_2*2

		return final_sum

	except:
		return 0
print(solution("---"))
