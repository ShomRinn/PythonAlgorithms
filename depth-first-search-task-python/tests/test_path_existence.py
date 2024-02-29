"""Tests for 'tasks.path_existence' module."""
from tasks.path_existence import check_path_existence


def test_check_path_existence():
    """Tests for path_existence function."""
    assert not check_path_existence(5, {}, 0, 4)
    assert check_path_existence(5, {1: {0, 3}, 0: {2}, 3: {4}}, 1, 4)
    assert not check_path_existence(5, {1: {0, 3}, 0: {2}, 3: {4}}, 4, 1)
    assert check_path_existence(5, {4: {3}, 3: {2}, 2: {1}, 1: {0}}, 3, 0)
    assert not check_path_existence(5, {4: {3}, 3: {2}, 2: {1}, 1: {0}}, 0, 1)
