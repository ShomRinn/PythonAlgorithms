# Linked List

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:
* Basic data structure for elements of linked lists
* Operations with linked lists

## Overview

The coding exercises cover the following practical problems:
* Creating a linked list using given values
* Removing elements of a linked list by value
* Reversing a linked list
* Finding the middle element of a linked list

## Coding exercises

### Exercise 1: Create a linked list using a given array of values

#### Elements of linked lists

The following snippet contains the very basic data structure that could be used to represent elements of linked lists. Of course, the class can be expanded with additional information if necessary.

```python
class LinkedListNode:
    """Dataclass that represents linked list elements."""

    def __init__(
        self,
        value: int = 0,
        next_element: Optional['LinkedListNode'] = None
    ):
        self.value = value
        self.next_element = next_element
```

Assume that, for all programming assignments in this set of coding exercises, the following data class
will be used to represent elements of linked lists. The implementation above can be found in the `tasks/linked_list_node.py` file.

For example, the following linked list can be created using the snippet below:

```mermaid
graph LR;
    A[value=5] == next_element ===> B[value=107] == next_element ===> C[value=42]
```

```python
a = LinkedListNode(value=42)
b = LinkedListNode(value=107, next_element=a)
c = LinkedListNode(value=5, next_element=b)
```

#### Problem statement

Given an array of values, return a linked list with the initial values (its head element).

**Example:**

Input: [23, 1, 49]

Expected result:
```mermaid
graph LR;
    A[value=23] == next_element ===> B[value=1] == next_element ===> C[value=49]
    style A fill:#f9f,stroke:#333,stroke-width:4px
```

<br/>

Please use the template `tasks/linked_list:create_linked_list` for the implementation.

### Exercise 2: Remove elements of linked list by value

Given the `head` of a linked list and an integer `value`, remove all the nodes of the linked list that have `LinkedListNode.value == value`, and return *the new head*.


**Example 1:**

```mermaid
graph LR;
    subgraph Result Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23]
    end

    subgraph Input Linked List
    A[value=5] --> B[value=107] --> C[value=42] --> D[value=5] --> E[value=23] --> F[value=5]
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style D fill:#f9f,stroke:#333,stroke-width:4px
    style F fill:#f9f,stroke:#333,stroke-width:4px
    end
```

Here and in the examples below the element to remove is `42`. 

**Example 2:**

Input: [42, 42, 42]

Expected result: []


**Example 3:**

Input: []

Expected result: []

<br/>

Please use the template `tasks/linked_list:remove_values` for the implementation.


### Exercise 3: Reverse a given linked list

Given the `head` of a linked list, reverse the list, and return the head of the reversed list.


**Example 1:**

```mermaid
graph LR;
    subgraph Result Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23]
    end

    subgraph Input Linked List
    B[value=23] --> C[value=42] --> E[value=107]
    end
```

**Example 2:**

```mermaid
graph LR;
    subgraph Result Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23] --> AA[value=21] --> DD[value=2] --> FF[value=0]
    end

    subgraph Input Linked List
    F[value=0] --> A[value=2] --> D[value=21] --> B[value=23] --> C[value=42] --> E[value=107]
    end
```

**Example 3:**

Input: []

Expected result: []

<br/>

Please use the template `tasks/linked_list:reverse_linked_list` for the implementation.


### Exercise 4: Find the middle node of a given linked list

Given the `head` of a linked list, return *the middle node of the linked list*.

If there are two middle nodes, return **the second middle** node.

**Example 1:**

```mermaid
graph LR;
    subgraph Input Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23] --> AA[value=21] --> DD[value=2] --> FF[value=0]
    end

    style AA fill:#f9f,stroke:#333,stroke-width:4px
```

**Example 2:**

```mermaid
graph LR;
    subgraph Input Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23] --> AA[value=21] --> DD[value=2]
    end

    style EE fill:#f9f,stroke:#333,stroke-width:4px
```

**Example 3:**

Input: []

Expected result: []

<br/>

Please use the template `tasks/linked_list:get_middle_node` for the implementation.
