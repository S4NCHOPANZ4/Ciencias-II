n = 2
trust = [[1,2]]
out_degree = [0 for _ in range(n)] 
in_degree = [0 for _ in range(n)]
posibles = []
adjList = {}

for i in trust:
    in_ = i[0]
    out_ = i[1]
    out_degree[in_-1] +=1
    in_degree[out_-1] +=1

for i in range(n):
    print(out_degree[i] , in_degree[i])
    if out_degree[i] == 0 and in_degree[i] == n-1:
        posibles.append(i)

unicidad = len(posibles)
if unicidad == 1:
    print(posibles[0] + 1)
else:
    print(-1)