"""Sample tests for 'tasks.guess' module."""
from tasks.guess import guess_number


class DummyBlackBox:
    """Please don't assume that this class will be used in the hidden tests."""

    def __init__(self, secret_number: int):
        self.secret_number = secret_number
    
    def guess(self, value: int):
        if self.secret_number == value:
            return 0
        if self.secret_number > value:
            return -1
        
        return 1


def test_guess_number_sample():
    """Sample tests for guess_number function."""
    # Example 1
    assert guess_number(
        left_bound=1,
        right_bound=10,
        black_box=DummyBlackBox(5)
    ) == 5

    # Example 2
    assert guess_number(
        left_bound=1,
        right_bound=10,
        black_box=DummyBlackBox(9)
    ) == 9
