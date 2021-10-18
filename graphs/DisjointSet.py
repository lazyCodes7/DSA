class DisjointSet:
	def __init__(self):
		self.nodes = {}
		self.indegree = {}

	def union(self, a, b):
		if a not in self.nodes.keys():
			self.nodes[a] = [0, a]

		if b not in self.nodes.keys():
			self.nodes[b] = [0, b]


		parent_a = self.nodes[a][1]
		parent_b = self.nodes[b][1]

		rank_parent1 = self.nodes[parent_a][0]
		rank_parent2 = self.nodes[parent_b][0]

		if(rank_parent1>rank_parent2):
			self.nodes[b][1] = parent_a

		elif(rank_parent1<rank_parent2):
			self.nodes[a][1] = parent_b

		else:
			if(parent_b>parent_a):
				self.nodes[parent_a][0]+=1
				self.nodes[parent_b][1] = parent_a

			else:
				self.nodes[parent_b][0]+=1
				self.nodes[parent_a][1] = parent_b

	def findIndegree(self):
		for node in self.nodes:
			if(self.nodes[node][1]!=node):
				try:
					self.indegree[self.nodes[node][1]]+=1
				except:
					self.indegree[self.nodes[node][1]]=1
	def pathCompression(self):
		self.findIndegree()
		for node in self.nodes:
			currParent = self.nodes[node][1]
			parent = self.findParent(node)
			if(parent!=currParent):
				self.indegree[currParent]-=1
				if(self.indegree[currParent] == 0):
					self.nodes[parent][0] -= 1
				self.nodes[node][1] = parent
		return self.nodes

	def findParent(self, element):
		if(self.nodes[element][1] == element):
			return element

		return self.findParent(self.nodes[element][1])

## Example
'''
dset = DisjointSet()
dset.union(1,2)
dset.union(2,3)
dset.union(3,4)
dset.union(6,7)
dset.union(7,8)
dset.union(3,7)
print(dset.nodes)
print(dset.findParent(1))
print(dset.pathCompression())
'''