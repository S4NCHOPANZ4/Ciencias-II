import heapq
times = [[1,2,1]]
n = 2
k = 1
visited = set()

edges = {(a-1,b-1,c) for a,b,c in times}
adjList = {node:[] for node in range(n)}

for i,j,dist in edges:
    adjList[i].append((j,dist))

distance = 0
def bfs(start):
    minheap = [(0, start)]
    maxDistance = 0
    while minheap:
        d, current_  = heapq.heappop(minheap)
        if current_ in visited:
            continue
        visited.add(current_)
        maxDistance = max(maxDistance, d)
        for neighbor, nd in adjList[current_]:
            if neighbor in visited:
                continue
            heapq.heappush(minheap, (d + nd, neighbor))
    return maxDistance, visited


ansd , visited = bfs(k-1)
if len(visited) == n:
    print(ansd)
else: 
    print(-1)
