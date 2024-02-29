"""Sample tests for 'tasks.bucket' module."""
from tasks.bucket import bucket_sort


def test_bucket_sort_sample():
    """Sample tests for bucket_sort function."""
    # Example 1
    assert bucket_sort(
        patterns=["abc", "cab", "qaf", "cabg", "qwr", "qegtw"],
        prefix_length=1
    ) == [
        (0, 0), # "abc"
        (1, 0), # "cab"
        (3, 0), # "qaf"
        (2, 1), # "cabg"
        (5, 2), # "qwr"
        (4, 1), # "qegtw"
    ]

    # Example 2
    assert bucket_sort(
        patterns=["aaaba", "aaaa", "basfa", "badaa", "macda"],
        prefix_length=2
    ) == [
        (1, 1), # "aaaba"
        (0, 0), # "aaaa"
        (3, 1), # "basfa"
        (2, 0), # "badaa"
        (4, 0), # "macda"
    ]

    # Example 3
    assert bucket_sort(
        patterns=["aa", "bb", "aa", "bb", "aa"],
        prefix_length=1
    ) == [
        (0, 0), # "aa"
        (3, 0), # "bb"
        (1, 1), # "aa"
        (4, 1), # "bb"
        (2, 2), # "aa"
    ]
