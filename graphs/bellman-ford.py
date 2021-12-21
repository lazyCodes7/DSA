from Graph import WeightedGraph
from pair import Pair
def shortestpath(graph):
	edges_len = len(set(graph.values))
	#print(edges_len)
	dp = {}
	visited = {}

	for val in list(set(graph.values)):
		dp[val] = float('inf')

	key1 = list(dp.keys())[0]
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

graph = WeightedGraph()
graph.addEdge("r",Pair("s",-3))
graph.addEdge("s", Pair("t",3))
graph.addEdge("v", Pair("t",1))
graph.addEdge("t", Pair("s",-1))
graph.addEdge("v", Pair("r",5))
graph.addEdge("s", Pair("v",-2))
graph.addEdge("u", Pair("s",1))
graph.addEdge("u", Pair("v",1))
graph.addEdge("w", Pair("u",1))
print(shortestpath(graph))
