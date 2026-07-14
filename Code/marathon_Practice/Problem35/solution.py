import heapq
heights = [[1,2,2],[3,8,2],[5,3,5]]
rows = len(heights)
cols = len(heights[0])
dirs = [(-1,0),(1,0),(0,1),(0,-1)]

def validPos(r,c) -> bool:
    return (r < rows and r >= 0 and c < cols and c >= 0)

def djikstra(e,r,c):
    visited = set()
    heap = [(e,r,c)]
    while heap:
        ce,cr,cc = heapq.heappop(heap)
        if (cr,cc) in visited:        
            continue
        visited.add((cr,cc))
        if (cr, cc) == (rows-1, cols-1):
            return ce 
        for dr, dc in dirs:
            nr = dr+cr
            nc = dc+cc
            if  validPos(nr,nc) and (nr,nc) not in visited:
                max_distance = max(ce, abs(heights[nr][nc] - heights[cr][cc]))
                heapq.heappush(heap, (max_distance, nr, nc))
    return -1

print(djikstra(0,0,0))

