image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
startColor = image[sr][sc]
rows = len(image)
cols = len(image[0])
visited = {}
directions = [[-1, 0],[1,0],[0,1],[0,-1]] 

def isValid(r,c):
    return r < rows and r >= 0 and c < cols and c >= 0 

def addVisited(r,c):
    if r not in visited:
        visited[r] = []
    visited[r].append(c)

def wasNotVisited(r,c):
    if r not in visited:
        return True
    if c in visited[r]:
        return False 
    return True


def dfs(r ,c):
    image[r][c] = color
    addVisited(r,c)
    for i in directions:
        nr = r+i[0]
        nc = c+i[1]
        if isValid(nr,nc) and image[nr][nc] == startColor and wasNotVisited(nr,nc):
            dfs(nr, nc)
dfs(sr,sc)
print(image)
     
