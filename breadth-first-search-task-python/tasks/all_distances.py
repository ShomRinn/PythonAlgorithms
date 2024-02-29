"""Template for programming assignment: calculate minimum distance from given vertex to all vertices."""
from typing import Dict, List, Set
from collections import deque

def calculate_all_distances_from_vertex(n: int, edges: Dict[int, Set], vertex: int) -> List:
    """
    Returns a list with the minimum distances from the vertex to all vertices, including itself.
    If there is no path, please set the distance to -1.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    E.g. you have graph with 4 vertices from 0 to 3 and edges {{0,1}, {1,2}). 
    Initial vertex is 2, and the expected result is [2, 1, 0, -1]. 
    - 2 at the first position (index 0) means that two edges 
        are needed to get from vertex '2' to vertex '0': 2 -> 1 -> 0. 
    - At the 2nd position (index 1), there is 1 because the vertices '1' and '2' are adjacent.
    - 0 is placed on the 3rd place (index 2) because it is the starting point and 
        the list ends with -1 because there is no path between vertices '2' and '3'.

    Parameters:
        n (int) : the number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores set of adjacent vertices for each vertex
        vertex (int): initial vertex
    Returns:
        List: distance list which reflects the distance between initial vertex and all other vertices,
        the number at each index I shows the distance from starting vertex to vertex I
    """
    distances = [-1] * n
    distances[vertex] = 0
    
    queue = deque([vertex])
    
    while queue:
        current_vertex = queue.popleft()
        for neighbor in edges.get(current_vertex, []):
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)
    
    return distances
