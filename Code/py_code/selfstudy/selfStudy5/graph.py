from typing import Optional, Any, Set, List, Dict
from data_structures import Stack, Queue 

class Graph:

    def __init__(self):
        self.adjacency_list: Dict[Any, List[Any]] = {}
        self.vertices = Set[Any] = set()
    
    def add_vertex(self, new_vertex: Any):
        if new_vertex not in self.vertices:
            self.vertices.add(new_vertex)
            self.adjacency_list[new_vertex] = []
        else: 
            print("vertex not added")
    
    def remove_vertex(self, vertex: Any):
        if vertex not in self.vertices:
            print("Vertex not Found")
        else:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]
            self.vertices.remove(vertex)
        
    def add_edge(self, vertex_1: Any, vertex_2: Any):
        if vertex_1 == vertex_2:
            print("Node can not be connected to itself")
        else:
            if vertex_2 not in self.adjacency_list[vertex_1]:
                self.adjacency_list[vertex_1].append(vertex_2)
            if vertex_1 not in self.adjacency_list[vertex_2]:
                self.adjacency_list[vertex_2].append(vertex_1)
        
    
    def remove_edge(self, vertex_1: Any, vertex_2: Any):
        if (vertex_1 not in  self.vertices) or(vertex_2 not in self.vertices):
            print("Could not delete check graph structure")
        else:
            if vertex_2 in self.adjacency_list[vertex_1]:
                self.adjacency_list[vertex_1].remove(vertex_2)
            if vertex_1 in self.adjacency_list[vertex_2]:
                self.adjacency_list[vertex_2].remove(vertex_1)

    def has_edge(self, vertex_1: Any, vertex_2: Any) -> bool:
        if (vertex_2 in self.adjacency_list[vertex_1]) and (vertex_1 in self.adjacency_list[vertex_2]):
            return True
        return False

    def get_neighbors(self, vertex: Any) -> Optional[Any]:
        if vertex not in self.vertices:
            return None
        return self.adjacency_list[vertex]
    
    def bfs(self, start: Any) -> List[Any]:
        if start not in self.vertices:
            print("Node not available")
        visited = set()
        queue = Queue()
        result = []

        queue.enqueue(start)
        visited.add(start)
        while not queue.is_empty():
            vertex = queue.dequeue()
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        return result
    
    def bfs(self, start: Any, target: Any) -> List[Any]:
        if start not in self.vertices:
            print("Node not available")
        visited = set()
        queue = Queue()
        result = []

        queue.enqueue(start)
        visited.add(start)
        while not queue.is_empty():
            vertex = queue.dequeue()
            result.append(vertex)

            if vertex == target:
                break
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        return result
    
    def dfs(self, start: Any) -> List[Any]:
        if start not in self.vertices:
            raise ValueError("Starting vertex not found")
        
        visited = set()
        stack = Stack()
        result = []

        stack.push(start)
        visited.add(start)
        while not stack.is_empty():
            vertex = stack.pop()
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)
        return result
    
    def bfs_distances(self, start: Any) -> Dict[Any, int]:
        distances = {start: 0}
        queue = Queue()
        queue.enqueue(start)

        while not queue.is_empty():
            vertex = queue.dequeue()
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in distances:
                    distances[neighbor] = distances[vertex]+1
                    queue.enqueue(neighbor)
        
        return distances

    def calculate_all_eccentricities(self) -> Dict[Any,int]:
        eccentricities = {}
        for vertex in self.vertices: 
            distances = self.bfs_distances(vertex)
            eccentricities[vertex] = max(distances.values())
        return eccentricities

    def graph_center(self) -> List[Any]:
        if not self.vertices:
            return []
        eccentricities = self.calculate_all_eccentricities()
        min_eccentricities = min(eccentricities.values())
        
        return sorted([v for v,ecc in eccentricities.items() if ecc == min_eccentricities])
    
    def __str__(self) -> str:
        result  = "Graph - adjList \n"
        for  vertex in sorted(self.vertices):
            result += f'{vertex}: {self.adjacency_list[vertex]}'
        return result