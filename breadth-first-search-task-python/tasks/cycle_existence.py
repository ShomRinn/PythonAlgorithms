"""Template for programming assignment: check if undirected graph has at least one cycle."""
from typing import Dict, Set


def check_cycle_existence(n: int, edges: Dict[int, Set]) -> bool:
    """
    Returns True if there is at least one cycle in the undirected graph.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    E.g. there is graph with 6 vertices from 0 to 5 and edges {{0,1}, {1,5}, {5,0}, {3,4}},
    the expected result is True because there is a cycle 0 - 1 - 5 - 0.

    Parameters:
        n (int) : the number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        bool: True if there is a cycle in the undirected graph, otherwise False
    """
    visited = set()
    
    def dfs(v, parent):
        visited.add(v)
        for neighbour in edges.get(v, []):
            if neighbour not in visited:
                if dfs(neighbour, v):
                    return True
            elif parent != neighbour:
                return True
        return False
    
    for vertex in range(n):
        if vertex not in visited:
            if dfs(vertex, -1):
                return True
    
    return False
