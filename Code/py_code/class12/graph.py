from typing import Optional, Any, List, Set, Dict
# Asumiendo que el archivo de importación se llama Class11 y contiene las clases Stack y Queue
from nig import Stack, Queue 

class Graph:
    def __init__(self):
        self.adjacency_list: Dict[Any, List[Any]] = {} 
        self.vertices: Set[Any] = set()

    def add_vertex(self, new_vertex: Any):
        if new_vertex not in self.vertices:
            self.vertices.add(new_vertex)
            self.adjacency_list[new_vertex] = []
        else:
            print("Nigga")
    
    def remove_vertex(self, vertex: Any):
        if vertex not in self.vertices: # Corregido: self.vertex -> self.vertices
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
        if (vertex_1 not in self.vertices) or (vertex_2 not in self.vertices): # Corregido: self.vertex -> self.vertices
            print("NiGgA")
        else:
            if vertex_2 in self.adjacency_list[vertex_1]:
                self.adjacency_list[vertex_1].remove(vertex_2)
            if vertex_1 in self.adjacency_list[vertex_2]:
                self.adjacency_list[vertex_2].remove(vertex_1)

    def has_edge(self, vertex_1: Any, vertex_2: Any):
        if (vertex_2 in self.adjacency_list[vertex_1] and vertex_1 in self.adjacency_list[vertex_2]):
            return True
        return False
    
    def get_neighbors(self, vertex: Any) -> Optional[List[Any]]:
        if vertex not in self.vertices:
            print(f'Nigga node {vertex} no existe.')
            return None
        return self.adjacency_list[vertex]
    
    def bfs(self, start: Any) -> List[Any]:
        if start not in self.vertices:
            raise ValueError(f'Nigga dead') # Corregido: Value -> ValueError

        visited = set()
        queue = Queue() # Corregido: Nombre de clase consistente (Queue)
        result = []

        queue.enqueue(start)
        visited.add(start)

        while not queue.is_empty():
            vertex = queue.dequeue() # Corregido: deque() -> dequeue()
            result.append(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor) # Corregido: visited.add(visited) -> visited.add(neighbor)
                    queue.enqueue(neighbor)
        return result
    
    def bfs_target(self, start: Any, target: Any) -> List[Any]:
        if start not in self.vertices:
            raise ValueError(f'Nigga dead') # Corregido: Value -> ValueError

        visited = set()
        queue = Queue()
        result = []

        queue.enqueue(start)
        visited.add(start)

        while not queue.is_empty():
            vertex = queue.dequeue() # Corregido: deque() -> dequeue()
            result.append(vertex)

            if target == vertex: # Corregido: terget -> target
                break

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor) # Corregido: visited.add(visited) -> visited.add(neighbor)
                    queue.enqueue(neighbor)
        return result

    def dfs(self, start: Any) -> List[Any]: # Corregido: Arreglada la indentación del método
        if start not in self.vertices: # Corregido: nor -> not
            raise ValueError(f'NIGGAAAA')
        visited = set()
        stack = Stack() 
        result = []

        stack.push(start)
        visited.add(start)

        while not stack.is_empty():
            vertex = stack.pop()
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]: # Corregido: Añadido ':' al final
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)
        return result

    def bfs_distances(self, start: Any) -> Dict[Any, int]:
        distances = {start: 0}
        queue = Queue()
        queue.enqueue(start) # Corregido: Se pasaba el string 'start' en lugar de la variable start

        while not queue.is_empty(): # Corregido: Consistencia usando queue.is_empty() como en los otros métodos
            vertex = queue.dequeue()
            for neighbor in self.adjacency_list[vertex]: # Corregido: Añadido ':' al final
                if neighbor not in distances:
                    distances[neighbor] = distances[vertex] + 1
                    queue.enqueue(neighbor) # Corregido: emqueue -> enqueue
    
        return distances

    def calculate_all_eccentricities(self) -> Dict[Any, int]:
        eccentricities = {}
        for vertex in self.vertices:
            distances = self.bfs_distances(vertex)
            eccentricities[vertex] = max(distances.values())
        return eccentricities

    def graph_center(self) -> List[Any]:
        if not self.vertices:
            return []        

        eccentricities = self.calculate_all_eccentricities()
        min_eccentricitie = min(eccentricities.values())

        # Corregido: .items() para desempaquetar clave/valor y corregida la sintaxis de la condición
        return sorted([v for v, ecc in eccentricities.items() if ecc == min_eccentricitie]) 

    def __str__(self) -> str: # Corregido: __srt__ -> __str__ y tipo de retorno -> str
        result = "Graph - Adjacency List\n"
        for vertex in sorted(self.vertices):
            result += f'{vertex}: {self.adjacency_list[vertex]}\n'
        return result