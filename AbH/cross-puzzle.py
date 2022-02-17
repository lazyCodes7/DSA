def checkHorizontalDirection(puzzle, words, word_map, i, j):
	print(word_map)
	word_len = 0
	while(puzzle[i][j]!="+" and j>0):
		j-=1

	if(puzzle[i][j] == "+"):
		j+=1

	temp_j = j
	print(temp_j)
	while(puzzle[i][temp_j] != "+" and temp_j<len(puzzle)):
		temp_j+=1
		word_len+=1

	print(word_len)
	for word in words:
		temp_j = j
		k = 0
		if(len(word)!=word_len):
			continue
		if(puzzle[i][temp_j]!="-"):
			while(temp_j<len(puzzle) and puzzle[i][temp_j] == word[k]):
				temp_j+=1
				k+=1
			if(temp_j == j):
				continue

		puzzle[i][temp_j:temp_j + (word_len - k)] = word[k:]
		word_map[word] = False
		return puzzle, word_map, word, k

	return puzzle, word_map, None, 0
	
def checkVerticalDirection(puzzle, words, word_map, i, j):
	print("Vert")
	print(word_map)
	word_len = 0
	while(puzzle[i][j]!="+" and i>0):
		i-=1

	if(puzzle[i][j] == "+"):
		i+=1



	temp_i = i
	print(temp_i)
	while(puzzle[temp_i][j] != "+" and temp_i<len(puzzle)):

		temp_i+=1
		word_len+=1


	print(word_len)

	for word in words:
		temp_i = i
		k = 0
		if(len(word)!=word_len or word_map[word] == False):
			continue
		if(puzzle[temp_i][j]!="-"):
			while(temp_i<len(puzzle) and puzzle[temp_i][j] == word[k]):
				temp_i+=1
				k+=1
			if(temp_i == i):
				continue

		for z in range(temp_i, temp_i+word_len-k):
			puzzle[z][j] = word[k]
			k+=1
		word_map[word] = False
		return puzzle, word_map, word, k

	return puzzle, word_map, None, 0

def solvePuzzle(puzzle, words, word_map, i, j):
	print(i,j)
	if(sum(word_map.values()) == 0):
		return True

	if(i >= len(puzzle)):
		return False

	else:
		if(j >= len(puzzle)):
			j = 0
			i+=1

		if(puzzle[i][j] == "-"):
			puzzle, word_map, word, start = checkHorizontalDirection(puzzle, words, word_map, i, j)
			if(word!=None):
				j+=len(word)
				is_possible = solvePuzzle(puzzle, words, word_map, i, j)
				if(is_possible):
					return puzzle
				else:
					puzzle[i][j:j+len(word)-start] = "-"
					word_map[word] = True
			else:
				puzzle, word_map, word, start = checkVerticalDirection(puzzle, words, word_map, i, j)
				if(word!=None):
					j+=1
					is_possible = solvePuzzle(puzzle, words, word_map, i, j)
					if(is_possible):
						return puzzle
					else:
						k = start
						word_map[word] = True
						for z in range(i, i+len(word)-start):
							puzzle[z][j] = word[k]
							k+=1
		else:
			j+=1
			solvePuzzle(puzzle, words, word_map, i, j)
		return puzzle


crossword = [
	["+","+","+","+","+","+","+","+","+","+"],
	["+","-","-","-","-","-","-","+","+","+"],
	["+","+","+","-","+","+","+","-","+","+"],
	["+","+","+","-","+","+","+","-","+","+"],
	["+","+","+","-","-","-","-","-","+","+"],
	["+","+","+","-","+","+","+","-","+","+"],
	["+","+","+","+","+","+","+","-","+","+"],
	["+","+","+","+","+","+","+","+","+","+"],
	["+","+","+","+","+","+","+","+","+","+"],
	["+","+","+","+","+","+","+","+","+","+"]
]
words = ["POLAND", "LHASA", "SPAIN", "INDIA"]

word_map = {word:True for word in words}
i,j = 0,0
print(solvePuzzle(crossword,words,word_map,i,j))




