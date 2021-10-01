from Graph import Graph
from queue import Queue
def detectCycle(graph):
	visited = {}
	queue = Queue()
	for edge in graph.edges:
		visited[edge] = [False,-1]
	for edge in graph.edges:
		if(visited[edge][0] == False):
			queue.put(edge)
			visited[edge][0] = True
			while(queue.empty() == False):
				node = queue.get()
				for neighbor in graph.edges[node]:
					try:
						if(visited[neighbor][0] == False):
							queue.put(neighbor)
							visited[neighbor] = [True, node]
						elif(visited[neighbor][0] == True and visited[node][1]!=neighbor and visited[node][1]!=-1):
							print(visited)
							return True
					except:
						## we reached a node that was not connected to anything

						visited[neighbor] = [True, node]
	return False
graph = Graph(undirected = True)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(5,1)
print(detectCycle(graph))