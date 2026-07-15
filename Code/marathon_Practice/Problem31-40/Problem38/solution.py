# 4 1
# 1 1 0 0
# 1 2
# 1 3
# 1 4
from collections import deque

def solve():
    v, max_cats = list(map(int, input().split()))
    vertices = list(map(int, input().split()))
    edges=[]
    for _ in range(v-1):
        a,b = list(map(int, input().split()))
        edges.append((a-1,b-1))
    
    adjMatrix = {vertex:[] for vertex in range(len(vertices))}

    for src,dst in edges:
        adjMatrix[src].append(dst)
        adjMatrix[dst].append(src)

    print(adjMatrix)
    visited = set()

    def isLeaf(vertex):
        if vertex == 0:
            return False
        return len(adjMatrix[vertex]) <= 1

    def bfs(start):
        queue = deque([(start, vertices[start])])
        count = 0
        if vertices[start] > max_cats:
            return count
        while queue:
            current, current_cats = queue.popleft()
            visited.add(current)
            if isLeaf(current):
                count += 1
            for neighbor in adjMatrix[current]:
                new_cats = 0
                if vertices[neighbor] != 0:
                    new_cats = current_cats+vertices[neighbor]
                if neighbor not in visited and (new_cats <= max_cats):
                    queue.append((neighbor, new_cats))
        return count 
    
    print(bfs(0))
solve()