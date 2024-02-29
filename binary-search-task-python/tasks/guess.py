"""Template for programming assignment: Guess game."""


def guess_number(left_bound: int, right_bound: int, black_box: "BlackBox") -> int:
    """Returns the secret number based on a given black box.

    NOTE:
    * the secret number lies in the [left_bound, right_bound] interval
    * you interact with a given black box to guess the secret number
    * the only assumption you can have about a black box is that is has a `.guess` method
    * don't try to guess in which attribute the secret number is stored within a given black box ;)
    * trying all the numbers in [left_bound, right_bound] will be too slow to pass the hidden tests

    Args:
        left_bound: int, the left bound while guessing
        right_bound: int, the right bound while guessing
        black_box: "BlackBox", some object with a `.guess` method available
    Returns:
        int, the secret number.
    """
    while left_bound <= right_bound:
        mid = left_bound + (right_bound - left_bound) // 2
        result = black_box.guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            left_bound = mid + 1
        else:
            right_bound = mid - 1

    return -1