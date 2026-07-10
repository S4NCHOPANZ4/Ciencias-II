import heapq
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
dirs = [[-1,0],[1,0],[0,-1],[0,1]]
rows = len(heights)
cols = len(heights[0])
visit = set()

def isValidPos(r,c):
    if r < rows and r >= 0 and c < cols and c >=0:
        return True
    return False
#start at (0,0,0)
def dijkstra(e,r,c):
    heap = [(e,r,c)]
    while heap:
        ce,cr,cc = heapq.heappop(heap)
        if (cr,cc) in visit:
            continue
        visit.add((cr,cc))
        if (cr, cc) == (rows-1, cols-1):
            print(ce)
            return ce

        for dr,dc in dirs:
            nr = cr + dr
            nc = cc + dc
            if (nr,nc) in visit or not isValidPos(nr,nc):
                continue
            heapq.heappush(heap, (max(ce, abs(heights[nr][nc] - heights[cr][cc])), nr, nc))
    return -1
    
dijkstra(0,0,0)
