"""Sample tests for 'tasks.lcs' module."""
from tasks.lcs import get_optimal_solution, get_optimal_substructure


def test_get_optimal_substructure_sample():
    """Sample tests for get_optimal_substructure function."""
    # Example 1
    assert get_optimal_substructure(
        string_a='aa',
        string_b='ab',
    ) == [
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 1],
    ]
    # Example 2
    assert get_optimal_substructure(
        string_a='aaa',
        string_b='aba',
    ) == [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 2],
        [0, 1, 1, 2],
    ]
    # Example 3
    assert get_optimal_substructure(
        string_a='ababab',
        string_b='accabcc',
    ) == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 2, 2, 2],
        [0, 1, 1, 1, 2, 2, 2, 2],
        [0, 1, 1, 1, 2, 3, 3, 3],
        [0, 1, 1, 1, 2, 3, 3, 3],
        [0, 1, 1, 1, 2, 3, 3, 3],
    ]


def test_get_optimal_solution_sample():
    """Sample tests for get_optimal_solution function."""
    # Example 1
    assert get_optimal_solution(
        string_a='aa',
        optimal_substructure_matrix=[
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1],
        ]
    ) == 'a'
    # Example 2
    assert get_optimal_solution(
        string_a='aaa',
        optimal_substructure_matrix=[
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 1, 1, 2],
            [0, 1, 1, 2],
        ]
    ) == 'aa'
    # Example 3
    assert get_optimal_solution(
        string_a='ababab',
        optimal_substructure_matrix=[
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 2, 2, 2],
            [0, 1, 1, 1, 2, 2, 2, 2],
            [0, 1, 1, 1, 2, 3, 3, 3],
            [0, 1, 1, 1, 2, 3, 3, 3],
            [0, 1, 1, 1, 2, 3, 3, 3],
        ]
    ) == 'aab'
