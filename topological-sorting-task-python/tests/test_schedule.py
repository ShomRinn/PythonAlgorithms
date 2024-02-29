"""Tests for 'tasks.longest_path' module."""
from tasks.schedule import find_task_order


def check_order(n, dependencies, order):
    positions = [0 for _ in range(n)]
    for ind in range(len(order)):
        positions[order[ind]] = ind
    for dependency in dependencies:
        if positions[dependency[0]] > positions[dependency[1]]:
            return False
    return True


def test_find_the_longest_path_in_dag():
    """Tests for find_task_order function."""
    assert check_order(5, [(1, 0), (3, 0), (0, 4)], find_task_order(5, [(1, 0), (3, 0), (0, 4)]))
    assert check_order(5, [(0, 1), (1, 2), (2, 3), (3, 4)], find_task_order(5, [(0, 1), (1, 2), (2, 3), (3, 4)]))
    assert check_order(6, [(2, 5), (5, 3), (3, 1), (1, 4), (3, 0)], find_task_order(6, [(2, 5), (5, 3), (3, 1), (1, 4), (3, 0)]))
