from typing import Any, Optional, List

class Node:
    def __init__(self, new_data: Any):
        """Class constructor"""
        self.data = new_data
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0

    def append(self, data: Any):
        """Add to the end"""
        new_node = Node(data)
        if not self.head: # empty list
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data: Any):
        """Add to the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove_and_return(self, position: str) -> Optional[Any]:
        if not self.head:
            return None
        
        if not self.head.next:
            # One element list
            value = self.head.data
            self.head = None
            self.size -= 1 
            return value
        
        if position == 'end':
            current = self.head
            while current.next.next:
                current = current.next
            value = current.next.data
            current.next = None
            self.size -= 1
            return value
        elif position == 'begin': # Corregido: Añadido el ':' que faltaba
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value
        else:
            return None

    def to_list(self) -> List[Any]:
        result = [] 
        current = self.head 
        while current:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self) -> bool:
        # Corregido: Antes devolvía el nodo completo (o None), ahora evalúa a un booleano real
        return self.head is None

    def __len__(self) -> int:
        return self.size 
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data 
            current = current.next 

    def __str__(self) -> str:
        # Corregido: Cambiado self.to_list() para que coincida con el nombre del método
        return ', '.join(str(item) for item in self.to_list())


class Stack(LinkedList):
    def push(self, data: Any):
        # Corregido: Eliminado el guion bajo para usar el método público de la clase padre
        self.prepend(data)
    
    def pop(self) -> Optional[Any]: # Comúnmente llamado 'pop' en pilas, mantengo la estructura
        # Corregido: Eliminado el guion bajo
        return self.remove_and_return('begin')

    def pull(self) -> Optional[Any]:
        """Alias para pop por compatibilidad con tu código original"""
        return self.remove_and_return('begin')


class Queue(LinkedList):
    def enqueue(self, data: Any):
        # Corregido: Eliminado el guion bajo
        self.append(data)
        
    def dequeue(self) -> Optional[Any]:
        # Corregido: Eliminado el guion bajo
        return self.remove_and_return('begin')