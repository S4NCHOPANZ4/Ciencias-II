edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
edgeList = [(s-1,d-1) for s,d in edges]
n = len(edges)
parents = [i for i in range(n)] 
def find(vertex):
    x = vertex
    while parents[x] != x:
        x = parents[x]
    return x
def union(x1 ,x2):
    root_1 = find(x1)
    root_2 = find(x2)
    if root_1 == root_2:
        return [x1+1,x2+1]
    parents[root_2] = root_1


for s,d in edgeList:
    res = union(s,d)
    if res != None:
        print(res)

# adjList = {vertex:[] for vertex in range(n)}

# def add(new_vertex):
#     s,d = new_vertex
#     adjList[s].append(d)
#     adjList[d].append(s)
#     if     

    


# def msp():
#     visited = set()
#     for c,d in edgeList:
#         if d in visited:
#             return [c,d]
#         visited.add(c)
#         visited.add(d)
#     return -1

# print(msp())

