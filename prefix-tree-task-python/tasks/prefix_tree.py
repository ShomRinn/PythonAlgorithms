"""Templates for programming assignments: Prefix Tree."""
from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.mapping: Dict[str, 'TrieNode'] = dict()
        self.is_terminal = False
        self.word_count = 0
        self.prefix_count = 0


class PrefixTree:
    """Implementation of a basic prefix tree API."""

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s: str):
        """Inserts a given string into the prefix tree.

        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string for insertion.
        """
        cur = self.root
        for c in s:
            if c not in cur.mapping:
                cur.mapping[c] = TrieNode()
            cur = cur.mapping[c]
        cur.is_terminal = True
    
    def search(self, s: str) -> bool:
        """Returns whether a given string is in the prefix tree (was inserted before).
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string for look-up.
        Returns:
            bool, whether a given string is in the prefix tree.
        """
        cur = self.root
        for c in s:
            if c not in cur.mapping:
                return False
            cur = cur.mapping[c]
        return cur.is_terminal

    def starts_with(self, s: str) -> bool:
        """Returns whether there is a string in the prefix tree with the prefix equal to a given string.
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string (prefix) for look-up.
        Returns:
            bool, whether there is a string in the prefix tree that starts with a given string.
        """
        cur = self.root
        for c in s:
            if c not in cur.mapping:
                return False
            cur = cur.mapping[c]
        return True


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
        super().__init__()

    def insert(self, s: str):
        cur = self.root
        for c in s:
            cur.prefix_count += 1
            if c not in cur.mapping:
                cur.mapping[c] = TrieNode()
            cur = cur.mapping[c]
        cur.is_terminal = True
        cur.word_count += 1
        cur.prefix_count += 1

    def count_words_equal_to(self, s: str) -> int:
        """Returns the number of strings in the prefix tree that are equal to a given string.
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).

        Args:
            s: string, a given string for look-up.
        Returns:
            int, the number of strings in the prefix tree that are equal to a given string.
        """
        cur = self.root
        for c in s:
            if c not in cur.mapping:
                return 0
            cur = cur.mapping[c]
        return cur.word_count if cur.is_terminal else 0

    def count_words_starting_with(self, s: str) -> int:
        """Returns the number of strings in the prefix tree that start with a given string (prefix).
        
        NOTE: the expected complexity is O(|s|), assuming dict operations have a complexity of O(1).
        

        Args:
            s: string, a given string (prefix) for look-up.
        Returns:
            int, the number of strings in the prefix tree that start with a given string.
        """
        cur = self.root
        for c in s:
            if c not in cur.mapping:
                return 0
            cur = cur.mapping[c]
        return cur.prefix_count


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
    trie = PrefixTreeAugmented()
    for pattern in patterns:
        trie.insert(pattern)

    match_count = 0
    for i in range(len(text)):
        cur = trie.root
        for j in range(i, len(text)):
            if text[j] not in cur.mapping:
                break
            cur = cur.mapping[text[j]]
            if cur.is_terminal:
                match_count += cur.word_count

    return match_count