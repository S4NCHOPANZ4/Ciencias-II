# 5 6
# 1 2 2
# 2 5 5
# 2 3 4
# 1 4 1
# 4 3 3
# 3 5 1
import heapq
def solve():
    vertex, n_edges = list(map(int, input().split()))
    edges = []
    for _ in range(n_edges):
        new_edge = list(map(int, input().split()))
        a,b,w = new_edge
        edges.append((w,a-1,b-1))

    adjMatrix = {vertex:[] for vertex in range(vertex)}

    for w,a,b in edges:
        adjMatrix[a].append((w,b))
        adjMatrix[b].append((w,a))

    dist = [float("inf")] * vertex
    dist[0] = 0
    parent = [-1] * vertex
    parent[0] = 0

    visited = set()
    def dijkstra(start):
        heap = [(0, start)]
        while heap:
            cw, cn = heapq.heappop(heap)
            if cn in visited:
                continue
            visited.add(cn)
            if cn == vertex - 1:
                break
            for nw, nn in adjMatrix[cn]:
                if nn not in visited:
                    new_dist = cw + nw
                    if new_dist < dist[nn]:
                        dist[nn] = new_dist
                        parent[nn] = cn
                        heapq.heappush(heap,(new_dist, nn))
    dijkstra(0)
    def getParents(start):
        res = []
        current = start
        if dist[start] == float("inf"):
            print(-1)
            return
        while current != parent[current]:
            res.append(current+1)
            current = parent[current]
        res.append(current+1)
        ans = res[::-1]
        print(ans)
    getParents(vertex-1)


solve()

    
