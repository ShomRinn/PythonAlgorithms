"""Tests for 'tasks.shortest_path_with_negatives' module."""
from tasks.shortest_path_with_negatives import find_shortest_path_cost


def test_find_shortest_path_cost():
    """Tests for find_shortest_path_cost function."""
    assert find_shortest_path_cost(3, {0: {(1, 5), (2, 2)},
                                       1: {(0, 5), (2, 2)},
                                       2: {(0, 2), (1, 2)}},
                                   0) == (6, 0)
    assert find_shortest_path_cost(2, {0: {(1, -1)},
                                       1: {(0, -2)}},
                                   1) == (None, None)
    assert find_shortest_path_cost(3, {0: {(1, 3), (2, -7)},
                                       1: {(0, 5), (2, -1)}},
                                   1) == (3, 0)
    assert find_shortest_path_cost(4, {0: {(1, 3), (2, 7)},
                                       1: {(2, 5)},
                                       2: {(3, 5)}},
                                   1) == (15, 1)
    assert find_shortest_path_cost(4, {0: {(1, 3), (2, 7)},
                                       1: {(2, 5)},
                                       2: {(3, 5)}},
                                   0) == (22, 0)
