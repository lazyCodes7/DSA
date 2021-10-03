from Graph import Graph
from queue import Queue
def indegree(graph):
	indegree_map = {}
	for val in graph.values:
		indegree_map[val] = 0
	for edges in graph.edges:
		for values in graph.edges[edges]:
			indegree_map[values]+=1
			


	return indegree_map

def toposort(graph, indegree_map):
	queue = Queue()
	print(graph.edges)
	for values in indegree_map:
		if(indegree_map[values] == 0):
			queue.put(values)
	while(queue.empty() == False):
		node = queue.get()
		print(node)
		try:
			for neighbors in graph.edges[node]:
				if(indegree_map[neighbors]>0):
					indegree_map[neighbors]-=1

				if(indegree_map[neighbors]==0):
					queue.put(neighbors)

		except:
			pass




graph = Graph(undirected = False)
graph.addEdge(5,2)
graph.addEdge(5,0)
graph.addEdge(2,3)
graph.addEdge(3,1)
graph.addEdge(4,1)
graph.addEdge(4,0)
indegree_map = indegree(graph)
toposort(graph, indegree_map)