class Node:

    def __init__(self, value:int, next:'Node'=None) -> None:
        self._value = value
        self._next = next

    @property
    def value(self) -> int:
        return self._value

    @property
    def next(self) -> 'Node':
        return self._next

    @next.setter
    def next(self, node: 'Node') -> None:
        self._next = node
