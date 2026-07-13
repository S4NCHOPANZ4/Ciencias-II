from typing import Any, Optional, List

class Node:
    def __init__(self, new_data: Any):
        self.data = new_data
        self.next: Optional['Node'] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0
    
    def append(self, data: Any):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current =  current.next
            current = newNode
        self.size += 1
    
    def prepend(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def remove_and_return(self, position: str) -> Optional[Any]:
        if not self.head:
            return
        if not self.head.next:
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
        if position == 'begin':
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
        return self.head is None
    
    def __len__(self) -> int:
        return self.size 
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return ', '.join(str(item) for item in self.to_list())


class Stack(LinkedList):

    def push(self, data: Any):
        self.prepend(data)
    
    def pop(self) -> Optional[Any]:
        return self.remove_and_return('begin')
    
class Queue(LinkedList):
    def enqueue(self, data:Any):
        self.append(data)
    def dequeue(self) -> Optional[Any]:
        return self.remove_and_return('begin')


            
