from typing import Optional, Any, List
from graph import Graph 
from nig import Queue

class Tree(Graph):
    def __init__(self, new_root: Optional[Any]):
        super.__init__()
        self.root = new_root
        if self.root is not None:
            self.add_vertex(self.root)

    def set_root(self, root: Any):
        if root not in self.vertices:
            print(f'Nodo {root} no existe')
        self.root = root


    def distance_between_nodes(self, node_1: Any, node_2: Any) -> int:
        if node_1 not in self.vertices or node_2 not in self.vertices:
            print("NIGGA. Verifique que los nodos existen en la definicion del grafo")

        distance: int = -1
        if node_1 == node_2:
            distance = 0
        
        distances = self.bfs_distances(node_1)
        distance = distances.get(node_2, -1)
        return distance

    def calculate_eccentricity(self, vertex:Any) -> Any:
        if vetex not in self.vertices:
            print(f'Nodo {vertex} NO EXISTE')
        
        vertex_distances = self.bfs_distances(vertex)
        return max(vertex_distances.values())

    def diameter_and_radius(self):
        if not self.vertices:
            diameter = 0
            radius = 0        
        eccentricities = self.calculate_all_eccentricities()
        diameter = max(eccentricities.values())
        radius = min(eccentricities.values())

        return diameter, radius

    def tree_center(self):
        return self.graph_center()

    def get_path(self, start: Any, end: Any) -> List[Any]:
        if (start not in self.vertices) or (end not in self.vertices):
            print("Los nodos no estan nigging")
        if start == end:
            solution = [start]

        #BFS to find path
        parent = {start: None}
        queue = Queue()
        queue.enqueue(start)

        while queue:
            node = self.queue.dequeue()
            if node == end:
                path = []
                curent = end
                while curremt is not None:
                    path.append(curren) 
                    current = parent(current)
                return path[::-1]
        
            for x in self.adjacency_list:
                if neighbor not in parent:
                    parent[neighbor] = node
                    self.queue.append(neighbor)
        return []

    def is_empty(self) -> bool:
        if self.root is None:
            print("No hay padres en arboles vacios")
        return self.root


    def get_parent(self, vertex: Any) ->  Optional[Any] :
        if self.root is None:
            print("No hay padres en arboles vacios")
        if vertex not in self.vertex:
            print("El node ingresado no existe")
        if vertex == self.root:
            return None
        else:
            visited = {self.root}
            queue = Queue()
            queue.enqueue(self.root)
            while queue:
                current = queue.dequeue()
                for neighbor in self.adjacency_list[current]:
                    if neighbor == vertex: 
                        parent = current
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.enqueue(neighbor)
            return parent         

    def get_children(self, vertex: Any) -> List[Any]:
        if vertex not in self.vertices or self.is_empty():
            return None
        children = self.adjacency_list[vertex]
        parent = self.get_parent(vertex)
        children.remove(parent)
        return children

    def lowest_common_ancestor(self, node_1: Any, node_2: Any) -> Optional[Any]:
        if (node_1 not in self.vertices) or (node_2 not in self.vertices):
            print("Nigaa")
            return None 

        path_1 = self.get_path(self.root, node_1)
        path_2 = self.get_path(self.root, node_2)

        if not path_1 or not path_2:
            print("Error")
            return None
        
        for anc_1, anc_2 in zip(path_1, path_2):
            if anc_1 == anc_2:
                return anc_1


    def get_depth(self, node: Any):
        if not self.is_empty():
            return self.distance_between_nodes(self.root, node)
        return -1



    # difference between height and depth 
    def get_height(self, node: Any):
        if not self.is_empty():
            max_height = 0
            for neighbor in self.adjacency_list[node]:
                if self.root and self.get_parent(neighbor) == node:
                    height = self.get_height(neighbor) + 1
                    max_height = max(max_height, height)

    def __str__(self):
        result = "Tree"
        result += f'Tree root: {self.root}'

        for vertex in sorted(self.vertices):
            result += f'{vertex}: {self.adjacency_list[vertex]}'        
        
        return result





