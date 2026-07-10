n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]

edges = {(a,b) for a,b in connections}
adjList = { city:[] for city in range(n)}
visit = set()
count = 0

for i,j in connections:
    adjList[i].append(j)
    adjList[j].append(i) 

def dfs(node):
    global count
    visit.add(node)
    for element in adjList[node]:
        if element in visit:
            continue
        if (element, node) not in edges:
            count +=1
        dfs(element)
    
dfs(0)
print(count)