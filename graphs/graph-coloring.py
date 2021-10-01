from Graph import Graph
from queue import Queue
def coloring(graph):
	visited  = {}
	queue = Queue()
	flag = 0
	for edge in graph.edges:
		visited[edge] = [False, "Not colored"]
	for edge in graph.edges:
		if(visited[edge][0] == False):
			queue.put(edge)
			visited[edge] = [True, "Blue"]
			while(queue.empty() == False):
				node = queue.get()
				for neighbor in graph.edges[node]:
					#print("Neighbor:" + str(neighbor))
					if(visited[neighbor][0] == False):
						if(visited[node][1] == "Blue"):
							visited[neighbor] = [True, "Green"]
						else:
							visited[neighbor] = [True, "Blue"]
						queue.put(neighbor)
					else:
						if(visited[neighbor][1] == visited[node][1]):
							print("Graph is not bipartite")
							print("Stopping traversal")
							return False
	return visited
graph = Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(4,1)
print(graph.edges)
print(coloring(graph))