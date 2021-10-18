from Graph import WeightedGraph
from pair import Pair
def shortestpath(graph):
	edges_len = len(set(graph.values))
	#print(edges_len)
	dp = {}
	visited = {}

	for val in list(set(graph.values)):
		dp[val] = float('inf')

	key1 = dp.keys()[0]
	dp[key1] = 0


	while(edges_len>1):
		for val in list(set(graph.values)):
			visited[val] = False

		#print(edges_len)
		#print(visited)
		for node in graph.edges:
			if(visited[node] == False):
				visited[node] = True
				dfs(graph, visited, dp, node)
		edges_len-=1
	return dp

def dfs(graph, visited, dp, node):
	try:
		for neighbors in graph.edges[node]:
			edge, weight = neighbors['edge'], neighbors['weight']
			if(visited[edge] == False):
				visited[edge] = True
				try:
					if(dp[node]+weight<dp[edge]):
						dp[edge] = dp[node]+weight
						#print(dp)
						dfs(graph, visited, dp, edge)

				except:
					pass
			else:
				try:
					if(dp[node]+weight<dp[edge]):
						dp[edge] = dp[node]+weight
						dfs(graph, visited, dp, edge)

				except:
					pass
			#print(dp)
	except:
		pass

graph = WeightedGraph(undirected = False)
graph.addEdge(1,Pair(2,6))
graph.addEdge(1, Pair(3,5))
graph.addEdge(1, Pair(4,5))
graph.addEdge(2, Pair(5,-1))
graph.addEdge(5, Pair(7,3))
graph.addEdge(3, Pair(5,1))
graph.addEdge(3, Pair(2,-2))
graph.addEdge(4, Pair(3,-2))
graph.addEdge(4, Pair(6,-1))
graph.addEdge(6, Pair(7,3))
print(shortestpath(graph))
