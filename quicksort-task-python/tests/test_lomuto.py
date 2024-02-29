"""Sample tests for 'tasks.lomuto' module."""
from tasks.lomuto import lomuto_partition, quicksort_lomuto


def test_quicksort_lomuto_sample():
    """Sample tests for lomuto_partition and quicksort_lomuto functions."""
    # Example 1
    array = [5, 3, 2, 1, 7, 4]
    assert lomuto_partition(array, 0, 5) == (3, 4)
    assert array == [3, 2, 1, 4, 7, 5]

    # Example 2
    array = [2, 5, 3, 1, 4]
    assert lomuto_partition(array, 0, 4) == (3, 4)
    assert array == [2, 3, 1, 4, 5]

    # Example 3
    array = [1, 2, 4, 5, 6, 3]
    assert lomuto_partition(array, 0, 5) == (2, 3)
    assert array == [1, 2, 3, 5, 6, 4]

    # Example 4
    array = [1, 2, 3, 4, 5]
    assert quicksort_lomuto(array) == 14
    assert array == [1, 2, 3, 4, 5]

    # Example 5
    array = [5, 4, 3, 2, 1]
    assert quicksort_lomuto(array) == 8
    assert array == [1, 2, 3, 4, 5]

    # Example 6
    array = [5, 3, 2, 7, 5, 9]
    assert quicksort_lomuto(array) == 11
    assert array == [2, 3, 5, 5, 7, 9]
