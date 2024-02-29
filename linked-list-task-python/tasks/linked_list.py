"""Templates for programming assignments: operations with linked list."""


from typing import List, Optional

from tasks.linked_list_node import LinkedListNode


def create_linked_list(values: List[int]) -> Optional[LinkedListNode]:
    """Returns a head element of the linked list for given values."""
    if not values:
        return None

    head = LinkedListNode(values[0])
    current = head
    for value in values[1:]:
        current.next_element = LinkedListNode(value)
        current = current.next_element

    return head



def remove_values(head: Optional[LinkedListNode], value_to_remove: int) -> Optional[LinkedListNode]:
    """Returns a head element of the new linked list after removal of all 'value_to_remove' nodes."""
    fix_node = LinkedListNode(0, head)
    current = fix_node
    while current.next_element:
        if current.next_element.value == value_to_remove:
            current.next_element = current.next_element.next_element
        else:
            current = current.next_element
    return fix_node.next_element



def reverse_linked_list(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Returns a head element of the new linked list after reversing a given linked list."""
    previous = None
    current = head
    while current:
        next_temp = current.next_element
        current.next_element = previous
        previous = current
        current = next_temp
    return previous



def get_middle_node(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Returns the middle element of a given linked list."""
    slow = fast = head
    while fast and fast.next_element:
        slow = slow.next_element
        fast = fast.next_element.next_element
    return slow

