# 5 2
# 2 5 3 4 8
# 1 4
# 4 5

def solve():
    n,c = list(map(int, input().split()))
    persons = list(map(int, input().split()))
    edges = []
    for i in range(c):
        src, dst = list(map(int, input().split()))
        edges.append((src,dst))
    
    adjList = {i:[] for i in persons}

    for edge in edges:
        a, b =edge
        src = persons[a-1]
        dst = persons[b-1]
        adjList[src].append(dst)
        adjList[dst].append(src)
    
    visited = set()

    def dfs(start):
        stack = [start]
        min_val = float("inf")
        while stack:
            current = stack.pop()
            visited.add(current)
            min_val = min(min_val, current)
            for neighbor in adjList[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return min_val
    total = 0
    for i in adjList:
        if i not in visited:
            total += dfs(i)
    
    return total

print(solve())