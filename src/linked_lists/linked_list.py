from .node import Node


class LinkedList:
    
    def __init__(self) -> None:
        self._head = None
        self._size = 0


    def __len__(self) -> int:
        return self._size


    def empty(self) -> bool:
        return self._size == 0


    def push_front(self, value: int) -> None:
        self._head = Node(value=value, next=self._head)
        self._size += 1


    def value_at(self, index: int) -> int:
        if index < 0:
            return None 

        current = self._head
        count = 0

        while current:
            if count == index:
                break

            current = current.next
            count += 1

        return current.value if current else None


    def pop_front(self) -> int:
        if not self._head:
            return None

        value = self._head.value
        self._head = self._head.next
        self._size -= 1

        return value


    def push_back(self, value: int) -> None:
        if not self._head:
            self._head = Node(value=value)
            self._size += 1
            return None

        current = self._head

        while current.next:
            current = current.next

        current.next = Node(value=value)
        self._size += 1


    def pop_back(self) -> int:
        if not self._head:
            return None

        current = self._head
        prev = current

        if not self._head.next:
            self._head = None
            self._size = 0
            return current.value

        while current.next:
            prev = current
            current = current.next

        prev.next = None

        self._size -= 1

        return current.value


    def front(self) -> int:
        if not self._head:
            return None

        return self._head.value


    def back(self) -> int:
        if not self._head:
            return None

        current = self._head

        while current.next:
            current = current.next

        return current.value


    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > self._size:
            return None
        elif index == 0:
            return self.push_front(value) 

        current = self._head
        prev = current
        count = 0

        while count < index and current.next:            
            prev = current
            current = current.next
            count += 1

        prev.next = Node(value=value, next=current)
        self._size += 1


    def erase(self, index: int) -> int:
        if index < 0 or index > self._size:
            return None
        elif index == 0:
            return self.pop_front() 

        current = self._head
        prev = current
        count = 0

        while count < index and current.next:            
            prev = current
            current = current.next
            count += 1

        prev.next = current.next
        self._size -= 1

        return current.value


    def remove_value(self, value: int) -> int:
        if self._head.value == value:
            return self.pop_front()

        current = self._head
        prev = current
        found = False

        while current:
            if value == current.value:
                found = True
                break

            prev = current
            current = current.next

        if not found:
            return None

        prev.next = current.next
        self._size -= 1

        return current.value


    def show(self) -> None:
        current = self._head
        output = "\n\n"
        
        while current:
            output += ' -> ' + str(current.value)
            current = current.next

        print(output)