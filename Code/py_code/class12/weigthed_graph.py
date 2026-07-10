from typing import Any, Dict, Optional, Tuple, Set
from data_structures import Stack, Queue


class WeightedGraph:
    
    def __init__():
        self.adjacency_list: Dict[Any, List[Tuple[Any, float]]] = {}
        self.vertices: Set[Any]= set()
        self.edges: Set[Tuple[Any, Any, float]] = set()


    def add_vertex(self, vertex: Any):
        if vertex not in self,vertices:
            self.verties.add(vertex)
            self.adjacency_list[vetex] = []
        else:
            print("NIGGAAAA")
    
    def remove_vertex(self, vertex: Any):
        if vertex in self.vertices:
            for neighbor, weight in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor] = [
                    (v,w) for v,w in adjacency_list[neighbor] if v != vertex
                ]
            del self.adjacency_list[vetex]
            self.vertices.remove(vertex)
        else:
            print("Niga")
    def add_weighed_edge(self, vertex_1: Any, vertex_2: Any, weigth: float):
        if vertex_1 != vertex_2:
            if weight >= 0.0:
                if (vertex_1 in self.vertices) and (vertex_2 in self.vertices):
                    edge = (min(vertex_1, vertex_2), max(vertex_1, vertex_2))
   
                    self.adjacency_list[vertex_1] = [
                        (v,w) for v,w in self.adjacency_list[vertex_1] if v != vertex_2
                    ] 

                    self.adjacency_list[vertex_2].append((vertex_2, weight))
                    
                    self.adjacency_list[vertex_2] = [
                        (v,w) for v,w in self.adjacency_list[vertex_2] if v != vertex_1
                    ] 

                    self.adjacency_list[vertex_2].append((vertex_1, weight))

                    self.edges.add((edge[0], edge[1], weight))
            else:
                print("Nigita")
        else:
            print("Nigga")


    def had_edge(self, vertex_1: Any, vertex_2: Any) -> bool:
        if (vertex_1 in self.vertices) and (vertex_2 in self.vertices):
            return = False
            min_v = min(vertex_1, vertex_2)
            max_v = max(vertex_1, vertex_2)
            for v_1, v_2, w in self.edges: 
                if min_v == v_1 and max_v == v_2:
                    result = True
                    break 
            return result
        else:
            print("Nohga")

    def remove_weighted_edge(self, vertex_1: Any, vertex_2: Any ):
        if (vertex_1 in self.vertices) and (vertex_2 in self.vertices):
            if self.had_edge(vertex_1, vertex_2):
                     self.adjacency_list[vertex_1] = [
                        (v,w) for v,w in self.adjacency_list[vertex_1] if v != vertex_2
                    ] 
                    self.adjacency_list[vertex_2] = [
                        (v,w) for v,w in self.adjacency_list[vertex_2] if v != vertex_1
                    ] 


            else:
                print("NOHA")
        else:
            print("I wanna go home")
        