class Stack:
	def __init__(self):
		self.stack = []

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		if(self.stack!=[]):
			element = self.stack.pop()
			return element

		return "Stack empty"

	def isEmpty(self):
		if(self.stack!=[]):
			return False

		return True

	def getTop(self):
		return self.stack[-1]




