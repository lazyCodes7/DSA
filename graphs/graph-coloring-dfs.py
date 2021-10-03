from Graph import Graph

def color(graph):
	visited = {}
	for edge in graph.edges:
		visited[edge] = [False, "No color"]

	for edge in graph.edges:
		if(visited[edge][0] == False):
			visited[edge] = [True, "Blue"]
			val = dfs(edge, graph, visited)

	return val if val == False else visited

def dfs(node, graph, visited):
	for neighbors in graph.edges[node]:
		if(visited[neighbors][0] == False):
			if(visited[node][1] == "Blue"):
				visited[neighbors] = [True, "Green"]

			else:
				visited[neighbors] = [True, "Blue"]

			value = dfs(neighbors, graph, visited)
			if(value == False):
				return False

		else:
			if(visited[neighbors][1] == visited[node][1]):
				print("Oops the graph is not bipartite. Go do something!")
				return False

graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,4)
graph.addEdge(1,3)
graph.addEdge(3,5)
graph.addEdge(4,6)
graph.addEdge(5,6)
#graph.addEdge(5,6)
print(color(graph))