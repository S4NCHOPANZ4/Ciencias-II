# 8 4
# 1 2 1 2 1 1 1
def solve():
    n, obj = list(map(int, input().split()))
    stops = list(map(int, input().split()))

    stack= [0]
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)
        if current==obj-1:
            print("YES")
            return 
        if current > obj -1:
            break
        next = stops[current]+current
        if next not in visited:
            stack.append(next)
        

    print("NO")        

solve()