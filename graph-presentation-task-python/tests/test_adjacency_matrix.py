"""Tests for 'tasks.adjacent_list_using_dict' module."""
import random
import pytest

from tasks.adjacency_matrix import GraphAdjacencyMatrix


@pytest.mark.timeout(2)
def test_adjacency_matrix_sample():
    """Tests for adjacency matrix class."""
    num_of_vertices = 5
    graph = GraphAdjacencyMatrix(num_of_vertices)

    assert graph.get_number_of_adjacent_vertices(0) == 0

    for vertex in range(4):
        graph.add_new_edge(vertex, vertex+1)

    assert graph.get_number_of_adjacent_vertices(0) == 1
    assert graph.get_number_of_adjacent_vertices(1) == 2

    for vertex in range(4):
        assert graph.is_edge(vertex, vertex+1) == True

    # Pop when stack is empty.
    assert graph.is_edge(0, 4) == False
