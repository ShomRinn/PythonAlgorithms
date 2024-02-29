"""Template for programming assignment: find the length of the longest path in a directed acyclic graph."""
from typing import Dict, Set


def find_the_longest_path_in_dag(n: int, edges: Dict[int, Set]) -> int:
    """
    Returns the length of the longest path in a directed acyclic graph.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    For example, you have a graph with five vertices from 0 to 4 and the edges {4: {3}, 3: {2}, 2: {1}, 1: {0}}.
    The longest path is (4, 0)-path: 4 -> 3 -> 2 -> 1 -> 0. The expected result is 4.

    Parameters:
        n (int) : the number of vertices in the graph; vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        int: the length of the longest eligible path in a graph
    """
    def dfs(vertex, visited, stack):
        visited.add(vertex)
        for neighbour in edges.get(vertex, []):
            if neighbour not in visited:
                dfs(neighbour, visited, stack)
        stack.append(vertex)

    stack = []
    visited = set()
    for vertex in range(n):
        if vertex not in visited:
            dfs(vertex, visited, stack)
    
    longest_path_length = 0
    path_length = {vertex: 0 for vertex in range(n)}

    while stack:
        node = stack.pop()
        for neighbour in edges.get(node, []):
            if path_length[node] + 1 > path_length[neighbour]:
                path_length[neighbour] = path_length[node] + 1
                longest_path_length = max(longest_path_length, path_length[neighbour])
    
    return longest_path_length
