from collections import deque

mat = [[0,0,0],[0,1,0],[1,1,1]]
dirs = [[-1,0],[1,0],[0,1],[0,-1]]
rows = len(mat)
cols = len(mat[0])

queue = deque()

def isValid(r,c):
    if r < rows and r >= 0 and c < cols and c >=0:
        return True
    return False

def bfs(r,c):
    queue = deque([(r,c,1)])
    visited = set()
    visited.add((r,c))
    while queue:
        r,c,d = queue.popleft()
        for mr, mc in dirs:
            nr = r+mr
            nc = c+mc
            if isValid(nr,nc) and (nr,nc) not in visited:
                if mat[nr][nc] == 0:
                    return d
                queue.append((nr,nc,d+1))
                visited.add((nr,nc))
    return 0


def searchOnes(mat):
    answer = mat
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                answer[i][j] = bfs(i,j)
    return answer

print(searchOnes(mat))

