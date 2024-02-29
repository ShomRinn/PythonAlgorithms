"""Tests for 'tasks.all_pairs_shortest_paths' module."""
from tasks.all_pairs_shortest_paths import get_sum_of_all_pairs_shortest_paths


def test_get_sum_of_all_pairs_shortest_paths():
    """Tests for get_sum_of_all_pairs_shortest_paths function."""
    assert get_sum_of_all_pairs_shortest_paths(5, [[0, 2, 0, 6, 0],
                                                   [2, 0, 3, 8, 5],
                                                   [0, 3, 0, 0, 7],
                                                   [6, 8, 0, 0, 9],
                                                   [0, 5, 7, 9, 0]]) == (126, 0)
    assert get_sum_of_all_pairs_shortest_paths(5, [[0, 2, 0, 6, 0],
                                                   [2, 0, 3, 8, 0],
                                                   [0, 3, 0, 0, 0],
                                                   [6, 8, 0, 0, 0],
                                                   [0, 0, 0, 0, 0]]) == (70, 8)
    assert get_sum_of_all_pairs_shortest_paths(3, [[0, 10, 5],
                                                   [10, 0, 6],
                                                   [5, 6, 0]]) == (42, 0)
