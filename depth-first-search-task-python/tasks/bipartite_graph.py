"""Template for programming assignment: check if a given connected undirected graph is bipartite or not."""
from typing import Dict, Set


def check_bipartite_graph(n: int, edges: Dict[int, Set]) -> bool:
    """
    Returns True/False if a connected undirected graph is bipartite or not.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    For example, you have a graph with five vertices from 0 to 4 and the edges {0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3}.
    This graph is bipartite because you can select two sets of vertices, {0, 2, 4} and {1, 3}, that don't have inner edges.

    Parameters:
        n (int) : the number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        bool: True or False if a graph is bipartite or not
    """
    color = {}
    
    def dfs(vertex, current_color):
        if vertex in color:
            return color[vertex] == current_color
        color[vertex] = current_color
        return all(dfs(neighbour, not current_color) for neighbour in edges.get(vertex, set()))
    
    for vertex in range(n):
        if vertex not in color:
            if not dfs(vertex, True):
                return False
    return True
