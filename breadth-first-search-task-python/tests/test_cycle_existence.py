"""Tests for 'tasks.components' module."""
from tasks.cycle_existence import check_cycle_existence


def test_cycle_existence():
    """Tests for find_number_of_components function."""
    assert not check_cycle_existence(5, {})
    assert check_cycle_existence(10, {0: {6, 7}, 6: {0, 7}, 7: {0, 6}})
    assert not check_cycle_existence(5, {1: {0}, 0: {2, 1}, 2: {0}})
    assert check_cycle_existence(5, {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 0}})
