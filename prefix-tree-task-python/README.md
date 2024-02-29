# Prefix Tree (Trie)

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* Prefix tree data structure
* Data structure augmentation

## Overview

The coding exercises cover the following practical problems:
* Implementing a basic version of a prefix tree
* Augmenting a prefix tree to support more complex operations
* Using a prefix tree to match strings

## Coding exercises

### Exercise 1: The basic version of a prefix tree

Each node in a prefix tree should contain at least two things:
* some indication of whether the node corresponds to a string from the corpus (strings that were previously inserted)
* a mapping from characters to the corresponding prefix tree nodes

Consider the following class, which represents a prefix tree node:
```python
class PrefixTreeNode:
    def __init__(self):
        self.mapping: Dict[str, 'PrefixTreeNode'] = dict()
        self.is_terminal = False
```

Your task is to implement the following class for supporting basic prefix tree operations:

```python
class PrefixTree:
    """Implementation of a basic prefix tree API."""

    def __init__(self):
        # Here, you should initialize the prefix tree with an empty root node.
        pass
    
    def insert(self, s: str):
        """Inserts a given string into the prefix tree.

        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string for insertion.
        """
        pass
    
    def search(self, s: str) -> bool:
        """Returns whether a given string is in the prefix tree (was inserted before).
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string for look-up.
        Returns:
            bool, whether a given string is in the prefix tree.
        """
        pass

    def starts_with(self, s: str) -> bool:
        """Returns whether there is a string in the prefix tree with the prefix equal to a given string.
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string (prefix) for look-up.
        Returns:
            bool, whether there is a string in the prefix tree that starts with a given string.
        """
        pass
```


**Example:**

Setup:
```python
pt = PrefixTree()
pt.insert("aba")
pt.insert("aba") # NOTE: duplicate strings are allowed
pt.insert("abab")
pt.insert("caba")
```

Queries:
```python
pt.search("a") # False is expected
pt.search("ab") # False is expected
pt.search("aba") # True is expected
pt.search("abab") # True is expected
pt.search("caba") # True is expected
pt.search("cabacaba") # False is expected

pt.starts_with("a") # True is expected
pt.starts_with("ab") # True is expected
pt.starts_with("aba") # True is expected
pt.starts_with("abab") # True is expected
pt.starts_with("caba") # True is expected
pt.starts_with("cabacaba") # False is expected
```

<br>

Please use the template `tasks/prefix_tree.py:PrefixTree` for the implementation.

### Exercise 2: Augment a basic prefix tree to support more complex operations

[Data structures augmentation](https://users.cs.fiu.edu/~giri/teach/UoM/7713/f98/lec3.html)

Basically, the process of augmenting a data structure consists of the following steps:
1. Choose an underlying data structure
   * We will use a basic prefix tree.
2. Determine additional information to be maintained in the underlying data structure
   * You need to understand what additional information needs to be stored to support new operations.
3. Verify whether the augmentation is feasible
   * Yes, it is. Trust us.
4. Implementation... Profit!

In this coding exercise, you will change the basic prefix tree data structure to support of more complex operations, like counting the number of words in the corpus (previously inserted words) that match a given string (prefix).

Take a look at the following class to be implemented:

```python
class PrefixTreeAugmented(PrefixTree):
    """Implementation of an augmented prefix tree API.
    
    NOTE: this class inherits a basic interface, so the basic operations should be supported:
    * insert
    * search
    * starts_with

    If you need to make changes in the `PrefixTreeNode` class, feel free to either 
    create an additional class like `PrefixTreeAugmentedNode` or just add some additional 
    attributes to the class.
    """

    def __init__(self):
        # Here, you should initialize the augmented prefix tree with an empty root node.
        pass

    def count_words_equal_to(self, s: str) -> int:
        """Returns the number of strings in the prefix tree that are equal to a given string.
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string for look-up.
        Returns:
            int, the number of strings in the prefix tree that are equal to a given string.
        """
        pass

    def count_words_starting_with(self, s: str) -> int:
        """Returns the number of strings in the prefix tree that start with a given string (prefix).
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string (prefix) for look-up.
        Returns:
            int, the number of strings in the prefix tree that start with a given string.
        """
        pass
```

**Example:**

Setup:
```python
pta = PrefixTreeAugmented()
pta.insert("aba")
pta.insert("aba")
pta.insert("aba")
pta.insert("abab")
pta.insert("ababad")
pta.insert("caba")
```

Queries:
```python
# The basic operations should still work correctly.
pta.search("a") # False is expected
pta.search("ab") # False is expected
pta.search("aba") # True is expected
pta.search("abab") # True is expected
pta.search("caba") # True is expected
pta.search("cabacaba") # False is expected

pta.starts_with("a") # True is expected
pta.starts_with("ab") # True is expected
pta.starts_with("aba") # True is expected
pta.starts_with("abab") # True is expected
pta.starts_with("caba") # True is expected
pta.starts_with("cabacaba") # False is expected

# The new operations.
pta.count_words_equal_to("aba") # 3
pta.count_words_equal_to("ab") # 0
pta.count_words_equal_to("abab") # 1
pta.count_words_equal_to("cabacaba") # 0

pta.count_words_starting_with("") # 6
pta.count_words_starting_with("a") # 5
pta.count_words_starting_with("ab") # 5
pta.count_words_starting_with("aba") # 5
pta.count_words_starting_with("abab") # 2
pta.count_words_starting_with("ababa") # 1
pta.count_words_starting_with("c") # 1
```

<br>

Please use the template `tasks/prefix_tree.py:PrefixTreeAugmented` for the implementation.


### Exercise 3: Use Prefix Tree for string matching

Given the string $s$ and a set of $k$ patterns $p_i$, your task is to implement the following function
for calculating the total number of times the patterns $p_i$ match a substring in $s$:

```python
def get_number_of_matches(text: str, patterns: List[str]) -> int:
    """Returns the number of times all given patterns occur in a given string.
    
    NOTE: If there are duplicates within the given patterns, each one should be counted.
    NOTE: You probably need to use trie somehow...
    NOTE: |text| >> max(|patterns_i|)
    NOTE: The expected complexity looks like O(|text| * ...) - linear in terms of the length of a given string.

    Args:
        text: str, a given string for matching
        patterns: List[str], a given set of patterns for matching
    Returns:
        int, the number of times all given patterns occur in a given string.
    """
    pass
```

**Example 1:**

`text`='abracadabra'

`patterns`=['a', 'a', 'abra', 'ca']

Expected output: 13

Explanation:

* 'a' occurs 5 times
* 'a' occurs 5 times
* 'abra' occurs 2 times
* 'ca' occurs 1 time

**Example 2:**

`text`='hello world'

`patterns`=['hell', 'l', 'l', 'o']

Expected output: 9

Explanation:

* 'hell' occurs 1 time
* 'l' occurs 3 times
* 'l' occurs 3 times
* 'o' occurs 2 times

**Example 3:**

`text`='Tomatoes make great weapons when water balloons aren’t available.'

`patterns`=['at', 'ma', 'great weapons']

Expected output: 6

Explanation:

* 'at' occurs 3 times
* 'ma' occurs 2 times
* 'great weapons' occurs 1 time

<br>

Please use the template `tasks/prefix_tree.py:get_number_of_matches` for the implementation.
