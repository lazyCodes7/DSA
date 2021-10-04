from Graph import WeightedGraph
import heapq
from pair import Pair
def dijkstra(graph, position):
	elements = []
	visited = {}
	paths = {}
	#print(graph.edges)
	for values in graph.values:
		visited[values] = False
		paths[values] = float('inf')

	for edges in graph.edges:
		if(visited[edges] == False):
			visited[edges] = True
			heapq.heappush(elements,edges)
			paths[edges] = 0
		while(elements!=[]):
			node = heapq.heappop(elements)
			if(type(node) != int):
				node = node[1]
			#print(node)
			for neighbors in graph.edges[node]:
				#print(visited[neighbors['edge']])
				if(visited[neighbors['edge']] == False):
					paths[neighbors['edge']] = paths[node] + neighbors['weight']
					visited[neighbors['edge']] = True
					heapq.heappush(elements, [neighbors['weight'], neighbors['edge']])

				else:
					if(paths[node] + neighbors['weight'] < paths[neighbors['edge']]):
						paths[neighbors['edge']] = paths[node] + neighbors['weight']
	#print(paths)
	return paths[position]



graph = WeightedGraph()
graph.addEdge(1, Pair(2,2))
graph.addEdge(1, Pair(4,1))
graph.addEdge(4, Pair(3,3))
graph.addEdge(2, Pair(3,4))
graph.addEdge(3, Pair(5,1))
graph.addEdge(2, Pair(5,5))
print(dijkstra(graph, 5))








