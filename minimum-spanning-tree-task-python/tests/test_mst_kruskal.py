"""Tests for 'tasks.mst_prim' module."""
from tasks.mst_kruskal import kruskal_mst


def test_kruskal_mst():
    """Tests for kruskal_mst function."""
    assert kruskal_mst(5, [[0, 1, 1], [0, 2, 1], [2, 3, 5], [0, 3, 1], [2, 4, 7], [3, 4, 5]]) == 8
    assert kruskal_mst(5, [[0, 1, 1], [0, 2, 1], [2, 3, 5], [0, 3, 1]]) is None
    assert kruskal_mst(3, [[1, 0, 5], [2, 0, 10], [1, 2, 6]]) == 11
    assert kruskal_mst(3, [[1, 0, 5], [2, 0, 10]]) == 15
