"""Template for programming assignment: Finding single-source shortest paths with negative edges """
from typing import Set, Dict, Tuple


def find_shortest_path_cost(n: int, edges: Dict[int, Set[Tuple[int, int]]], v: int) -> Tuple[int, int]:
    """
    Returns the tuple where the first value is the sum of the minimum cost paths from vertex `v` to all achievable vertices
    and the second is the number of unachievable vertices from vertex `v` in a directed weighted graph.
    The weight of (u,v)-edge represents the cost of traversing from 'u' to 'v'.

    !Weights can be negative, and there can also be negative cycles.
    !If there is a negative cycle, please return (None, None).

    Edges are stored as an adjacency dictionary whose second parameter is weight (cost).
    The expected algorithm complexity is O(N*M), where N is the number of vertices and M is the number of edges.

    For example, there is a graph with four vertices from 0 to 3 and the following edges/weights:
    {0: {(1, 3), (2, 7)}, 1: {(2, 5)}, 2: {(3, 5)}}
    If the starting vertex is 1, the expected result is (15, 1).
    Vertex 0 is the only unachievable vertex from vertex 1.
    The cost of getting a vertex that is equal to the starting vertex is 0, the (1,2)-path min cost is 5 and (1,3)-path min cost is 10 (1 -> 2 -> 3).

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set[Tuple[int, int]]]): adjacency dictionary which stores a set of adjacent vertices
        and the weights for each vertex
        v (int) : start vertex
    Returns:
        Tuple [int, int]: the sum of the minimum cost paths from vertex `v` to all achievable vertices
        and the number of unachievable vertices from vertex 'v'
    """
    distance = [float('inf')] * n
    distance[v] = 0

    for _ in range(n-1):
        for src, destinations in edges.items():
            for dest, weight in destinations:
                if distance[src] != float('inf') and distance[src] + weight < distance[dest]:
                    distance[dest] = distance[src] + weight

    for src, destinations in edges.items():
        for dest, weight in destinations:
            if distance[src] != float('inf') and distance[src] + weight < distance[dest]:
                return (None, None)

    sum_of_paths = sum([dist if dist != float('inf') else 0 for dist in distance])
    unachievable_vertices = len([1 for dist in distance if dist == float('inf')])

    return (sum_of_paths, unachievable_vertices)
