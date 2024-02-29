# The Quicksort algorithm

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The quicksort algorithm
* Lomuto partitioning
* Hoare partitioning

## Overview

The coding exercises cover the following practical problems:
* Implementing the quicksort algorithm with Lomuto partitioning
* Implementing the quicksort algorithm with Hoare partitioning

## Coding exercises

### Exercise 1: Quicksort (Lomuto Partitioning)

Your task is to implement the following functions to get the quicksort algorithm with Lomuto partitioning:

```python
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
    pass


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
        pass

    total_swaps = _quicksort(
        array=array, 
        left_index=...,
        right_index=...
    )

    return total_swaps
```


**Example 1:**

`lomuto_partition([5, 3, 2, 1, 7, 4], 0, 5)`

Expected result:
* `partition_index`=3
* `swaps`=4

Explanation:
* 1-st swap: Indices 0 and 1
  * Array after the swap: [**3**, **5**, 2, 1, 7, 4]
* 2-nd swap: Indices 1 and 2
  * Array after the swap: [3, **2**, **5**, 1, 7, 4]
* 3-rd swap: Indices 2 and 3
  * Array after the swap: [3, 2, **1**, **5**, 7, 4]
* 4-th swap: Indices 3 and 5
  * Array after the swap: [3, 2, 1, **4**, 7, **5**]

**Example 2:**

`lomuto_partition([2, 5, 3, 1, 4], 0, 4)`

Expected result:
* `partition_index`=3
* `swaps`=4

Explanation:
* 1-st swap: Indices 0 and 0 (!!!)
  * Array after the swap: [**2**, 5, 3, 1, 4]
* 2-nd swap: Indices 1 and 2
  * Array after the swap: [2, **3**, **5**, 1, 4]
* 3-rd swap: Indices 2 and 3
  * Array after the swap: [2, 3, **1**, **5**, 4]
* 4-th swap: Indices 3 and 4
  * Array after the swap: [2, 3, 1, **4**, **5**]

**Example 3:**

`lomuto_partition([1, 2, 4, 5, 6, 3], 0, 5)`

Expected result:
* `partition_index`=2
* `swaps`=3

Explanation:
* 1-st swap: Indices 0 and 0 (!!!)
  * Array after the swap: [**1**, 2, 4, 5, 6, 3]
* 2-nd swap: Indices 1 and 1 (!!!)
  * Array after the swap: [1, **2**, 4, 5, 6, 3]
* 3-rd swap: Indices 2 and 5
  * Array after the swap: [1, 2, **3**, 5, 6, **4**]

**Example 4:**

`quicksort_lomuto([1, 2, 3, 4, 5])`

Expected result:
* `array`=[1, 2, 3, 4, 5]
* `swaps`=14

**Example 5:**

`quicksort_lomuto([5, 4, 3, 2, 1])`

Expected result:
* `array`=[1, 2, 3, 4, 5]
* `swaps`=8

**Example 6:**

`quicksort_lomuto([5, 3, 2, 7, 5, 9])`

Expected result:
* `array`=[2, 3, 5, 5, 7, 9]
* `swaps`=11

<br>


Please use the templates`tasks/lomuto.py:lomuto_partition+quicksort_lomuto` for the implementation.


### Exercise 2: Quicksort (Hoare partitioning)

Your task is to implement the following functions to get the quicksort algorithm with Hoare partitioning:

```python
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
    pass


def quicksort_hoare(array: List[int]) -> int:
    """Implements the quicksort algorithm with Hoare partitioning.
    
    NOTE: this function should work in-place
    
    Args:
        List[int], a given array to sort in ascending order
    Returns:
        int, the number of swaps used
    """
    def _quicksort(array: List[int], left_index: int, right_index: int) -> int:
        # if left_index >= right_index - return ...
        # pivoting_index, swaps = hoare_partition(...)
        # swaps += _quicksort(...)
        # swaps += _quicksort(...)
        # return swaps
        pass

    total_swaps = _quicksort(
        array=array, 
        left_index=...,
        right_index=...
    )

    return total_swaps
```


**Example 1:**

`hoare_partition([1, 5, 3, 2, 4], 0, 4)`

Expected result:
* `partition_index`=2
* `swaps`=1

Explanation:
* 1-st swap: Indices 1 and 3
  * Array after the swap: [1, **2**, 3, **5**, 4]

**Example 2:**

`hoare_partition([6, 5, 4, 3, 2, 1], 0, 5)`

Expected result:
* `partition_index`=2
* `swaps`=3

Explanation:
* 1-st swap: Indices 0 and 5
  * Array after the swap: [**1**, 5, 4, 3, 2, **6**]
* 2-nd swap: Indices 1 and 4
  * Array after the swap: [1, **2**, 4, 3, **5**, 6]
* 3-rd swap: Indices 2 and 3
  * Array after the swap: [1, 2, **3**, **4**, 5, 6]

**Example 3:**

`quicksort_hoare([6, 5, 4, 3, 2, 1])`

Expected result:
* `array`=[1, 2, 3, 4, 5, 6]
* `swaps`=3

**Example 4:**

`quicksort_hoare([5, 3, 2, 7, 5, 9])`

Expected result:
* `array`=[2, 3, 5, 5, 7, 9]
* `swaps`=3

**Example 5:**

`quicksort_hoare([6, 6, 1, 8, 3, 1, 7, 4, 2])`

Expected result:
* `array`=[1, 1, 2, 3, 4, 6, 6, 7, 8]
* `swaps`=8
<br>

Please use the templates `tasks/lomuto.py:hoare_partition+quicksort_hoare` for the implementation.
