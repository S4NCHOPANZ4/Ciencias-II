from typing import Any, Dict, List, Tuple, Set


class WightedGraph:

    def __int__(self):
        self.adjacency_list: Dict[Any, List[Tuple[Any, float]]] = {}
        self.vertices: Set[Any] = set()
        self.edges: Set[Tuple[Any,Any,float]]= set()

    def add_vertex(self, vertex:Any):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adjacency_list[vertex] = []
        else:
            print("Vertex already exists")
    
    def remove_vertex(self, vertex):
        if vertex not in self.vertices:
            print("Vertex not found")
            return 
        for neighbor, _ in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor] = [
                (v,w)
                for v,w in self.adjacency_list[neighbor]
                if v!= vertex
            ]

        self.edges = {
            (u,v,w)
            for (u,v,w) in self.edges
            if u != vertex and v != vertex
        }

        del self.adjacency_list[vertex]
        self.vertices.remove(vertex)
    
    def add_weghted_edge(
        self,
        vertex_1:Any,
        vertex_2:Any,
        weight: float
    ):
        if vertex_1 == vertex_2:
            print("Vertex cannot connect itself.")
            return

        if weight < 0:
            print("Weight must be non-negative.")
            return 

        if (vertex_1 not in self.vertices) or (vertex_2 not in self.vertices):
            print("One or both vertices do not exist.")
            return
        
        self.adjacency_list[vertex_1] = [
            (v,w)
            for v,w in self.adjacency_list[vertex_1]
            if v != vertex_2
        ]

        self.adjacency_list[vertex_2] = [
            (v,w)
            for v,w in self.adjacency_list[vertex_2]
            if v != vertex_1
        ]

        self.adjacency_list[vertex_1].append((vertex_2, weight))
        self.adjacency_list[vertex_2].append((vertex_1, weight))

        self.edges = {
            (u,v,w)
            for (u,v,w) in self.edges 
            if not (
                u == min(vertex_1, vertex_2)
                and
                v == max(vertex_1, vertex_2)
            )
        }

        edge = (
            min(vertex_1, vertex_2),
            max(vertex_1, vertex_2),
            weight
        )

        self.edges.add(edge)

    def has_edge(self, vertex_1: Any, vertex_2: Any) -> bool:
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            print("One or both vertices do not exist")
            return False
    
        min_v = min(vertex_1 , vertex_2)
        max_v = max(vertex_1 , vertex_2)

        for u, v, _ in self.edges:
            if u == min_v and v == max_v:
                return True
        
        return False

    def remove_weighted_edge(self, vertex_1: Any, vertex_2: Any):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            print("One or both vertices do not exist")
            return 

        if not self.has_edge(vertex_1, vertex_2):
            print("No edge was found")
            return 
        
        self.adjacency_list[vertex_1] = [
            (v,w)
            for v, w in self.adjacency_list[vertex_1]
            if v != vertex_2
        ]

        self.adjacency_list[vertex_2] = [
            (v,w)
            for v, w in self.adjacency_list[vertex_2]
            if v != vertex_1
        ]

        min_v = min(vertex_1,vertex_2)
        max_v = max(vertex_1,vertex_2)

        self.edges = {
            (u,v,w)
            for (u,v,w) in self.edges
            if not (u == min_v and v == max_v)
        }

    def get_neighbors(self, vertex: Any):
        if vertex not in self.vertices:
            return None
        return self.adjacency_list[vertex]
        
    def __str__(self):
        """Representación del grafo como lista de adyacencia."""

        result = "Weighted Graph\n"

        for vertex in sorted(self.vertices):
            result += f"{vertex}: {self.adjacency_list[vertex]}\n"

        return result    
        
