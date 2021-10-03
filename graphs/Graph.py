from queue import Queue
class Graph:
	def __init__(self, undirected = True):
		self.edges = {}
		self.undirected = undirected
		self.values = []

	def addEdge(self, u, v = None):
		try:
			if(self.undirected):
				if u not in self.edges.keys():
					self.edges[u] = []
				if v not in self.edges.keys():
					self.edges[v] = []
				self.edges[u].append(v)
				self.edges[v].append(u)
			else:
				if(u not in self.edges.keys()):
					self.edges[u] = []
				self.edges[u].append(v)

			self.values.append(u)
			self.values.append(v)
			return 1
		except Exception as e:
			print(repr(e))
			return 0 
	def traverse(self, option="dfs"):
		visited = {}
		for edge in self.edges:
			visited[edge] = False
		if(option == "dfs"):
			# do dfs
			for edge in self.edges:
				if(visited[edge] == False):
					print(edge)
					visited[edge] = True
					Graph.dfs(edge, self.edges, visited)
		else:
			# do bfs
			queue = Queue()
			for edge in self.edges:
				if(visited[edge] == False):
					queue.put(edge)
				while(queue.empty() == False):
					node = queue.get()
					if(visited[node] == False):
						visited[node] = True
						print(node)
					for neighbor in self.edges[node]:
						try:
							if(visited[neighbor] == False):
								visited[neighbor] = True
								print(neighbor)
								queue.put(neighbor)
						except:
							visited[neighbor] = True
							print(neighbor)
	@staticmethod
	def dfs(node, edges, visited):
		for neighbor in edges[node]:
			try:
				if(visited[neighbor] == False):
					visited[neighbor] = True
					print(neighbor)
					Graph.dfs(neighbor, edges, visited)

			except:
				visited[neighbor] = True
				print(neighbor)










