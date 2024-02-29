# Bucket and Radix sorting algorithms

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The bucket sort algorithm
* The radix sort algorithm

## Overview

The coding exercises cover the following practical problems:
* Implementing the bucket sort algorithm
* Implementing the radix sort algorithm


## Coding exercises

### Exercise 1: Implement the bucket sort algorithm

Your task is to implement the following function, which emulates the bucket sort algorithm:

```python
def bucket_sort(patterns: List[str], prefix_length: int) -> List[Tuple[int, int]]:
    """Orders a given array of strings using bucket sort.

    NOTE: for bucketing purposes, you need to use the first `prefix_length` characters of each input pattern.
    Example 1: 
    | patterns = ["aa", "ab", "ba", "bb", "bbac"], prefix_length=1
    | buckets = {"a": ["aa", "ab"], "b": ["ba", "bb", "bbac"]}

    Example 2: 
    | patterns = ["aa", "ab", "ba", "bb", "bbac"], prefix_length=2
    | There will be four buckets (two patterns in the bucket "bb").

    NOTE: for each input pattern, you should return two things:
    * the final positions of patterns after bucket sort
    * the positions of patterns in corresponding buckets after ordering within buckets
    
    Args:
        patterns: List[str], a given list of patterns to order
        prefix_length: int, a parameter that should be used to bucket patterns
    Returns:
        List[Tuple[int, int]], positions that correspond to given patterns both globally and 
            within individual buckets
    """
    pass
```

**Example 1:**

`patterns`=["abc", "cab", "qaf", "cabg", "qwr", "qegtw"]

`prefix_length`=1

Expected result: [ <br>
    (0, 0), # "abc" <br>
    (1, 0), # "cab" <br>
    (3, 0), # "qaf" <br>
    (2, 1), # "cabg" <br>
    (5, 2), # "qwr" <br>
    (4, 1), # "qegtw" <br>
]

Explanation: there will be three buckets (the patterns are already ordered):
* "a": ["abc"]
* "c": ["cab", "cabg"]
* "q": ["qaf", "qegtw", "qwr"]


**Example 2:**

`patterns`=["aaaba", "aaaa", "basfa", "badaa", "macda"]

`prefix_length`=2

Expected result: [ <br>
    (1, 1), # "aaaba" <br>
    (0, 0), # "aaaa" <br>
    (3, 1), # "basfa" <br>
    (2, 0), # "badaa" <br>
    (4, 0), # "macda" <br>
]

Explanation: there will be three buckets (the patterns are already ordered):
* "aa": ["aaaa", "aaaba"]
* "ba": ["badaa", "basfa"]
* "ma": ["macda"]


**Example 3:**

`patterns`=["aa", "bb", "aa", "bb", "aa"]

`prefix_length`=1

Expected result: [ <br>
    (0, 0), # "aa" <br>
    (3, 0), # "bb" <br>
    (1, 1), # "aa" <br>
    (4, 1), # "bb" <br>
    (2, 2), # "aa" <br>
]

Explanation: there will be two buckets (the patterns are already ordered):
* "a": ["aa", "aa", "aa"]
* "b": ["bb", "bb"]


<br>

Please use the template `tasks/bucket.py:bucket_sort` for the implementation.


### Exercise 2: Implement the radix sort algorithm

Your task is to implement the following function, which returns intermediate indices of given elements after `k` iterations of the radix sort algorithm:

```python
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
    pass
```

**Example 1:**

`array`=["542", "124", "423", "142", "631", "624"]

`k`=1

Expected result: [1, 4, 3, 2, 0, 5]

Explanation: 

After the first iteration, the numbers will be ordered as follows:
* ["631", "542", "142", "423", "124", "624"]
* "542" has index `1`
* "123" has index `4`
* "423" has index `3`, etc.


**Example 2:**

`array`=["542", "124", "423", "142", "631", "624"]

`k`=2

Expected result: [4, 1, 0, 5, 3, 2]

Explanation: 

After the second iteration, the numbers will be ordered as follows:
* ["423", "124", "624", "631", "542", "142"]


**Example 3:**

`array`=["542", "124", "423", "142", "631", "624"]

`k`=3

Expected result: [3, 0, 2, 1, 5, 4]

Explanation: 

After the third (final) iteration, the numbers will be ordered as follows:
* ["124", "142", "423", "542", "624", "631"]


**Example 4:**

`array`=["22", "32", "33", "11", "11"]

`k`=1

Expected result: [2, 3, 4, 0, 1]

Explanation: 

After the third (final) iteration, the numbers will be ordered as follows:
* ["11", "11", "22", "32", "33"]

<br>

Please use the template `tasks/radix.py:radix_sort` for the implementation.
