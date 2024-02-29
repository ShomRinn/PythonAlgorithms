"""Tests for 'tasks.bipartite_graph' module."""
from tasks.bipartite_graph import check_bipartite_graph


def test_check_bipartite_graph():
    """Tests for check_bipartite_graph function."""
    assert not check_bipartite_graph(5, {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 0}})
    assert check_bipartite_graph(5, {0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3}})
    assert not check_bipartite_graph(6, {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 4}, 3: {0, 5}, 4: {1,2}, 5: {3}})
    assert check_bipartite_graph(6, {0: {1, 3}, 1: {0, 2, 5}, 2: {1, 4}, 3: {0, 5}, 4: {2, 5}, 5: {1, 3, 4}})
