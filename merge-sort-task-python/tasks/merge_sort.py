"""Templates for programming assignments: the merge sort algorithm."""
from typing import List, Tuple


def merge_sorted_subarrays(
    data: List[int],
    left_index: int,
    middle_index: int,
    right_index: int,
):
    """Merges two sorted subarrays of a given list (in-place).
    
    Assume the first ordered subarray is within the [left_index; middle_index] interval
    and the second subarray is within the (middle_index; right_index] interval.

    NOTE: even though this function should work in-place, you can use up to O(n) auxiliary space,
        where n = right_index - left_index + 1
    NOTE: the expected time complexity is O(n), where n = right_index - left_index + 1

    Args:
        data: List[int], a given list that contains two subarrays for merging
        left_index: int, defines the left bound of the first subarray
        middle_index: int, defines the right bound of the first subarray
        right_index: int, defines the right bound of the second subarray
    """
    n1 = middle_index - left_index + 1  # Length of the first subarray
    n2 = right_index - middle_index     # Length of the second subarray

    # Creating temporary arrays
    L = data[left_index:middle_index + 1]
    R = data[middle_index + 1:right_index + 1]

    # Initial indexes of first and second subarrays
    i = 0
    j = 0
    
    # Initial index of merged subarray
    k = left_index

    # Merging the temp arrays back into data[left_index:right_index+1]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1

    # Copying the remaining elements of L[], if there are any
    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    # Copying the remaining elements of R[], if there are any
    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1


def merge_sort_algorithm(data: List[int]) -> Tuple[List[int], int]:
    """Returns the sorted array and a `special statistic` that will be defined below.

    The idea is simple: You use the merge sort algorithm to order a given array, and that's it.
    The algorithm is simple: You divide the current subarray, sort both parts, and then merge them.
    
    NOTE: The statistic you need to calculate has the following definition:
    * At the beginning of the algorithm `statistic=0`
    * Each time you use the `merge_sorted_subarrays` function, you should do the following BEFORE and AFTER each call:
        * `statistic += data[left_index]`
        * `statistic += data[middle_index]` (even if left_index == middle_index)
        * `statistic += data[right_index]`
    Ask yourself, "But why?" You know, just to avoid silly stuff like "return sorted(data)".

    NOTE: you are expected to implement `merge_sorted_subarrays` before starting with this function
    NOTE: the expected time complexity is O(n * log n), where n=|data|

    Args:
        data: List[str], a given list of elements to sort (in ascending order)
    Returns:
        Tuple[List[int], int], the sorted array and the `statistic` defined above.
    """
    def _merge_sort(left_index: int, right_index: int) -> int:
        """Sorts a given subarray and returns the corresponding `statistic`."""

        statistic = 0
        if left_index < right_index:
            # Don't change this!
            middle_index = (left_index + right_index) // 2

            # Sorting first and second halves
            statistic += _merge_sort(left_index, middle_index)
            statistic += _merge_sort(middle_index + 1, right_index)

            # Calculating statistic before merge
            statistic += data[left_index] + data[middle_index] + data[right_index]

            # Merging the sorted halves
            merge_sorted_subarrays(data, left_index, middle_index, right_index)

            # Calculating statistic after merge
            statistic += data[left_index] + data[middle_index] + data[right_index]

        return statistic

    result_statistic = _merge_sort(0, len(data) - 1)
    return data, result_statistic
