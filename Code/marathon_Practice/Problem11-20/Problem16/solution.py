n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# graph = [[0 for _ in range(n)] for i in range(n)]
graph = {}

def addNode(graph, s, d):
    if s not in graph:
        graph[s] = []
    if d not in graph:
        graph[d] = []
    graph[s].append(d)
    graph[d].append(s)
        
def neighbors(graph, n):
    return graph[n]
        
def dfs(graph, n, visited):
    visited[n] = True
    for neighbor in neighbors(graph,n):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    return visited

def isReacheble(graph, s, d):
    visited = [False for i in range(len(graph))]
    visited = dfs(graph,s, visited)
    return visited[d]


for i in edges:
    addNode(graph, i[0], i[1])    
nigga = [False for i in range(len(graph))]
print(nigga)
# print(neighbors(graph,0))
print(isReacheble(graph,0,4))            