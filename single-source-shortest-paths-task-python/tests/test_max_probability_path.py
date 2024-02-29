"""Tests for 'tasks.max_probability_path' module."""
from tasks.max_probability_path import get_max_probability_path


def check_ans(x, y):
    return x - y < 1e-5


def test_get_max_probability_path():
    """Tests for get_max_probability_path function."""
    assert check_ans(get_max_probability_path(3, {0: {(1, 0.5), (2, 0.2)},
                                                  1: {(0, 0.5), (2, 0.5)},
                                                  2: {(0, 0.2), (1, 0.5)}},
                                              0, 2), 0.25)
    assert check_ans(get_max_probability_path(3, {0: {(1, 0.5), (2, 0.3)},
                                                  1: {(0, 0.5), (2, 0.5)},
                                                  2: {(0, 0.3), (1, 0.5)}},
                                              0, 2), 0.3)
    assert check_ans(get_max_probability_path(3, {0: {(1, 0.5)},
                                                  1: {(0, 0.5)}},
                                              0, 2), 0)
    assert check_ans(get_max_probability_path(5, {0: {(1, 0.5)},
                                                  1: {(0, 0.5), (2, 0.5), (3, 0.2)},
                                                  2: {(1, 0.5), (3, 0.5)},
                                                  3: {(1, 0.2), (2, 0.5), (4, 0.5)},
                                                  4: {(3, 0.5)}},
                                              0, 4), 0.0625)

