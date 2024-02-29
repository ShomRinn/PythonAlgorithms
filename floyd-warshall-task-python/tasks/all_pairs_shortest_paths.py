"""Template for programming assignment: Finding all-pairs shortest paths."""
from typing import List, Tuple


def get_sum_of_all_pairs_shortest_paths(n: int, adj_matrix: List[List[int]]) -> Tuple[int, int]:
    """
    Returns a tuple in which the first value is the sum of the all-pairs shortest paths between all connected vertices
    and the second is the number of disconnected pairs of vertices in an undirected weighted graph.
    The weight of (u,v)-edge represents the distance between 'u' and 'v' and vice versa.

    Edges are stored as an adjacency matrix, where 0 means no edge and a positive value indicates the presence of an edge and reflects its weight.
    The expected algorithm complexity is O(N^3), where N is the number of vertices.
    The vertices are enumerated from 0 to N-1, where N is the number of vertices.

    For example, you have a graph with three vertices from 0 to 2 and the following adjacency matrix:
    [[0, 10, 5], [10, 0, 6], [5, 6, 0]]
    The expected result is (42, 0).

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        adj_matrix (List[List[int]]): adjacency matrix with weights
    Returns:
        Tuple [int, int]: the sum of the all-pairs shortest paths between all connected vertices
        and the number of disconnected pairs of vertices
    """
    shortest_paths = [[float('inf') if adj_matrix[i][j] == 0 and i != j else adj_matrix[i][j] for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])
    
    sum_of_paths = 0
    disconnected_pairs = 0
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if shortest_paths[i][j] == float('inf'):
                    disconnected_pairs += 1
                else:
                    sum_of_paths += shortest_paths[i][j]
    
    return sum_of_paths, disconnected_pairs
