grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
visited = set()
movs = [[-1,0], [1,0], [0,1], [0,-1]]
row = len(grid)
cols = len(grid[0])
def isValid(r,c):
    return r < row and r >= 0 and c < cols and c >= 0


def dfs(r,c, add):
    visited.add((r,c))
    add = 1
    for mov in movs:
        nr = r + mov[0]
        nc = c + mov[1]
        if isValid(nr,nc) and grid[nr][nc] != 0 and (nr,nc) not in visited:
            add =  add + dfs(nr,nc, add)
    return add


def maxArea(grid):
    max = 0
    current = 0
    for i in range(len(grid)):
        for j in  range (len(grid[0])):
            if grid[i][j] != 0 and (i,j) not in visited:
                current = dfs(i,j,current)
                if current > max:
                    max = current
                current = 0
    return max
print(maxArea(grid))
