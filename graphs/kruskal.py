from DisjointSet import DisjointSet
from Graph import WeightedGraph
from pair import Pair
example_graph = [
	[1, 1, 4],
	[2, 1, 2],
	[3, 2, 3],
	[3, 2, 4],
	[4, 1, 5],
	[5, 3, 4],
	[7, 2, 6],
	[8, 3, 6],
	[9, 4, 5]
]
example_graph.sort()
dset = DisjointSet()
graph = WeightedGraph()
for edge in example_graph:
	weight, a, b = edge[0], edge[1], edge[2]
	try:
		if(dset.findParent(a)!=dset.findParent(b)):
			graph.addEdge(a, Pair(b, weight))
			dset.union(a,b)
	except:
		graph.addEdge(a, Pair(b, weight))
		dset.union(a,b)

print(graph.edges)


