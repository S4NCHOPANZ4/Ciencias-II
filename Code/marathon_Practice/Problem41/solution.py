# 5 7
# 1 2 3
# 1 3 1
# 1 4 5
# 2 3 2
# 2 5 3
# 3 4 2
# 4 5 4

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u,v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] +=1 
            return True
        return False
    
def kruskal(n_vertex, edges_list, starting_edge):
    dsu = DSU(n_vertex)

    sorted_edges = sorted(edges_list)

    mst_weight = 0
    mst_edges = []
    edges_connected = 0

    sw, su, sv = starting_edge

    dsu.union(su,sv)
    mst_weight += sw
    mst_edges.append((su,sv,sw))
    edges_connected +=1

    for weight, u, v in sorted_edges:

        if weight == sw and u == su and v == sv:
            continue

        if dsu.union(u,v):
            mst_weight += weight
            mst_edges.append((u,v,weight))
            edges_connected += 1

            if edges_connected == n_vertex - 1:
                break
    
    return mst_weight

def solve():
    vert, edge = list(map(int, input().split()))
    edges = []
    for _ in range(edge):
        a,b,w = list(map(int, input().split()))
        edges.append((w, a-1, b-1))

    results = []
    for edge in edges:
        results.append(kruskal(vert,edges,edge))
    print(results)

solve()

    