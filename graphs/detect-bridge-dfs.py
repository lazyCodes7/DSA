from Graph import Graph
def detectBridge(graph):
	time_visited = {}
	least_time = {}
	visited = {}

	time_count = 1

	print(graph.edges)
	for edges in graph.edges:
		visited[edges] = False

	for edges in graph.edges:
		if(visited[edges]==False):
			visited[edges] = True
			time_visited[edges] = time_count
			least_time[edges] = time_count
			dfs(graph, edges, visited,time_visited, least_time, time_count)

	#print(time_visited)
	#print(least_time)



def dfs(graph, node, visited, time_visited, least_time, time_count):
	for neighbors in graph.edges[node]:
		if(visited[neighbors] == True):
			if(time_visited[node] < least_time[neighbors]):
				return True

			else:
				least_time[node] = least_time[neighbors]

		else:
			
			visited[neighbors] = True
			time_visited[neighbors] = time_count+1
			least_time[neighbors] = time_count+1
			print("least_time: {}".format(least_time))
			dfs(graph, neighbors, visited, time_visited, least_time, time_count+1)

graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(1,4)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(5,6)
graph.addEdge(6,9)
graph.addEdge(6,7)
graph.addEdge(7,8)
graph.addEdge(8,9)
graph.addEdge(8,10)
graph.addEdge(10,11)
graph.addEdge(10,12)
graph.addEdge(11,12)
print(detectBridge(graph))


 
