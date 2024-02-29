"""Template for programming assignment: the Rabin-Karp algorithm."""
from typing import List

from tasks.rolling_hash import RollingHash


def find_occurrences_via_rabin_karp(
    text: str, 
    pattern: str, 
    hash_base: int = 3, 
    hash_modulo: int = 31,
    deterministic: bool = True
) -> List[int]:
    """Returns all positions within a text where a given pattern occurs.

    NOTE: Please use the Rabin-Karp algorithm.
    NOTE: The parameter `deterministic` defines whether hash value hits should be checked explicitly
    or whether false positive matches are fine.

    Args:
        text: str, the text to be searched
        pattern: str, the pattern to search for
        hash_base: int, the base value for polynomial hashing (P)
        hash_modulo: int, the modulo that will be used for hashing (M)
        deterministic: bool, whether hash value hits should be checked explicitly
    Returns:
        List[int], all indices in the text where the pattern occurs.
    """
    pattern_length = len(pattern)
    text_length = len(text)

    if pattern_length > text_length or pattern_length == 0:
        return []

    rolling_hash_text = RollingHash(text, hash_base, hash_modulo)
    rolling_hash_pattern = RollingHash(pattern, hash_base, hash_modulo)

    pattern_hash = rolling_hash_pattern.get_hash(0, pattern_length - 1)

    occurrences = []

    for i in range(text_length - pattern_length + 1):
        if rolling_hash_text.get_hash(i, i + pattern_length - 1) == pattern_hash:
            if not deterministic or text[i:i + pattern_length] == pattern:
                occurrences.append(i)

    return occurrences
