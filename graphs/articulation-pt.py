from Graph import Graph

def articulation(graph):
	visited = {}
	articulations = []
	ti = {}
	lt = {}
	time_count = 1
	child = 0
	for edges in graph.edges:
		visited[edges] = False
		ti[edges] = -1
		lt[edges] = -1

	for edges in graph.edges:
		if(visited[edges] == False):
			visited[edges] = True
			ti[edges] = time_count
			lt[edges] = time_count
			dfs(visited, articulations, edges, -1, ti, lt, time_count)

	return articulations


def dfs(visited, articulations, node, parent, ti, lt, time_count):
	child = 0
	for neighbors in graph.edges[node]:
		if(visited[neighbors] == False):
			#print(ti)
			#print(lt)
			if(node == parent):
				continue
			visited[neighbors] = True
			ti[neighbors] = time_count+1
			lt[neighbors] = time_count+1
			dfs(visited, articulations, neighbors, node, ti, lt, time_count+1)
			child+=1

			if(lt[neighbors] >= ti[node] and parent!=-1):
				articulations.append(node)

			elif(lt[neighbors]<lt[node]):
				lt[node] = lt[neighbors]

		else:
			lt[node] = min(lt[node], ti[neighbors])
			#print(ti)
			#print(lt)
	if(parent == -1 and child>1):
		print(child)
		articulations.append(node)

graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(1,4)
graph.addEdge(4,5)
graph.addEdge(5,6)
graph.addEdge(6,7)
graph.addEdge(7,8)
graph.addEdge(8,9)
graph.addEdge(9,6)
graph.addEdge(8,10)
graph.addEdge(10,11)
graph.addEdge(11,12)
graph.addEdge(12,10)
print(articulation(graph))