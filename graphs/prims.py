from Graph import WeightedGraph
from pair import Pair
import heapq

def prim(graph):
	key = {}
	mst = {}
	parent = {}
	count = 1
	weight_queue = []
	for edges in graph.edges:
		key[edges] = float('inf')
		mst[edges] = False
		parent[edges] = -1

	heapq.heappush(weight_queue, [0, graph.edges.keys()[0]])

	while(count<len(graph.edges)-1):
		element = heapq.heappop(weight_queue)
		node = element[1]
		mst[node] = True
		for neighbors in graph.edges[node]:
			edge, weight = neighbors['edge'], neighbors['weight']
			if(mst[edge] == False and weight<key[edge]):
				key[edge] = weight
				parent[edge] = [node, key[edge]]
				heapq.heappush(weight_queue,[weight, edge])
		count+=1

	#print(parent)

	mst_graph = WeightedGraph()
	for edges in parent.keys():
		if(type(parent[edges]) == int):
			continue


		parent_node, weight = parent[edges][0], parent[edges][1]
		mst_graph.addEdge(parent_node, Pair(edges, weight))

	return mst_graph



graph = WeightedGraph()
graph.addEdge(0, Pair(1, 2))
graph.addEdge(0, Pair(3, 6))
graph.addEdge(1, Pair(3, 8))
graph.addEdge(1, Pair(4, 5))
graph.addEdge(1, Pair(2, 3))
graph.addEdge(2, Pair(4, 7))
print(prim(graph).edges)


