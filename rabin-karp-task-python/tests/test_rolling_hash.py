"""Sample tests for 'tasks.rolling_hash' module."""
from tasks.rolling_hash import RollingHash


def test_rolling_hash_sample():
    """Tests for RollingHash class."""
    rh = RollingHash(
        text='hello hello',
        hash_base=3,
        hash_modulo=31,
    )

    assert rh.get_hash(0, 1) == 10
    assert rh.get_hash(0, 2) == 14
    assert rh.get_hash(2, 4) == 12
    assert rh.get_hash(2, 2) == 15
    assert rh.get_hash(0, 4) == rh.get_hash(6, 10)
