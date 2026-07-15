# 3 3
# 1 2 0
# 3 4 0
# 0 0 5

def solve():
    row, col = list(map(int, input().split()))
    pool = []
    for i in range(row):
        new_row = list(map(int, input().split()))
        pool.append(new_row)
    
    def isValid(r,c):
        return (r < row and r>=0 and c < col and c >=0)

    dirs = [(-1,0), (1,0), (0,1), (0,-1)]
    visited = set()

    def dfs(sr,sc):
        stack = [(sr,sc)]
        total_pool = 0
        while stack:
            cr, cc = stack.pop()
            if (cr,cc) in visited:
                continue
            visited.add((cr,cc))
            total_pool = total_pool + pool[cr][cc]
            for dr,dc in dirs:
                nr = cr + dr
                nc = cc + dc
                if isValid(nr,nc) and (nr,nc) not in visited and pool[nr][nc] > 0:
                    stack.append((nr,nc))
        return total_pool


    def searchMaxDepth():
        max_depth = 0
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and pool[i][j] != 0:
                    max_depth = max(max_depth, dfs(i,j))
        
        return max_depth

    print(searchMaxDepth())


solve()