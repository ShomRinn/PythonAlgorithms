"""Templates for programming assignments: the Knuth-Morris-Pratt algorithm."""
from typing import List


def build_lps_array(text: str) -> List[int]:
    """Returns the LPS array for a given string.

    Args:
        text: str, a given string
    Returns:
        List[int], the result LPS array.
    """
    lps = [0] * len(text)
    length = 0

    i = 1
    while i < len(text):
        if text[i] == text[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def find_occurrences_via_kmp(text: str, pattern: str) -> List[int]:
    """Returns all positions within a given text where a given pattern occurs.

    NOTE: Please use the KMP algorithm.

    Args:
        text: str, the text to be search
        pattern: str, the pattern to search for
    Returns:
        List[int], all indices in the given text where the pattern occurs.
    """
    if not pattern:
        return []

    lps = build_lps_array(pattern)
    occurrences = []
    i = j = 0

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences


def is_tandem_repeat(text: str) -> bool:
    """Checks whether a given string is a tandem repeat.

    NOTE: The expected complexity is O(n), where n is the length of `text`.

    Args:
        text: str, a given string
    Returns:
        bool, whether a given string is a tandem repeat.
    """
    n = len(text)
    if n == 0:
        return False

    lps = build_lps_array(text)
    length = lps[n - 1]

    # Check if the string can be divided into equal parts
    return length > 0 and n % (n - length) == 0
