"""Template for programming assignment:
check if there is an eligible path in a directed graph from given vertex v to given vertex u."""
from typing import Dict, Set


def check_path_existence(n: int, edges: Dict[int, Set], v: int, u: int) -> bool:
    """
    Returns True/False depending on the existence of an eligible path from vertex v to vertex u in a directed graph.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    For example, you have a graph with five vertices from 0 to 4 and the edges {1: {0, 3}, 0: {2}, 3: {4}}.
    There is a path from vertex 1 to vertex 4: 1 -> 3 -> 4, so for v=1 and u=4, the function should return True.
    At the same time, no path exists from vertex 2 to vertex 0, so the expected result is False.

    Parameters:
        n (int) : the number of vertices in the graph; vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
        v (int): start path vertex
        u (int): end path vertex
    Returns:
        bool: True or False, depending on whether a (v,u)-path exists
    """
    visited = set()
    
    def dfs(current_vertex):
        if current_vertex == u:
            return True
        visited.add(current_vertex)
        for neighbor in edges.get(current_vertex, []):
            if neighbor not in visited and dfs(neighbor):
                return True
        return False
    
    return dfs(v)
