# 0-1 Knapsack Problem 

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:

* The 0-1 Knapsack Problem and its optimal substructure

## Overview

The coding exercises cover the following practical problems:
* Finding an optimal substructure matrix for a 0-1 knapsack problem
* Constructing an optimal solution using the optimal substructure matrix

## Coding exercises

### Exercise 1: Find the optimal substructure matrix for a 0-1 knapsack problem

Your task is to implement the following function for finding the optimal substructure given a `0-1 knapsack` problem definition:

```python
def get_optimal_substructure(weights: List[int], values: List[int], w: int) -> List[List[int]]:
    """Given parameters of 0-1 knapsack problem returns the optimal substructure matrix.

    The idea is to build a matrix F, where 
      F[i][j] - the maximum sum of values for some subset of packages among the first 'i' 
        packages, where their total weight does not exceed 'j'

    NOTE: sometimes you won't be able to fill in the matrix F completely, for all 
      'undefined' combinations of 'i' and 'j' just use 0 as a placeholder.

    NOTE: the result F is expected to have (N+1, w+1) shape, where N is the number of packages.

    NOTE: O(w * N) complexity is expected.

    Args:
        weights: List[int], the weights that correspond to available packages.
        values: List[int], the values that correspond to available packages.
        w: int, the given capacity of the knapsack.
    
    Returns:
        The optimal substructure matrix.
    """
    pass
```

**Example 1:**

`weights`=[2, 2]

`values`=[1, 2]

`w`=3

Expected result:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 2 & 2
\end{pmatrix}
```

**Example 2:**

`weights`=[1, 1, 1]

`values`=[1, 2, 3]

`w`=2

Expected result:
```math
\begin{pmatrix}
0 & 0 & 0 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
0 & 3 & 5
\end{pmatrix}
```

**Example 3:**

`weights`=[3, 2, 1, 4]

`values`=[1, 2, 1, 2]

`w`=6

Expected result:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 \\
0 & 0 & 2 & 2 & 2 & 3 & 3 \\
0 & 1 & 2 & 3 & 3 & 3 & 4 \\
0 & 1 & 2 & 3 & 3 & 3 & 4
\end{pmatrix}
```

<br>

Please use the template `tasks/knapsack:get_optimal_substructure` for the implementation.

### Exercise 2: Construct an optimal solution using the optimal substructure matrix

Your task is to implement the following function for constructing an optimal solution to the `0-1 knapsack` problem using the optimal substructure matrix:

```python
def get_optimal_solution(weights: List[int], optimal_substructure_matrix: List[List[int]]) -> List[int]:
    """Returns an optimal solution using the given list of weights and optimal substructure.

    NOTE: if there are multiple optimal solutions, feel free to return any of them.

    Args:
        weights: List[int], the weights that correspond to available packages.
        optimal_substructure: List[List[int]], the optimal substructure of the 0-1 knapsack problem previously 
            calculated using the `get_optimal_substructure` function.
    
    Returns:
        The optimal solution is represented by the binary vector (0/1 values), where 1 means
        that the corresponding package is included in the optimal solution and 0 otherwise.
    """
    pass
```

**Example 1:**

`weights`=[2, 2]

`optimal_substructure_matrix`:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 2 & 2
\end{pmatrix}
```

`values`=[1, 2]

`w`=3

Expected result: [0, 1] - the second package only (`best_value`=2).

**Example 2:**

`weights`=[1, 1, 1]

`optimal_substructure_matrix`:
```math
\begin{pmatrix}
0 & 0 & 0 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
0 & 3 & 5
\end{pmatrix}
```

`values`=[1, 2, 3]

`w`=2

Expected result: [0, 1, 1] - the second and the third packages (`best_value`=5).


**Example 3:**

`weights`=[3, 2, 1, 4]

`optimal_substructure_matrix`:
```math
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 \\
0 & 0 & 2 & 2 & 2 & 3 & 3 \\
0 & 1 & 2 & 3 & 3 & 3 & 4 \\
0 & 1 & 2 & 3 & 3 & 3 & 4
\end{pmatrix}
```

`values`=[1, 2, 1, 2]

`w`=6

Expected result: [1, 1, 1, 0] - the first three packages (`best_value`=4).

NOTE: [0, 1, 0, 1] also works here (the same total value - 4).

<br>

Please use the template `tasks/knapsack:get_optimal_solution` for the implementation.
