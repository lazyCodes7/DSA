def solveRecursive(S1, S2, memo):
	key = S1 + "," + S2
	if(key in memo.keys()):
		return memo[key]
	if(S1 == "" and S2 == ""):
		return ""
	else:
		c1 = ""
		c2 = ""
		if(len(S1)!=0):
			c1 += solveRecursive(S1[1:], S2 + S1[0], memo)

		if(len(S2)!=0):
			c2 = S2[-1]+solveRecursive(S1, S2[0:len(S2)-1], memo)

		if(c1 == ""):
			memo[key] = c2
			return memo[key]

		if(c2 == ""):
			memo[key] = c1
			return memo[key]

		memo[key] = min(c1, c2)
		return memo[key]

print("Enter input: ")
string = input()
print(solveRecursive(string, "", {}))




