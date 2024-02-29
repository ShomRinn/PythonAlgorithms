"""Templates for programming assignments: LCS problem."""
from typing import List


def get_optimal_substructure(string_a: str, string_b: str) -> List[List[int]]:
    n = len(string_a)
    m = len(string_b)
    F = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string_a[i-1] == string_b[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F


def get_optimal_solution(string_a: str, optimal_substructure_matrix: List[List[int]]) -> str:
    lcs = []
    i, j = len(string_a), len(optimal_substructure_matrix[0]) - 1

    while i > 0 and j > 0:
        if optimal_substructure_matrix[i][j] != optimal_substructure_matrix[i-1][j]:
            lcs.append(string_a[i-1])
            i -= 1
            j -= 1
        elif optimal_substructure_matrix[i][j] == optimal_substructure_matrix[i][j-1]:
            j -= 1
        else:
            i -= 1

    return ''.join(reversed(lcs))
