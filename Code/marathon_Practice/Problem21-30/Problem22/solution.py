rooms = [[1,3],[3,0,1],[2],[0]]

visited = set()

def dfs(room):
    visited.add(room)
    for key in rooms[room]:
        if key not in visited:
            dfs(key)


dfs(0)
print(len(visited) == len(rooms))