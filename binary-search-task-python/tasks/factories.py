"""Template for programming assignment: Factories."""
from typing import List


def get_required_time(capacities: List[int], target_amount: int) -> int:
    """Returns the minimum number of hours required to produce `target_amount` of product.

    NOTE: it is guaranteed that result won't exceed 10^12 hours.

    Args:
        capacities: List[int], capacities of factories, number of hours 
            required for a given factory to produce 1 ton of product
        target_amount: int, the target amount of product
    Returns:
        int, the minimum number of hours required
    """
    left, right = 0, 10**12

    def is_enough(time):
        total = sum(time // capacity for capacity in capacities)
        return total >= target_amount

    while left < right:
        mid = (left + right) // 2
        if is_enough(mid):
            right = mid
        else:
            left = mid + 1

    return left