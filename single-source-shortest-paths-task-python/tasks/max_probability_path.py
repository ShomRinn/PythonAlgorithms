"""Template for programming assignment: Finding the most probable path"""
from typing import Set, Dict, Tuple


def get_max_probability_path(n: int, edges: Dict[int, Set[Tuple[int, float]]], v: int, u: int) -> float:
    """
    Returns the maximum probability of getting from vertex `v` to vertex `u` in an undirected weighted graph.
    The weight of (u,v)-edge represents the probability of successfully of traversing from 'u' to 'v' and vice versa.
    Edges are stored as an adjacency dictionary whose second parameter is weight (probability).
    The expected algorithm complexity is O(N^2), where N is the number of vertices.
    Vertices are enumerated from 0 to N-1.

    If no (v,u)-path exists, please return 0.
    Your answer will be accepted if it differs from the correct answer by 1e-5 or less.

    For example, there is a graph with three vertices from 0 to 2 and the following edges:
    {0: {(1, 0.5), (2, 0.2)), 1: {(0, 0.5), (2, 0.5)}, 2: {(0, 0.2), (1, 0.5)}}
    If the starting vertex is 0 and the ending vertex is 2, the expected result is 0.25.
    There are two paths from start to end, one (0 -> 2) with a probability of success of 0.2 and
    the other (0 -> 1 -> 2) with a probability of 0.5 * 0.5 = 0.25.

    Parameters:
        n (int) : the number of vertices in the graph, numbered from 0 to n-1
        edges (Dict[int, Set[Tuple[int, float]]]): adjacency dictionary, which stores a set of adjacent vertices
        and its weights for each vertex
        v (int) : start vertex
        u (int) : finish vertex
    Returns:
         int: the maximum probability of getting from vertex `v` to vertex `u`
    """
    probabilities = [0.0] * n
    probabilities[v] = 1.0
    
    for _ in range(n - 1):
        updated = False
        for vertex, neighbors in edges.items():
            for neighbor, prob in neighbors:
                if probabilities[vertex] * prob > probabilities[neighbor]:
                    probabilities[neighbor] = probabilities[vertex] * prob
                    updated = True
        if not updated: break
    
    return probabilities[u] if probabilities[u] > 0 else 0

