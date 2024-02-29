"""Sample tests for 'tasks.factories' module."""
from tasks.factories import get_required_time


def test_get_required_time_sample():
    """Sample tests for get_required_time function."""
    # Example 1
    assert get_required_time([2, 4, 3], 10) == 10

    # Example 2
    assert get_required_time([1, 1, 3, 5], 11) == 5
