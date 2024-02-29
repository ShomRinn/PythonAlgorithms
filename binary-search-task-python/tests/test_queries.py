"""Sample tests for 'tasks.queries' module."""
from tasks.queries import process_queries


def test_process_queries_sample():
    """Sample tests for process_queries function."""
    # Example 1
    assert process_queries(
        [0, 1, 2, 4, 6, 1000],
        [(-100, 3), (5, 5), (1, 4)]
    ) == [3, 0, 3]

    # Example 2
    assert process_queries(
        [0, 0, 1, 1, 2],
        [(0, 1), (1, 2), (-5, 10)]
    ) == [4, 3, 5]
