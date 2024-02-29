"""Templates for programming assignment: the heap sort algorithm."""
from typing import List


def min_heapify(data: List[int]) -> List[int]:
    """Returns the result of running the `heapify` (minimum) operation on a given array of numbers.

    What we know about the `heapify` operation:
    1) The expected time complexity of this operation is O(n), where n=|data|
    2) Here we're considering the "minimum" variation of `heapify`, so for the resulting array, the following
    conditions should hold (let's call the result array H):
        a) H[i] <= H[2 * i + 1], if 2 * i + 1 < n
        b) H[i] <= H[2 * i + 2], if 2 * i + 2 < n

    Basically the resulting array can be used as a base for the heap.

    Args:
        data: List[int], a given array of numbers to `heapify`
    Returns:
        List[int], the result of the `heapify` operation.
    """
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    
    return data

def heapify(arr: List[int], n: int, i: int):
    smallest = i         # Initialize smallest
    l = 2 * i + 1        # left = 2*i + 1
    r = 2 * i + 2        # right = 2*i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap

        heapify(arr, n, smallest)


def heap_sort(data: List[int]) -> List[int]:
    """Sorts a given array in ascending order using the heap sort algorithm.

    The idea is simple:
    1) First, use the `min_heapify` to get a heap
    2) Then, iteratively execute the `pop_minimum` operation (almost as in PriorityQueue.pop method) to create an ordered array

    NOTE: the expected time complexity is O(N * log N), where N=|data|

    Args:
        data: List[int], a given array to sort
    Returns:
        List[int], the ordered array
    """
    n = len(data)
    min_heapify(data)

    # Один за другим извлекаем наименьший элемент из кучи
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)
    
    # После завершения сортировки, элементы в массиве находятся в обратном порядке
    # Переворачиваем массив, чтобы получить правильный порядок
    data.reverse()
    
    return data