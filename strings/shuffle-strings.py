str1 = input()
str2 = input()
shuffle_str = input()
if(len(shuffle_str)!=len(str2)+len(str1)):
	print("Hehe stupid hoe")

else:
	str_list1 = list(shuffle_str)
	str_list1.sort()
	str_list2 = list(str1)+list(str2)
	str_list2.sort()
	if(str_list2 == str_list1):
		print("Nice try, punk")
