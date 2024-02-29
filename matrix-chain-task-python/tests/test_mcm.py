"""Sample tests for 'tasks.mcm' module."""
from tasks.mcm import get_optimal_substructure, get_mcm_solution


def test_get_optimal_substructure_sample():
    """Tests for get_optimal_substructure function."""
    assert get_optimal_substructure([(5, 12), (12, 7), (7, 3), (3, 6)]) == [
        [0, 420, 432, 522],
        [0, 0, 252, 468],
        [0, 0, 0, 126],
        [0, 0, 0, 0],
    ]

    assert get_optimal_substructure([(3, 2), (2, 5), (5, 2)]) == [
        [0, 30, 32],
        [0, 0, 20],
        [0, 0, 0],
    ]

    assert get_optimal_substructure([(1, 5), (5, 3), (3, 6), (6, 2)]) == [
        [0, 15, 33, 45],
        [0, 0, 90, 66],
        [0, 0, 0, 36],
        [0, 0, 0, 0],
    ]


def test_get_mcm_solution_sample():
    """Tests for get_mcm_solution function."""
    assert get_mcm_solution([(5, 12), (12, 7), (7, 3), (3, 6)]) == "(*(*))*"

    assert get_mcm_solution([(3, 2), (2, 5), (5, 2)]) == "*(*)"

    assert get_mcm_solution([(1, 5), (5, 3), (3, 6), (6, 2)]) == "((*)*)*"
