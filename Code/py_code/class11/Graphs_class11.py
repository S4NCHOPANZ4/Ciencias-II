from typing import Optional, Any, List, Set
from Class11 import Stack, queue

class Graph:
    def __init__(self):
        self.adjacency_list: Dict[Any, List[Any]] 
        self.vertices: Set[Any] = set()

    def add_vertex(self,new_vertex: Any):
        if new_vertex not in self.vertices:
            self.vertices.add(new_vertex)
            self.adjacency_list[new_vertex] = []
        else:
            print("Nigga")
    
    def remove_vertex(self, vertex: Any):
        if vertex not in self.vertex:
            print("No nigga")
        else:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]
            self.vertices.remove(vertex)
            
    def add_edge(self, vertex_1: Any, vertex_2: Any):
        if vertex_1 == vertex_2:
            print("Nigga!?")
        else:
            if (vertex_1 not in self.vertices) or (vertex_2 not in self.vertices):
                print("aggiN")
            else:
                if vertex_2 not in self.adjacency_list[vertex_1]:
                    self.adjacency_list[vertex_1].append(vertex_2)
                if vertex_1 not in self.adjacency_list[vertex_2]:
                    self.adjacency_list[vertex_2].append(vertex_1)
                     

    def remove_edge(self, vertex_1: Any, vertex_2: Any):
        if (vertex_1 not in self.vertex) or (vertex_2 not in self.vertex):
            print("NiGgA")
        else:
            if vertex_2 in self.adjacency_list[vertex_1]:
                self.adjacency_list[vertex_1].remove(vertex_2)
            if vertex_1 in self.adjacency_list[vertex_2]:
                self.adjacency_list[vertex_2].remove(vertex_1)

    def has_edge(self, vertex_1: Any, vertex_2:Any):
        if(vertex_2 in self.adjacency_list[vertex_1] and vertex_1 in self.adjacency_list[vertex_2]):
            return True
        return False
    
    def get_neighbors(self, vertex: Any)-> Optional[List[Any]]:
        if vertex not in self.vertices:
            print(f'Nigga node {vertex} no existe.')
            return None
        return self.adjacency_list[vertex]
    
    def bfs(self, start: Any) -> List[Any]:
        if start not in self.vertices:
            raise Value(f'Nigga dead')

        visited = set()
        queue = Queue()
        result = []

        queue.enqueue(start)
        visited.add(start)

        while not queue.is_empty():
            vertex = queue.deque()
            result.append(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(visited)
                    queue.enqueue(neighbor)
        return result
    
    def bfs_target(self, start: Any, target: Any) -> List[Any]:
        if start not in self.vertices:
            raise Value(f'Nigga dead')

        visited = set()
        queue = Queue()
        result = []

        queue.enqueue(start)
        visited.add(start)

        while not queue.is_empty():
            vertex = queue.deque()
            result.append(vertex)

            if terget == vertex:
                break

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(visited)
                    queue.enqueue(neighbor)
        return result

        def dfs(self, start: Any) -> List[Any]:
            if start nor in self.vertices:
                raise ValueError(f'NIGGAAAA')
            visited = set()
            stack = Stack() 
            result = []

            stack.push(start)
            visited.add(start)

            while not stack.is_empty():
                vertex = stack.pop()
                result.append(vertex)
                for neighbor in self.adjacency_list[vertex]
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.push(neighbor)
        
        return result