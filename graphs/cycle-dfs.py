from Graph import Graph
def detectCycle(graph):
	visited = {}
	for edge in graph.edges:
		visited[edge] = [False,-1]
	for edge in graph.edges:
		if(visited[edge][0] == False):
			visited[edge][0] = True
			value = dfs(edge, graph.edges, visited)
			if(value):
				print(visited)
				return True


	return False


def dfs(node, edges, visited):
	for neighbor in edges[node]:
		try:
			if(visited[neighbor][0] == False):
				#print("Node:"+str(node))
				visited[neighbor] = [True, node]
				#print(visited)
				if(dfs(neighbor, edges, visited)):
					return True
				

			else:
				if(visited[neighbor][0] == True and visited[node][1]!=neighbor and visited[node][1]!=-1):
					#print(visited)
					return True

		except Exception as e:
			#print(e)
			visited[neighbor] = [True,node]
			#print(neighbor)

	return False

graph = Graph(undirected = False)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(5,4)
graph.addEdge(6,1)
graph.addEdge(8,9)
graph.addEdge(9,7)
print(detectCycle(graph))