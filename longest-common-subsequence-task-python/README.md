# The Longest Common Subsequence (LCS) problem 

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:

* The LCS problem and its optimal substructure

## Overview

The coding exercises cover the following practical problems:
* Finding the optimal substructure matrix for the LCS problem
* Constructing the optimal solution using the optimal substructure matrix for the LCS problem

## Coding exercises

### Exercise 1: Find the optimal substructure matrix for the LCS problem

Your task is to implement the following function for finding the optimal substructure given an `LCS` problem definition:

```python
def get_optimal_substructure(string_a: str, string_b: str) -> List[List[int]]:
    """Returns the LCS optimal substructure using the two strings 'a' and 'b'.

    The idea is to build a matrix F, where 
      F[i][j] - maximum length of the common subsequence for the first 'i' characters of the first string,
      and the first 'j' characters of the second string

    NOTE: the result F is expected to have (N+1, M+1) shape, where N and M are the lengths of the given strings.

    NOTE: O(N * M) complexity is expected.

    Args:
        string_a: str, the first string.
        string_b: str, the second string.
    
    Returns:
        The optimal substructure matrix for the given LCS problem.
    """
    pass
```

**Example 1:**

`string_a`='aa'

`string_b`='ab'

Expected result:
```math
\begin{pmatrix}
0 & 0 & 0 \\
0 & 1 & 1 \\
0 & 1 & 1
\end{pmatrix}
```

**Example 2:**

`string_a`='aaa'

`string_b`='aba'

Expected result:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 1 & 1 & 2 \\
0 & 1 & 1 & 2
\end{pmatrix}
```

**Example 3:**

`string_a`='ababab'

`string_b`='accabcc'

Expected result:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
0 & 1 & 1 & 1 & 1 & 2 & 2 & 2\\
0 & 1 & 1 & 1 & 2 & 2 & 2 & 2\\
0 & 1 & 1 & 1 & 2 & 3 & 3 & 3\\
0 & 1 & 1 & 1 & 2 & 3 & 3 & 3\\
0 & 1 & 1 & 1 & 2 & 3 & 3 & 3
\end{pmatrix}
```

<br>

Please use the template `tasks/lcs:get_optimal_substructure` for the implementation.

### Exercise 2: Construct the optimal solution using the optimal substructure matrix

Your task is to implement the following function for constructing the optimal solution to the `LCS` problem with the optimal substructure matrix:

```python
def get_optimal_solution(string_a: str, optimal_substructure_matrix: List[List[int]]) -> str:
    """Given an optimal substructure matrix, the first string returns the optimal solution to the LCS problem.

    NOTE: if there are multiple optimal solutions, feel free to return any of them.

    Args:
        string_a: str, the first string.
        optimal_substructure: List[List[int]], optimal substructure of the LCS problem previously calculated using the `get_optimal_substructure` function.
    
    Returns:
        Str, the optimal solution to the LCS problem.
    """
    pass
```

**Example 1:**

`string_a`='aa'

`optimal_substructure_matrix`:
```math
\begin{pmatrix}
0 & 0 & 0 \\
0 & 1 & 1 \\
0 & 1 & 1
\end{pmatrix}
```

Expected result: 'a'.

**Example 2:**

`string_a`='aaa'

`optimal_substructure_matrix`:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 1 & 1 & 2 \\
0 & 1 & 1 & 2
\end{pmatrix}
```

Expected result: 'aa'.

**Example 3:**

`string_a`='ababab'

`optimal_substructure_matrix`:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
0 & 1 & 1 & 1 & 1 & 2 & 2 & 2\\
0 & 1 & 1 & 1 & 2 & 2 & 2 & 2\\
0 & 1 & 1 & 1 & 2 & 3 & 3 & 3\\
0 & 1 & 1 & 1 & 2 & 3 & 3 & 3\\
0 & 1 & 1 & 1 & 2 & 3 & 3 & 3
\end{pmatrix}
```

Expected result: 'aab'.

<br>

Please use the template `tasks/lcs:get_optimal_solution` for the implementation.
