import heapq
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
n = len(points)
adjList = { node:[] for node in range(n)}

def manhattanDist(a,b):
    x1,y1 = a
    x2,y2 = b
    return abs(x1-x2) + abs(y1-y2)
    
for i in range(n):
    for j in range(i+1, n):
        d = manhattanDist(points[i],points[j])
        adjList[i].append((d,j))
        adjList[j].append((d,i))


visited = set()
def prim(start):
    idist, start_node = start
    heap = [(idist, start_node)]
    res=0
    while len(visited) < n:
        dist , i = heapq.heappop(heap)
        if i in visited:
            continue
        res += dist
        visited.add(i)
        for ndist, nnode in adjList[i]:
            if nnode not in visited:
                heapq.heappush(heap, (ndist, nnode))
    return res

print(prim((0,0)))