"""Template for programming assignment: repeated dna sequences problem."""
from typing import List


DNA_ALPHABET = 'ATGC'


def dna_substring_to_int(dna_seq: str) -> int:
    """Returns integer representation of a given DNA sequence.

    NOTE: it is a helper function, feel free to use it (or not).

    Idea:
    * DNA 'alphabet' contains only 4 characters
    * We can use 'base-4' numeral system to encode DNA sequences

    Example:
    dna_seq = 'AATGC' -> [0, 0, 1, 2, 3]
    encoding = 4^4 * 0 + 4^3 * 0 + 4^2 * 1 + 4^1 * 2 + 4^0 * 3

    Args:
        dna_seq: str, a given DNA sequence.
    
    Returns:
        int, encoded integer representation of a given DNA sequence.
    """
    encoding = 0
    for ch in dna_seq:
        encoding = encoding * 4 + DNA_ALPHABET.index(ch)

    return encoding


def find_repeated_dna_sequences(dna_sequence: str) -> List[str]:
    if len(dna_sequence) < 8:
        return []

    seen, repeated = set(), set()
    for i in range(len(dna_sequence) - 7):
        substring = dna_sequence[i:i + 8]
        # Преобразуем подстроку в числовое представление
        encoded_substring = dna_substring_to_int(substring)
        if encoded_substring in seen:
            repeated.add(substring)
        else:
            seen.add(encoded_substring)

    return list(repeated)

