"""Tests for 'tasks.mst_prim' module."""
from tasks.mst_prim import prim_mst


def test_prim_mst():
    """Tests for prim_mst function."""
    assert prim_mst(5, [[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]]) == ([0, 1, 2, 4, 3], 16)
    assert prim_mst(5, [[0, 2, 0, 6, 0], [2, 0, 3, 8, 0], [0, 3, 0, 0, 0], [6, 8, 0, 0, 0], [0, 0, 0, 0, 0]]) == (None, None)
    assert prim_mst(3, [[0, 10, 5], [10, 0, 6], [5, 6, 0]]) == ([0, 2, 1], 11)
