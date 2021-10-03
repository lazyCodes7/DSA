from Graph import Graph
from stack import Stack

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
			if(visited[neighbors] == False):
				visited[neighbors] = True
				dfs(stack, graph, neighbors, visited)

		stack.push(edge)

	except:
		stack.push(edge)

graph = Graph(undirected = False)
graph.addEdge(5,2)
graph.addEdge(5,0)
graph.addEdge(2,3)
graph.addEdge(3,1)
graph.addEdge(4,1)
graph.addEdge(4,0)
return_stack = toposort(graph)
while(return_stack.isEmpty() == False):
	print(return_stack.pop())