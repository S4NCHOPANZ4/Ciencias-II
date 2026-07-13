import heapq
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
edges = {(a-1, b-1, c) for a,b,c in times}
adjList = { node:[] for node in range(n)}

for a,b,c in edges:
    adjList[a].append((b,c))

def dijkstra(sn):
    dist = [float("inf")] * n
    dist[sn] = 0
    heap = [(0,sn)]
    while heap:
        w, vertex = heapq.heappop(heap)
        if w > dist[vertex]:
            continue
        for nv, nw in adjList[vertex]:
            new_dist = w + nw
            if new_dist < dist[nv]:
                heapq.heappush(heap, (new_dist, nv))
                dist[nv] = new_dist

    return dist

ans_ = dijkstra(k-1)

if float("inf") in ans_:
    print(-1) 
else: 
    print(max(ans_))



