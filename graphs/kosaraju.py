from Graph import Graph
from toposortdfs import toposort
from stack import Stack
def kosaraju(graph, toposort):
	visited = {}
	scc = []
	for val in graph.values:
		visited[val] = False

	for values in toposort:
		if(visited[values] == False):
			visited[values] = True
			nodes = dfs(graph, visited, [values], values)
			scc.append(nodes)
	return scc


def dfs(graph, visited, nodes, node):
	try:
		for neighbors in graph.transpose_edges[node]:
			if(visited[neighbors] == False):
				visited[neighbors] = True
				nodes.append(neighbors)
				dfs(graph, visited, nodes, neighbors)
	except:
		pass

	return nodes





graph = Graph(undirected = False, transpose = True)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,1)
graph.addEdge(2,4)
graph.addEdge(4,5)
print(graph.edges)
toposort_arr = []
stack = toposort(graph)
while(stack.isEmpty() == False):
	toposort_arr.append(stack.pop())

print(kosaraju(graph, toposort_arr))











