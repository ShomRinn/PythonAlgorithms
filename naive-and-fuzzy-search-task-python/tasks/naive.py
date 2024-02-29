"""Template for programming assignment: the naive string-matching."""
from typing import List


def find_occurrences(text: str, pattern: str) -> List[int]:
    """Returns all positions within a given text where a given pattern occurs.

    NOTE: Nothing fancy is expected here, you can just use the naive algorithm.

    Args:
        text: str, a given text for searching.
        pattern: str, a given pattern for searching.
    
    Returns:
        List[int], all indices in the text where the pattern occurs.
    """
    if not pattern:  # If the pattern is empty, return an empty list
        return []

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences
