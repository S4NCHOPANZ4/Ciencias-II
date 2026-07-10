#  grid: List[List[str]]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

visited = {}
rows = len(grid)
cols = len(grid[0]) 
def addVisited(r,c):
    if r not in visited:
        visited[r] = []
    visited[r].append(c)

def wasVisited(r,c):
    if r not in visited:
        return False
    if c in visited[r]:
        return True
    return False

def isValid(r,c):
    return r < rows and r >= 0 and c < cols and c >= 0

def dfs(r,c):
    movs = [[-1,0], [1,0], [0,1], [0, -1]]
    addVisited(r,c)
    for mov in movs:
        nr = r + mov[0]
        nc = c + mov[1]
        if isValid(nr,nc) and int(grid[nr][nc]) == 1 and wasVisited(nr,nc) == False:
            dfs(nr,nc)


def searchLand(grid):
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value = int(grid[i][j])
            if value == 1 and wasVisited(i,j) == False:
                islands+=1 
                dfs(i,j)
    return islands


print(searchLand(grid))
