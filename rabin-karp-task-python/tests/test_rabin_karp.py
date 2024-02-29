"""Sample tests for 'tasks.rabin_karp' module."""
from tasks.rabin_karp import find_occurrences_via_rabin_karp


def test_rolling_hash_sample():
    """Tests for RollingHash class."""
    assert find_occurrences_via_rabin_karp(
        text='hello world',
        pattern='o',
        hash_base=3,
        hash_modulo=31,
        deterministic=True
    ) == [4, 7]

    assert find_occurrences_via_rabin_karp(
        text='hello world',
        pattern='o',
        hash_base=3,
        hash_modulo=2,
        deterministic=False
    ) == [1, 4, 6, 7]
