"""Sample tests for 'tasks.knapsack' module."""
from tasks.knapsack import get_optimal_solution, get_optimal_substructure


def test_get_optimal_substructure_sample():
    """Sample tests for get_optimal_substructure function."""
    # Example 1
    assert get_optimal_substructure(
        weights=[2, 2],
        values=[1, 2],
        w=3,
    ) == [
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 2, 2],
    ]
    # Example 2
    assert get_optimal_substructure(
        weights=[1, 1, 1],
        values=[1, 2, 3],
        w=2,
    ) == [
        [0, 0, 0],
        [0, 1, 1],
        [0, 2, 3],
        [0, 3, 5]
    ]
    # Example 3
    assert get_optimal_substructure(
        weights=[3, 2, 1, 4],
        values=[1, 2, 1, 2],
        w=6,
    ) == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 2, 2, 2, 3, 3],
        [0, 1, 2, 3, 3, 3, 4],
        [0, 1, 2, 3, 3, 3, 4]
    ]


def test_get_optimal_solution_sample():
    """Sample tests for get_optimal_solution function."""
    # Example 1
    assert get_optimal_solution(
        weights=[2, 2],
        optimal_substructure_matrix=[
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 2, 2],
        ]
    ) == [0, 1]
    # Example 2
    assert get_optimal_solution(
        weights=[1, 1, 1],
        optimal_substructure_matrix=[
            [0, 0, 0],
            [0, 1, 1],
            [0, 2, 3],
            [0, 3, 5]
        ]
    ) == [0, 1, 1]
    # Example 3
    assert get_optimal_solution(
        weights=[3, 2, 1, 4],
        optimal_substructure_matrix=[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 2, 2, 2, 3, 3],
            [0, 1, 2, 3, 3, 3, 4],
            [0, 1, 2, 3, 3, 3, 4]
        ]
    ) in [[1, 1, 1, 0], [0, 1, 0, 1]]
