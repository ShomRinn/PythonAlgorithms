"""Templates for programming assignments: 0-1 knapsack problem."""
from typing import List


def get_optimal_substructure(weights: List[int], values: List[int], w: int) -> List[List[int]]:
    N = len(weights)
    F = [[0 for _ in range(w + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, w + 1):
            if weights[i-1] <= j:
                F[i][j] = max(F[i-1][j], values[i-1] + F[i-1][j-weights[i-1]])
            else:
                F[i][j] = F[i-1][j]

    return F


def get_optimal_solution(weights: List[int], optimal_substructure_matrix: List[List[int]]) -> List[int]:
    solution = [0] * len(weights)
    i = len(weights)
    j = len(optimal_substructure_matrix[0]) - 1

    while i > 0 and j > 0:
        if optimal_substructure_matrix[i][j] != optimal_substructure_matrix[i-1][j]:
            solution[i-1] = 1
            j -= weights[i-1]
        i -= 1

    return solution
