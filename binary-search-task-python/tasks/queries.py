"""Template for programming assignment: Interval Queries."""
from typing import List, Tuple


def process_queries(array: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """Returns answers for a given set of queries.

    Each query is represented by two numbers: (left, right).
    The answer for a given query is the number of elements in a given array 
    with values in the interval [left, right].

    NOTE: the expected time complexity per query is O(log N), where N=|array|.
    NOTE: the expected time complexity is O(Q * log N), where Q=|queries|.

    Args:
        List[int], a given sorted array
        List[Tuple[int, int]], a given set of queries
    Returns:
        The answers that correspond to a given set of queries
    """
    def binary_search(arr, target, findFirst):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if (findFirst and arr[mid] < target) or (not findFirst and arr[mid] <= target):
                left = mid + 1
            else:
                right = mid - 1
        return left

    result = []
    for left, right in queries:
        left_index = binary_search(array, left, True)
        right_index = binary_search(array, right, False)
        result.append(right_index - left_index)

    return result
