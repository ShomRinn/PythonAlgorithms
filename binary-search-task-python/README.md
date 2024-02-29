# Binary Search

## Purpose

The coding exercises are designed to test your knowledge of the following concept:

* Binary search

## Overview

The coding exercises cover the following practical problems:
* Guessing a secret number
* Finding the minimum time to produce a given amount of product
* Finding the number of elements in an array in a given interval

## Coding exercises

### Exercise 1: Guess a secret number

Suppose you have a black box:

```python
class BlackBox:
    """Mysterious class."""

    ...

    def guess(self, value: int) -> int:
        """Evaluates a given guess."""
        #
        # if `value` == `secret_number`:
        #     return 0
        # if `value` < `secret_number`:
        #     return -1
        # if `value` == `secret_number`:
        #     return 1
        #

    ...
```

As you can see, a black box has the method `guess`, which accepts and evaluates guesses:
* it returns `0` if you guess correctly (in this case, your job is done)
* it returns `-1` if your guess is too low
* it returns `1` if your guess is too high

Your task is to implement the following function, which guesses a secret number in a black box:

```python
def guess_number(left_bound: int, right_bound: int, black_box: "BlackBox") -> int:
    """Returns the secret number based on a given black box.

    NOTE:
    * the secret number lies in the [left_bound, right_bound] interval
    * you interact with a given black box to guess the secret number
    * the only assumption you can have about a black box is that is has a `.guess` method
    * don't try to guess in which attribute the secret number is stored within a given black box ;)
    * trying all the numbers in [left_bound, right_bound] will be too slow to pass the hidden tests

    Args:
        left_bound: int, the left bound while guessing
        right_bound: int, the right bound while guessing
        black_box: "BlackBox", some object with a `.guess` method available
    Returns:
        int, the secret number.
    """
    pass
```

**Example 1:**

`secret_number`=5

`left_bound`=1

`right_bound`=10

Expected result:

`black_box.guess(10)` # 1

`black_box.guess(3)` # -1

`black_box.guess(1)` # -1

`black_box.guess(9)` # 1

`black_box.guess(5)` # 0 - Wow, you guessed correctly!


**Example 2:**

`secret_number`=9

`left_bound`=1

`right_bound`=10

Expected result:

`black_box.guess(10)` # 1

`black_box.guess(3)` # -1

`black_box.guess(1)` # -1

`black_box.guess(5)` # -1

`black_box.guess(9)` # 0 - Wow, you guessed correctly!

<br>

Please use the template `tasks/guess.py:guess_number` for the implementation.


### Exercise 2: Find the minimum time to produce a given amount of product

Suppose there are `N` factories. Each factory produces one ton of product per $c_i$ hours. The target amount of product is `P`, and you want to know the minimum number of hours required to produce at least `P` tons of product.

Your task is to implement the following function, which calculates the minimum number of hours to produce enough product:

```python
def get_required_time(capacities: List[int], target_amount: int) -> int:
    """Returns the minimum number of hours required to produce `target_amount` of product.

    NOTE: it is guaranteed that result won't exceed 10^12 hours.

    Args:
        capacities: List[int], capacities of factories, number of hours 
            required for a given factory to produce 1 ton of product
        target_amount: int, the target amount of product
    Returns:
        int, the minimum number of hours required
    """
    pass
```


**Example 1:**

`capacities`=[2, 4, 3]

`target_amount`=10

Expected result: 9

Explanation:
* after 1 hour, `0` tons of product will be produced (0 + 0 + 0)
* after 2 hours, `1` ton of product will be produced (1 + 0 + 0)
* after 3 hours, `2` tons of product will be produced (1 + 0 + 1)
* after 4 hours, `4` tons of product will be produced (2 + 1 + 1)
* after 5 hours, `4` tons of product will be produced (2 + 1 + 1)
* after 6 hours, `6` tons of product will be produced (3 + 1 + 2)
* after 7 hours, `6` tons of product will be produced (3 + 1 + 2)
* after 8 hours, `8` tons of product will be produced (4 + 2 + 2)
* after 9 hours, `9` tons of product will be produced (4 + 2 + 3)
* after 10 hours, `10` tons of product will be produced (5 + 2 + 3)

**Example 2:**

`capacities`=[1, 1, 3, 5]

`target_amount`=11

Expected result: 5

Explanation:
* after 1 hour, `2` tons of product will be produced (1 + 1 + 0 + 0)
* after 2 hours, `4` ton of product will be produced (2 + 2 + 0 + 0)
* after 3 hours, `7` tons of product will be produced (3 + 3 + 1 + 0)
* after 4 hours, `9` tons of product will be produced (4 + 4 + 1 + 0)
* after 5 hours, `12` tons of product will be produced (5 + 5 + 1 + 1)

<br>

Please use the template `tasks/factories.py:get_required_time` for the implementation.


### Exercise 3: Find the number if elements in an array in a given interval

Your task is to implement the following function, which handles queries for a given sorted array:

```python
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
    pass
```

**Example 1:**

`array`=[0, 1, 2, 4, 6, 1000]

`queries=`=[(-100, 3), (5, 5), (1, 4)]

Expected result: [3, 0, 3]

Explanation:
* `(-100, 3)` - the numbers [0, 1, 2] are in the interval
* `(5, 5)` - no numbers are in the interval
* `(1, 4)` - the numbers [1, 2, 4] are in the interval


**Example 2:**

`array`=[0, 0, 1, 1, 2]

`queries=`=[(0, 1), (1, 2), (-5, 10)]

Expected result: [4, 3, 5]

Explanation:
* `(0, 1)` - the numbers [0, 0, 1, 1] are in the interval
* `(1, 2)` - the numbers [1, 1, 2] are in the interval
* `(-5, 10)` - the numbers [0, 0, 1, 1, 2] are in the interval


<br>

Please use the template `tasks/queries.py:process_queries` for the implementation.
