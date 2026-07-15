# 4 1
# 1 1 0 0
# 1 2
# 1 3
# 1 4

from collections import deque

def solve():
    n_vert, max_cats = list(map(int, input().split()))
    vertx = list(map(int, input().split()))
    edges = []
    for _ in range(n_vert-1):
        new_edge = list(map(int, input().split()))
        src, dst = new_edge
        edges.append((src-1, dst-1))
    
    adjMatrix = {vert:[] for vert in range(n_vert)}

    for src,dst in edges:
        adjMatrix[src].append(dst)
        adjMatrix[dst].append(src)

    def isLeaf(edge):
        return len(adjMatrix[edge]) == 1
    
    visited = set()
    def bfs(start):
        queue = deque([start, vertx[start]])
        posible = 0
        if vertx[start] > max_cats:
            return -1
        while queue:
            current,current_cat = queue.popleft()
            if (current, current_cat) in visited:
                continue
            visited.add((current, current_cat))
            if isLeaf(current) and  current != 0:
                posible +=1 
                continue
            for neighbor, cat in adjMatrix[current]:
                new_cat = 0
                if vertx[neighbor] == 1:
                    new_cat = vertx[neighbor] + cat 

                if (neighbor, cat) not in visited and new_cat < max_cats:
                    queue.append((neighbor,new_cat) )
        return posible
    print(bfs(0))
solve()


