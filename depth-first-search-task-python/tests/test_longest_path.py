"""Tests for 'tasks.longest_path' module."""
from tasks.longest_path import find_the_longest_path_in_dag


def test_find_the_longest_path_in_dag():
    """Tests for find_number_of_components function."""
    assert find_the_longest_path_in_dag(5, {}) == 0
    assert find_the_longest_path_in_dag(5, {1: {0, 3}, 0: {2}, 3: {4}}) == 2
    assert find_the_longest_path_in_dag(5, {4: {3}, 3: {2}, 2: {1}, 1: {0}}) == 4
    assert find_the_longest_path_in_dag(6, {0: {1, 3}, 1: {2}, 2: {5}, 3: {4}, 5: {3}}) == 5
