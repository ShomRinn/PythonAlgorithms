"""Template for programming assignment: the radix sort algorithm."""
from typing import List, Tuple


def radix_sort(array: List[str], k: int) -> List[int]:
    """Emulates a given number of iterations of the radix sort algorithm.

    NOTE: all elements of a given array are in string format but contain only "0"-"9" characters.
    NOTE: assume that all input elements have the same length d (k <= d).
    
    Args:
        array: List[str], a given list of 'integers' to order
        k: int, the required number of radix sort iterations
    Returns:
        List[int], the list of intermediate positions after `k` iterations.
    """
    array = [([int(c) for c in e], i) for i, e in enumerate(array)]
    for i in range(k):
        array.sort(key=lambda x: x[0][-i - 1])

    return [e[1] for e in sorted((e[1], i) for i, e in enumerate(array))]
