"""Template for programming assignment: Reverse Polish notation."""
from typing import Any, List

class Node:
    def __init__(self, data: Any, next_node=None):  # Corrected __init__ method
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self):  # Corrected __init__ method
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

    def peek(self) -> Any:
        if self.empty():
            raise ValueError("The stack is empty")
        return self.top.data

def evaluate_rpn_tokens(rpn_tokens: List[str]) -> int:
    stack = Stack()

    for token in rpn_tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(int(operand1 / operand2))

    return stack.peek()
