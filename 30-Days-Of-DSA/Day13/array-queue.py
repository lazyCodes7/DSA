class Queue:
	def __init__(self, limit = 5):
		self.queue = []
		self.idx = 0
		self.limit = limit


	def __len__(self):
		return len(self.queue)


	def enqueue(self, element):
		if(self.isFull() == False):
			self.queue.append(element)
			return element

		return -1

	def dequeue(self):
		if(self.isEmpty() == False):
			temp = self.queue[self.idx]
			self.queue[self.idx] = None
			self.idx+=1
			return temp

		return -1

	def isEmpty(self):
		if(self.queue == []):
			return True

		return False

	def isFull(self):
		if(len(self.queue) == self.limit):
			return True

		return False

queue = Queue(limit = 5)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
print(queue.queue)
queue.dequeue()
print(queue.queue)

