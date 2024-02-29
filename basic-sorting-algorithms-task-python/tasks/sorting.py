"""Templates for programming assignments: the basic sorting algorithms."""

from typing import List


def partial_selection_sort(data: List[int], k: int) -> List[int]:
    """Returns the partially sorted array after 'k' iterations of the Selection Sort algorithm.

    NOTE: after the first 'i' iterations - the first 'i+1' elements of the array should be ordered.  
    NOTE: 0 <= k < |data| 

    Args:
        data: List[int], a given list of values to order.
        k: int, the required number of selection sort iterations
    Returns:
        List[int], the result partially sorted array.
    """
    n = len(data)
    k = min(k, n)

    for i in range(k):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

    return data

def partial_insertion_sort(data: List[int], k: int) -> List[int]:
    """Returns the partially sorted array after 'k' iterations of the Insertion Sort algorithm.

    NOTE: after the first 'i' iterations - the first 'i+1' elements of the array should be ordered.  
    NOTE: 0 <= k < |data| 

    Args:
        data: List[int], a given list of values to order.
        k: int, the required number of insertion sort iterations
    Returns:
        List[int], the result partially sorted array.
    """
    n = len(data)

    for i in range(1, min(k, n - 1) + 1):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


def partial_bubble_sort(data: List[int], k: int) -> List[int]:
    """Returns the intermediate state of a given array after 'k' swaps of the Bubble Sort algorithm.

    NOTE: if 'k' exceeds the number of swaps required (and an array can be sorted
    in less than 'k' swaps) - just ignore the other 'potential' swaps and return the sorted array.

    Args:
        data: List[int], a given list of values to order.
        k: int, the required number of bubble sort swaps
    Returns:
        List[int], the result intermediate array after 'k' swaps.
    """
    n = len(data)
    swaps_done = 0

    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps_done += 1

                if swaps_done == k:
                    return data

    return data
