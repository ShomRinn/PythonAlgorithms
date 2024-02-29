"""Template for programming assignment: rolling hash."""


class RollingHash:
    """Provides a basic 'Polynomial rolling hash' interface."""

    def __init__(self, text: str, hash_base: int = 3, hash_modulo: int = 31):
        """
        Args:
            text: str, a text that will be used for rolling hashing
            hash_base: int, a base value for polynomial hashing (P)
            hash_modulo: int, a modulo that should be used for hashing (M)
        """
        self.text = text
        self.hash_base = hash_base
        self.hash_modulo = hash_modulo
        self.precompute_hashes()
    
    def precompute_hashes(self):
        self.hash_values = [0] * (len(self.text) + 1)
        for i in range(1, len(self.text) + 1):
            self.hash_values[i] = (self.hash_values[i - 1] * self.hash_base + ord(self.text[i - 1])) % self.hash_modulo
    
    def get_hash(self, left_index: int, right_index: int) -> int:
        """Returns a polynomial hash value for a given substring.

        H(L, R) = ( ord(text[L]) * P^(R-L) + ... + ord(text[R]) ) % M

        NOTE: Use ord(.) - standard Python function

        NOTE: O(1) time complexity is expected.

        Args:
            left_index: int, the left index of the target substring
            right_index: int, the right index of the target substring
        Returns:
            int, the value of polynomial hash function for the given substring
        """
        if left_index > right_index:
            return 0

        left_hash = self.hash_values[left_index]
        right_hash = self.hash_values[right_index + 1]

        power = pow(self.hash_base, right_index - left_index + 1, self.hash_modulo)
        return (right_hash - left_hash * power) % self.hash_modulo
