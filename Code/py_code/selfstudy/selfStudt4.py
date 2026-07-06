from collections import deque

n = 4 
graph = [[0 for _ in range(n)] for _ in range(n)]

def addEdge(graph,u ,v):
    graph[u][v] = 1
    graph[v][u] = 1

def hasEdge(graph, u, v):
    return graph[u][v] == 1

def removeEdge(graph,u,v):
    graph[u][v] = 0
    graph[v][u] = 0

def printGraph(graph):
    for row in graph:
        print(row)

def neighbors(graph, u):
    print(f"\nBuscando vecinos de {u}")
    res = []
    for v in range(len(graph)):
        print(f"   ¿{u} está conectado con {v}?")
        if graph[u][v] == 1:
            print(f"      Sí -> agrego {v}")
            res.append(v)
        else:
            print("      No")
    print(f"{u} Esta conectado a: {res}")

    return res

def dfs(graph, node, visited):
    print(f"\nEntré al nodo {node}")
    visited[node] = True
    print("Visitados:", visited)
    for neighbor in neighbors(graph, node):
        if not visited[neighbor]:
            print(f"voy hacia {neighbor}")
            dfs(graph, neighbor, visited)
        else:
            print(f"{neighbor} ye fue visitado")

def bfs(graph, start):
    visited = [False]*len(graph)
    queue=deque()
    queue.append(start)
    visited[start]=True


    while queue:
        print(f"Cola:", list(queue))
        node=queue.popleft()
        print(f"Procesando {node}")
        for neighbor in neighbors(graph,node):
            print(f"Resicando {neighbor}")
            if not visited[neighbor]:
                print(f"{neighbor} a la cola")
                visited[neighbor]=True
                queue.append(neighbor) 
            else:
                print(f"{neighbor} Ya fue visitado")
        print("Visirados: ", visited)
            



addEdge(graph,0,1)
addEdge(graph,0,2)
addEdge(graph,1,2)
addEdge(graph,1,3)
    

