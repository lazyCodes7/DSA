class Pair:
	def __init__(self, value1, value2):
		self.pair = {"edge": value1, "weight": value2}

	def getEdge(self):
		self.pair["edge"]

	def getWeight(self):
		self.pair["weight"]

