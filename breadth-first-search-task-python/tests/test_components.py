"""Tests for 'tasks.components' module."""
from tasks.components import find_number_of_components


def test_find_number_of_components():
    """Tests for find_number_of_components function."""
    assert find_number_of_components(5, {}) == 5
    assert find_number_of_components(10, {}) == 10
    assert find_number_of_components(10, {0: {6, 7}, 6: {0, 7}, 7: {0, 6}}) == 8
    assert find_number_of_components(5, {1: {0, 2}, 0: {1}, 2: {0}}) == 3
    assert find_number_of_components(5, {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 0}}) == 1
