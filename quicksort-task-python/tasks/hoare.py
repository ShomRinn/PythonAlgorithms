"""Templates for programming assignment: Lamuto partitioning."""
from typing import List, Tuple


def hoare_partition(array: List[int], left_index: int, right_index: int) -> Tuple[int, int]:
    """Returns a partition index after Hoare partitioning and the number of swaps used.

    The idea is simple:
    * you need to partition a given array using the `middle` element
    * while partitioning, you need to keep track of the number of swaps required 
        (according to the pseudocode below)

    NOTE: refer to this pseudocode if necessary: https://www.baeldung.com/cs/algorithm-quicksort#2-hoare-partitioning
      The idea is to keep two pointers and gradually move them toward the center.

    NOTE: the expected time complexity is O(n), where n = right_index - left_index + 1
    NOTE: this function should work in-place

    Args:
        array: List[int], a given array to partition
        left_index: int, a starting index for partitioning
        right_index: int, an ending index for partitioning
    Returns:
        Tuple[int, int], the final position of the 'right' pointer just before partitioning 
        ('left' pointer >= 'right' pointer) and the number of swaps used
    """
    # pivoting element => array[(left_index + right_index) // 2]

    pivot = array[(left_index + right_index) // 2]
    i = left_index - 1
    j = right_index + 1
    swaps = 0

    while True:
        # Перемещаем левый указатель вправо пока элемент меньше опорного
        i += 1
        while array[i] < pivot:
            i += 1

        # Перемещаем правый указатель влево пока элемент больше опорного
        j -= 1
        while array[j] > pivot:
            j -= 1

        # Hазбиение завершено
        if i >= j:
            return j, swaps

        # Меняем элементы местами и учитываем перестановку
        array[i], array[j] = array[j], array[i]
        swaps += 1


def quicksort_hoare(array: List[int]) -> int:
    """Implements the quicksort algorithm with Hoare partitioning.
    
    NOTE: this function should work in-place
    
    Args:
        List[int], a given array to sort in ascending order
    Returns:
        int, the number of swaps used
    """
    def _quicksort(array: List[int], left_index: int, right_index: int) -> int:
        if left_index >= right_index:
            return 0 

        pivoting_index, swaps = hoare_partition(array, left_index, right_index)
        swaps += _quicksort(array, left_index, pivoting_index)
        swaps += _quicksort(array, pivoting_index + 1, right_index)
        return swaps

    total_swaps = _quicksort(
        array=array, 
        left_index=0,
        right_index=len(array) - 1
    )

    return total_swaps
