"""Templates for programming assignments: queue API."""
from typing import Any, Optional

from tasks.stack import Stack


class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.head = None  # Start of the queue
        self.tail = None  # End of the queue
        self.length = 0 

    def empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.length == 0

    def size(self) -> int:
        """Returns the number of elements in the queue."""
        return self.length

    def push(self, element: Any):
        """Adds an element to the end of the queue."""
        new_node = Node(element)
        if self.empty():
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> Any:
        """Removes and returns an element from the start of the queue."""
        if self.empty():
            raise ValueError("The queue is empty")
        removed_data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        self.length -= 1
        return removed_data

    def peak(self) -> Any:
        """Returns the first element of the queue without removing it."""
        if self.empty():
            raise ValueError("The queue is empty")
        return self.head.data


class QueueViaStacks:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def _transfer(self):
        """Transfer elements from first_stack to second_stack if second_stack is empty."""
        if self.second_stack.empty():
            while not self.first_stack.empty():
                self.second_stack.push(self.first_stack.pop())

    def empty(self) -> bool:
        """Returns True if the queue is empty."""
        return self.first_stack.empty() and self.second_stack.empty()

    def size(self) -> int:
        """Returns the number of elements within the queue."""
        return self.first_stack.size() + self.second_stack.size()

    def push(self, element: Any):
        """Adds a given element to the queue's tail."""
        self.first_stack.push(element)

    def pop(self) -> Any:
        """Returns the head element and removes it."""
        if self.empty():
            raise ValueError("The queue is empty")
        self._transfer()
        return self.second_stack.pop()

    def peak(self) -> Any:
        """Returns the head element."""
        if self.empty():
            raise ValueError("The queue is empty")
        self._transfer()
        return self.second_stack.peak()
