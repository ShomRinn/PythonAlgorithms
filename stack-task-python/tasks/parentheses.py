"""Template for programming assignment: parentheses validation."""
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

def is_valid_parentheses(expression: str) -> bool:
    stack = Stack()
    bracket_dict = {')': '(', '}': '{', ']': '['}
    for i in expression:
        if i in bracket_dict.values():
            stack.push(i)
        elif i in bracket_dict.keys():
            if stack.empty() or bracket_dict[i] != stack.pop():
                return False
        else:
            return False

    return stack.empty()
