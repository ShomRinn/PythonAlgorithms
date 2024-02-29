"""Sample tests for 'tasks.linked_list' module."""

from tasks.linked_list import (create_linked_list, get_middle_node,
                               remove_values, reverse_linked_list)
from tasks.linked_list_node import LinkedListNode


def test_create_linked_list_sample():
    """Sample tests for create_linked_list function."""
    assert create_linked_list([]) is None

    head = create_linked_list([1, 2, 3, 4])
    assert head.value == 1
    assert head.next_element.value == 2
    assert head.next_element.next_element.value == 3
    assert head.next_element.next_element.next_element.value == 4
    assert head.next_element.next_element.next_element.next_element is None


def test_remove_values_sample():
    """Sample tests for remove_values function."""
    assert remove_values(None, 107) is None

    assert remove_values(LinkedListNode(107), 107) is None

    head = remove_values(create_linked_list([107, 1, 107, 107, 2, 107, 3, 107, 4, 107]), 107)
    assert head.value == 1
    assert head.next_element.value == 2
    assert head.next_element.next_element.value == 3
    assert head.next_element.next_element.next_element.value == 4
    assert head.next_element.next_element.next_element.next_element is None


def test_reverse_linked_list_sample():
    """Sample tests for reverse_linked_list function."""
    assert reverse_linked_list(None) is None

    head = reverse_linked_list(LinkedListNode(107))
    assert head.value == 107
    assert head.next_element is None

    head = reverse_linked_list(create_linked_list([1, 2, 3, 4, 5]))
    assert head.value == 5
    assert head.next_element.value == 4
    assert head.next_element.next_element.value == 3
    assert head.next_element.next_element.next_element.value == 2
    assert head.next_element.next_element.next_element.next_element.value == 1
    assert head.next_element.next_element.next_element.next_element.next_element is None


def test_get_middle_node_sample():
    """Sample tests for get_middle_node function."""
    assert get_middle_node(None) is None

    middle_node = get_middle_node(create_linked_list([1, 2, 3, 4, 5]))
    assert middle_node.value == 3
    assert middle_node.next_element.value == 4
    assert middle_node.next_element.next_element.value == 5
    assert middle_node.next_element.next_element.next_element is None

    middle_node = get_middle_node(create_linked_list([1, 2, 3, 4, 5, 6]))
    assert middle_node.value == 4
    assert middle_node.next_element.value == 5
    assert middle_node.next_element.next_element.value == 6
    assert middle_node.next_element.next_element.next_element is None
