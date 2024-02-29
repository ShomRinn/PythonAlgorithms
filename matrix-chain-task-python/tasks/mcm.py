"""Templates for programming assignments: the Matrix chain multiplication problem."""
from typing import List, Tuple


def get_optimal_substructure(dimensions_of_matrices: List[Tuple[int, int]]) -> List[List[int]]:
    n = len(dimensions_of_matrices)
    F = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            F[i][j] = float('inf')
            for k in range(i, j):
                q = F[i][k] + F[k + 1][j] + dimensions_of_matrices[i][0] * dimensions_of_matrices[k][1] * dimensions_of_matrices[j][1]
                if q < F[i][j]:
                    F[i][j] = q

    return F



def get_mcm_solution(dimensions_of_matrices: List[Tuple[int, int]]) -> str:
    F = [[(0, "") for _ in range(len(dimensions_of_matrices))] for _ in range(len(dimensions_of_matrices))]

    for chain_len in range(2, len(dimensions_of_matrices) + 1):
        for i in range(len(dimensions_of_matrices) - chain_len + 1):
            j = i + chain_len - 1
            if F[i + 1][j][1]:
                F[i][j] = (F[i + 1][j][0] + dimensions_of_matrices[i][0] * dimensions_of_matrices[i][1] * dimensions_of_matrices[j][1], f"*({F[i + 1][j][1]})")
            else:
                F[i][j] = (F[i + 1][j][0] + dimensions_of_matrices[i][0] * dimensions_of_matrices[i][1] * dimensions_of_matrices[j][1], f"*")
            for k in range(i + 1, j):
                if F[i][k][0] + F[k + 1][j][0] + dimensions_of_matrices[i][0] * dimensions_of_matrices[k][1] * dimensions_of_matrices[j][1] < F[i][j][0]:
                    if F[i][k][1] and F[k + 1][j][1]:
                        F[i][j] = (F[i][k][0] + F[k + 1][j][0] + dimensions_of_matrices[i][0] * dimensions_of_matrices[k][1] * dimensions_of_matrices[j][1],
                                   f"({F[i][k][1]})*({F[k + 1][j][1]})")
                    elif F[i][k][1]:
                        F[i][j] = (F[i][k][0] + F[k + 1][j][0] + dimensions_of_matrices[i][0] * dimensions_of_matrices[k][1] * dimensions_of_matrices[j][1], f"({F[i][k][1]})*")
                    elif F[k + 1][j][1]:
                        F[i][j] = (F[i][k][0] + F[k + 1][j][0] + dimensions_of_matrices[i][0] * dimensions_of_matrices[k][1] * dimensions_of_matrices[j][1], f"*({F[i][k][1]})")

    return F[0][-1][1]
