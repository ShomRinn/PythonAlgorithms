"""Sample tests for 'tasks.naive' module."""
from tasks.naive import find_occurrences


def test_find_occurrences_sample():
    """Tests for find_occurrences function."""
    assert find_occurrences("abababa", "aba") == [0, 2, 4]
    assert find_occurrences("question", "answer") == []
    assert find_occurrences("Who’s there? Figs. Figs who? Figs the doorbell, it’s not working!", "Figs") == [13, 19, 29]
