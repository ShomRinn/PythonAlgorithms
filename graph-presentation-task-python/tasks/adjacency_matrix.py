"""Template for programming assignment: Graph Adjacency Matrix."""
from typing import List


class GraphAdjacencyMatrix:
    """Default interface for supporting undirected graphs using adjacency matrix."""

    def __init__(self, number_of_vertices: int):
        self.adjacency_matrix = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds a new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        self.adjacency_matrix[vertex1][vertex2] = 1
        self.adjacency_matrix[vertex2][vertex1] = 1

    def get_list_of_adjacent_vertices(self, vertex: int) -> List[int]:
        """Returns a 0/1 list for a given vertex that indicates vertices adjacent to it.

        Positions of 1-s in the result list correspond to vertices that are adjacent to a given vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} the following list should be returned for the vertex 0: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        return self.adjacency_matrix[vertex]

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns the number of adjacent vertices for a given vertex.

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        return sum(self.adjacency_matrix[vertex])

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks whether there is an edge in the graph between 2 given vertices.

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        return self.adjacency_matrix[vertex1][vertex2] == 1
