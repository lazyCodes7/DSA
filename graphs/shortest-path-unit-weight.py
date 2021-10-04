from Graph import Graph
from queue import Queue
def findShortestPath(graph, position):
	positive_infinity = float('inf')
	queue = Queue()
	paths = {}
	visited = {}
	for values in graph.values:
		visited[values] = False
		paths[values] = positive_infinity

	#print(visited)
	#print(graph.edges)
	for edges in graph.edges:
		if(visited[edges] == False):
			visited[edges] = True
			queue.put(edges)
			paths[edges] = 0
			while(queue.empty() == False):
				node = queue.get()
				#print(node)
				for neighbors in graph.edges[node]:
					if(visited[neighbors] == False):
						visited[neighbors] = True
						paths[neighbors] = paths[node]+1
						queue.put(neighbors)

					else:
						if((paths[node]+1) < paths[neighbors]):
							paths[neighbors] = paths[node]+1

	#print(paths)
	return paths[position]

graph = Graph()
graph.addEdge(1,2)
graph.addEdge(1,4)
graph.addEdge(4,5)
graph.addEdge(2,3)
graph.addEdge(3,5)
graph.addEdge(5,6)
graph.addEdge(6,7)
print(findShortestPath(graph, 7))









