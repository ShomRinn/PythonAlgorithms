# Naive string matching and fuzzy search

## Purpose

The following coding exercises are designed to test your knowledge of the following concepts:

* The naive string-matching algorithm
* The Levenshtein distance
* Fuzzy search

## Overview

The coding exercises cover the following practical problems:
* Implementing the naive string-matching algorithm
* Implementing the Levenshtein distance
* Implementing a simple fuzzy search engine on top of the Levenshtein distance

## Coding exercises

### Exercise 1: The Naive string matching algorithm

Your task is to implement the following function for string-matching using the naive algorithm:

```python
def find_occurrences(text: str, pattern: str) -> List[int]:
    """Returns all positions within a given text where a given pattern occurs.

    NOTE: Nothing fancy is expected here, you can just use the naive algorithm.

    Args:
        text: str, a given text for searching.
        pattern: str, a given pattern for searching.
    
    Returns:
        List[int], all indices in the text where the pattern occurs.
    """
    pass
```

**Example 1:**

`text`='abababa'

`pattern`='aba'

Expected result: [0, 2, 4]

Explanation:

**aba**baba - 1st match.

ab**aba**ba - 2nd match.

abab**aba** - 3rd match.

**Example 2:**

`text`='question'

`pattern`='answer'

Expected result: []

**Example 3:**

`text`='Who’s there? Figs. Figs who? Figs the doorbell; it's not working!'

`pattern`='Figs'

Expected result: [13, 19, 29]

<br>

Please use the template `tasks/naive.py:find_occurrences` for the implementation.

### Exercise 2: The Levenshtein distance

Your task is to implement the following function to calculate the Levenshtein distance between two strings:

```python
def find_levenshtein_distance(string_a: str, string_b: str) -> int:
    """Returns the Levenshtein distance between two strings.

    Args:
        string_a: str, the first string.
        string_b: str, the second string.
    
    Returns:
        int, the Levenshtein distance between the given strings.
    """
    pass
```

**Example 1:**

`string_a`='property'

`string_b`='attribute'

Expected result: 8

**Example 2:**

`string_a`='maximization'

`string_b`='minimization'

Expected result: 2

**Example 3:**

`string_a`='confusion'

`string_b`='induction'

Expected result: 5

<br>

Please use the template `tasks/fuzzy_search.py:find_levenshtein_distance` for the implementation.

### Exercise 3: Basic FuzzySearch Engine

Your task is to implement the following class template for a basic fuzzy search engine:

```python
class FuzzySearchEngine:
    """Provides a basic 'FuzzySearch engine' interface."""
    def __init__(self):
        pass

    def load_corpus(self, corpus: List[str]):
        """Loads a given corpus of texts.

        Args:
            corpus: List[str], a set of texts that will be used as a database for the engine.
        """
        pass
    
    def find_best_matches(self, query_text: str, n_results: int = 1) -> List[str]:
        """Returns the most similar texts from the corpus based on a query text.

        NOTE: Please use the Levenshtein distance to measure the similarity between strings.
        NOTE: If there are multiple texts with the same Levenshtein distance for the query text 
        within the corpus, order the results lexicographically.
        NOTE: If the corpus contains less than 'n_results' texts, please return all the available ones.

        Args:
            query_text: str, a query text that should be used to retrieve texts from the corpus.
            n_results: int, the number of texts that should be returned (the most similar ones).
        Returns:
            List[str], the best matches from the corpus.
        """
        pass
```

For the examples below the following corpus will be used:

* 'refund'
* 'spy'
* 'retailer'
* 'concede'
* 'dozen'

**Example 1**

`query_text` = 'recruit'

`n_results` = 3

Expected result: ['refund', 'retailer', 'concede']

Explanation:

Levenshtein_Distance ('refund', 'recruit') = 4 # The closest

Levenshtein_Distance ('spy', 'recruit') = 7

Levenshtein_Distance ('retailer', 'recruit') = 6 # The second closest

Levenshtein_Distance ('concede', 'recruit') = 7 # Lexicographically smallest among other texts

Levenshtein_Distance ('dozen', 'recruit') = 7


**Example 2**

`query_text` = 'button'

`n_results` = 3

Expected result: ['dozen', 'refund', 'spy']

Explanation:

Levenshtein_Distance ('refund', 'button') = 6 # The second one 'refund' < 'spy'

Levenshtein_Distance ('spy', 'button') = 6 # The third one

Levenshtein_Distance ('retailer', 'button') = 7

Levenshtein_Distance ('concede', 'button') = 7

Levenshtein_Distance ('dozen', 'button') = 5 # The closest

<br>
Please use for the implementation `tasks/fuzzy_search.py:FuzzySearchEngine` the template.
