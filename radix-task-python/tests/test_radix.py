"""Sample tests for 'tasks.radix' module."""
from tasks.radix import radix_sort


def test_radix_sort_sample():
    """Sample tests for radix_sort function."""
    # Example 1
    assert radix_sort(
        array=["542", "124", "423", "142", "631", "624"],
        k=1
    ) == [1, 4, 3, 2, 0, 5]

    # Example 2
    assert radix_sort(
        array=["542", "124", "423", "142", "631", "624"],
        k=2
    ) == [4, 1, 0, 5, 3, 2]

    # Example 3
    assert radix_sort(
        array=["542", "124", "423", "142", "631", "624"],
        k=3
    ) == [3, 0, 2, 1, 5, 4]

    # Example 4
    assert radix_sort(
        array=["22", "32", "33", "11", "11"],
        k=1
    ) == [2, 3, 4, 0, 1]
