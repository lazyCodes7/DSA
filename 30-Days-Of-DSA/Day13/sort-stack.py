def sortStack(stack):
	if(stack == []):
		return 

	else:
		element = stack.pop()
		sortStack(stack)
		stack = insertSortedStack(stack,element)

	return stack

def insertSortedStack(stack, element):
	if(stack == [] or element>=stack[-1]):
		stack.append(element)

	else:
		removed = stack.pop()
		insertSortedStack(stack,element)
		stack.append(removed)

	return stack

print(sortStack([1,4,2,3,6,5]))