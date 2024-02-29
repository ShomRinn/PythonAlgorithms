# The Knuth-Morris-Pratt algorithm

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* The LPS array
* The KMP algorithm for matching strings
* Applying the KMP algorithm in practice

## Overview

The coding exercises cover the following practical problems:
* Building an LPS array for a given string
* Implementing the KMP algorithm
* Checking whether a given string is a tandem repeat

## Coding exercises

### Exercise 1: Build the LPS array for a given string

Your task is to implement the following function, which returns `the LPS array` for a given string:

```python
def build_lps_array(text: str) -> List[int]:
    """Returns the LPS array for a given string.

    Args:
        text: str, a given string
    Returns:
        List[int], the result LPS array.
    """
    pass
```


**Example 1:**

`text`='abracadabra'

Expected output: [0, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4]

**Example 2:**

`text`='abacaba'

Expected output: [0, 0, 1, 0, 1, 2, 3]

**Example 3:**

`text`='ababbaab'

Expected output: [0, 0, 1, 2, 0, 1, 1, 2]

<br>

Please use the template `tasks/kmp.py:build_lps_array` for the implementation.

### Exercise 2: Implementing the KMP algorithm

Your task is to implement the following function for matching strings using `the Knuth-Morris-Pratt algorithm`:

```python
def find_occurrences_via_kmp(text: str, pattern: str) -> List[int]:
    """Returns all positions within a given text where a given pattern occurs.

    NOTE: Please use the KMP algorithm.

    Args:
        text: str, the text to be search
        pattern: str, the pattern to search for
    Returns:
        List[int], all indices in the given text where the pattern occurs.
    """
    pass
```


**Example 1:**

`text`='hello world'

`pattern`='o'

Expected result: [4, 7]

**Example 2:**

`text`='abacaba'

`pattern`='aba'

Expected output: [0, 4]

**Example 3:**

`text`='ababbaab'

`pattern`='ab'

Expected output: [0, 2, 6]

**Example 4:**

`text`='ababbaab'

`pattern`='caba'

Expected output: []

<br>

Please use the template `tasks/kmp.py:find_occurrences_via_kmp` for the implementation.

### Exercise 3: Check whether a given string is a tandem repeat

A string `s` is called a tandem repeat if a non-empty string `t` (|`s`| > |`t`|) exists such that `s=t^k` (`s` is equal to string `t` concatenated `k` times) for a positive integer `k` (where `k>1`).

Your task is to implement the following function, which checks whether a given string is a tandem repeat:

```python
def is_tandem_repeat(text: str) -> bool:
    """Checks whether a given string is a tandem repeat.

    NOTE: The expected complexity is O(n), where n is the length of `text`.

    Args:
        text: str, a given string
    Returns:
        bool, whether a given string is a tandem repeat.
    """
    pass
```


**Example 1:**

`text`='abacaba'

Expected result: False

**Example 2:**

`text`='**aba**abaabaaba'

Expected output: True

Explanation: 'aba' is repeated 4 times. 'abaaba' also works here (it is repeated twice). 

**Example 3:**

`text`='**ab**abab'

Expected output: True

Explanation: 'ab' is repeated 3 times.

<br>

Please use the template `tasks/kmp.py:is_tandem_repeat` for the implementation.
