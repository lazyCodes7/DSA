import copy
def part_palindrome(string, index, return_list = [], temp_list = []):
	if(string == ""):
		subset = copy.deepcopy(temp_list)
		return_list.append(subset)
		return 0

	else:
		for i in range(len(string)):
			partition1 = string[:i+1]
			result = check_palindrome(partition1)
			if(result):
				temp_list.append(partition1)
				#part_palindrome(string[:i+1], i)
				part_palindrome(string[i+1:],i+1)
				temp_list.pop()
	return return_list
			
def check_palindrome(string):
	len_str = len(string)
	i = 0
	j = len_str - 1
	while(i<j):
		if(string[i]!=string[j]):
			return False

		i+=1
		j-=1
	return True

print(part_palindrome("aab", 0))