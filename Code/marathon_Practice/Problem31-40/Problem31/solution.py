import heapq

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
adjList = {vertex:[] for vertex in range(len(points))}
n = len(points)
def manhathanDist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2 
    return abs(x1-x2) + abs(y1-y2)

for i in range(n):
    for j in range(i+1, n):
        d = manhathanDist(points[i], points[j])
        adjList[i].append((d,j))
        adjList[j].append((d,i))

visited = set() 
def prim():
    heap = ([(0,0)])
    res = 0
    while heap:
        d, v = heapq.heappop(heap)
        if v in visited:
            continue 
        visited.add(v)
        res += d
        for neighbor in adjList[v]:
            nd, nv = neighbor
            if nv not in visited:
                heapq.heappush(heap, (nd,nv))
    return res

print(prim())