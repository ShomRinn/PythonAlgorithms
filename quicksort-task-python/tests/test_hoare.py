"""Sample tests for 'tasks.hoare' module."""
from tasks.hoare import hoare_partition, quicksort_hoare


def test_quicksort_hoare_sample():
    """Sample tests for hoare_partition and quicksort_hoare functions."""
    # Example 1
    array = [1, 5, 3, 2, 4]
    assert hoare_partition(array, 0, 4) == (2, 1)
    assert array == [1, 2, 3, 5, 4]

    # Example 2
    array = [6, 5, 4, 3, 2, 1]
    assert hoare_partition(array, 0, 5) == (2, 3)
    assert array == [1, 2, 3, 4, 5, 6]

    # Example 3
    array = [6, 5, 4, 3, 2, 1]
    assert quicksort_hoare(array) == 3
    assert array == [1, 2, 3, 4, 5, 6]

    # Example 4
    array = [5, 3, 2, 7, 5, 9]
    assert quicksort_hoare(array) == 3
    assert array == [2, 3, 5, 5, 7, 9]

    # Example 5
    array = [6, 6, 1, 8, 3, 1, 7, 4, 2]
    assert quicksort_hoare(array) == 8
    assert array == [1, 1, 2, 3, 4, 6, 6, 7, 8]
