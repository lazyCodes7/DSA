def possible(graph, node, colors, mark):
    for x in range(len(graph)):
        if(graph[node][x] == 1 and colors[x] == mark):
            return False
    return True
    
def solve(graph, k, colors, node):
    if(node == len(graph)):
        return True
    
    else:
        for i in range(1,k+1):
            if(possible(graph, node, colors, i)):
                colors[node] = i
                res = solve(graph, k, colors, node+1)
                if(res):
                    return True
                colors[node] = -1
                
        return False
        
def graphColoring(graph, k, V):
    colors = {}
    for i in range(len(graph)):
        colors[i] = -1
    res = solve(graph, k, colors, 0)
    return int(res)