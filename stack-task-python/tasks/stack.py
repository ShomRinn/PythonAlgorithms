from typing import Any

class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def empty(self) -> bool:
        return self.length == 0

    def size(self) -> int:
        return self.length

    def push(self, element: Any):
        new_node = Node(element, self.top)
        self.top = new_node
        self.length += 1

    def pop(self) -> Any:
        if self.empty():
            raise ValueError("The stack is empty")
        top_data = self.top.data
        self.top = self.top.next_node
        self.length -= 1
        return top_data

    def peak(self) -> Any:
        if self.empty():
            raise ValueError("The stack is empty")
        return self.top.data

class StackWithMinimum(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = []

    def push(self, element: Any):
        super().push(element)
        if not self.min_stack or element < self.min_stack[-1]:
            self.min_stack.append(element)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> Any:
        if self.empty():
            raise ValueError("The stack is empty")
        popped_element = super().pop()
        self.min_stack.pop()
        return popped_element

    def get_minimum(self) -> Any:
        if self.empty():
            return None
        return self.min_stack[-1]
