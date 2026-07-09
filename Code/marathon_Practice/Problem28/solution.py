
edges = [[1,2],[1,3],[2,3]]
rows = len(edges)

dicEdges = {(a-1,b-1) for a,b in edges}
adjList = {node: [] for node in range(rows)}

for a,b in dicEdges:
    adjList[a].append(b)
    adjList[b].append(a)





print(adjList)