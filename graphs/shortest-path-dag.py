from Graph import WeightedGraph
from stack import Stack
from queue import Queue
from pair import Pair
def toposort(graph):
	visited = {}
	stack = Stack()
	for val in graph.values:
		visited[val] = False

	for edge in graph.edges:
		if(visited[edge] == False):
			visited[edge] = True
			dfs(stack, graph, edge, visited)

	return stack


def dfs(stack, graph, edge, visited):
	try:
		for neighbors in graph.edges[edge]:
			if(visited[neighbors['edge']] == False):
				visited[neighbors['edge']] = True
				dfs(stack, graph, neighbors['edge'], visited)

		stack.push(edge)

	except:
		stack.push(edge)

def findShortestPath(graph, stack, position):
	visited = {}
	queue = Queue()
	positive_infinity = float('inf')
	paths = {}
	#print(graph.edges)
	for val in graph.values:
		visited[val] = False
		paths[val] = positive_infinity

	while(stack.isEmpty() == False):
		element = stack.pop()
		if(visited[element] == False):
			visited[element] = True
			paths[element] = 0
			queue.put(element)
		while(queue.empty() == False):
			node = queue.get()
			#print(node)
			try:
				for neighbors in graph.edges[node]:
					if(visited[neighbors['edge']] == False):
						#print(neighbors['edge'])
						visited[neighbors['edge']] = True
						queue.put(neighbors['edge'])
						#print("weight: "+ str(neighbors['weight']))
						paths[neighbors['edge']] = paths[node]+neighbors['weight']
						#print(neighbors['weight'])

					else:
						if(paths[node]+neighbors['weight'] < paths[neighbors['edge']]):
							paths[neighbors['edge']] = paths[node] + neighbors['weight']
			except Exception as e:
				print(e)
				pass
	print(paths)
	return paths[position]





graph = WeightedGraph(undirected = False)
graph.addEdge(0, Pair(1,2))
graph.addEdge(1, Pair(2,3))
graph.addEdge(2, Pair(3,6))
graph.addEdge(0, Pair(4,1))
graph.addEdge(4, Pair(5,4))
graph.addEdge(5, Pair(3,1))
graph.addEdge(4, Pair(2,2))
stack = toposort(graph)
print(findShortestPath(graph, stack, 2))
