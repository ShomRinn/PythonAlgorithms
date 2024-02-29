"""Templates for programming assignment: Lamuto partitioning."""
from typing import List, Tuple


def lomuto_partition(array: List[int], left_index: int, right_index: int) -> Tuple[int, int]:
    """Returns a partition index after Lomuto partitioning and the number of swaps used.

    The idea is simple:
    * you need to partition a given array using the `right_index` element
    * `partition_index` (the first number that should be returned) should contain the last element
        of a given interval (the pivot itself), and all elements to the left of it should be strictly lower than the pivot
    * while partitioning, you need to keep track of the number of swaps required 
        (according to the pseudocode below)

    NOTE: refer to this pseudocode if necessary: https://www.baeldung.com/cs/algorithm-quicksort#1-lomuto-partitioning

    NOTE: the expected time complexity is O(n), where n = right_index - left_index + 1
    NOTE: this function should work in-place

    Args:
        array: List[int], a given array to partition
        left_index: int, the starting index for partitioning
        right_index: int, the ending index for partitioning
    Returns:
        Tuple[int, int], the index of the pivoting element after partitioning and 
            the number of swaps used
    """
    # pivoting element => array[right_index]
    pivot = array[right_index]
    i = left_index - 1
    swaps = 0

    for j in range(left_index, right_index):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            swaps += 1

    array[i + 1], array[right_index] = array[right_index], array[i + 1]
    swaps += 1
    return i + 1, swaps


def quicksort_lomuto(array: List[int]) -> int:
    """Implements the quicksort algorithm with Lomuto partitioning.
    
    NOTE: this function should work in-place
    
    Args:
        List[int], a given array to sort in ascending order
    Returns:
        int, the number of swaps used
    """
    def _quicksort(array: List[int], left_index: int, right_index: int) -> int:
        # if left_index >= right_index - return ...
        # pivoting_index, swaps = lomuto_partition(...)
        # swaps += _quicksort(...)
        # swaps += _quicksort(...)
        # return swaps
        if left_index >= right_index:
            return 0

        partition_index, swaps = lomuto_partition(array, left_index, right_index)
        swaps += _quicksort(array, left_index, partition_index - 1)
        swaps += _quicksort(array, partition_index + 1, right_index)
        return swaps

    total_swaps = _quicksort(
        array=array, 
        left_index=0,
        right_index=len(array) - 1
    )

    return total_swaps
