class Stack:
	def __init__(self):
		self.stack = []


	def push(self, element):
		self.stack.append(element)

	def pop(self):
		return self.stack.pop()

	def getFront(self):
		return self.stack[-1]


	def isEmpty(self):
		if(stack == []):
			return True

		return False

stack = Stack()
stack.push(5)
stack.push(7)
stack.push(8)
stack.push(9)



print(stack.stack)
print(stack.pop())
print(stack.stack)
