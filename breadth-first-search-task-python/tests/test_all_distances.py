"""Tests for 'tasks.components' module."""
import pytest

from tasks.all_distances import calculate_all_distances_from_vertex


@pytest.mark.timeout(6)
def test_calculate_all_distances_from_vertex():
    """Tests for find_number_of_components function."""
    assert calculate_all_distances_from_vertex(5, {}, 1) == [-1, 0, -1, -1, -1]
    assert calculate_all_distances_from_vertex(5, {1: {0}, 0: {2, 1}, 2: {0}}, 2) == [1, 2, 0, -1, -1]
    assert calculate_all_distances_from_vertex(5, {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 0}}, 4) == [1, 2, 2, 1, 0]
