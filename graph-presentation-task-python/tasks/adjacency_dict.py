"""Template for programming assignment: Graph Adjacency Dictionary."""
# Might be useful, take a look.
from collections import defaultdict
from typing import List

class GraphAdjacencyDictionary:
    """Default interface for supporting undirected graphs using adjacency dictionary."""

    def __init__(self, number_of_vertices: int):
        self.adjacency_dict = defaultdict(set)
        self.number_of_vertices = number_of_vertices

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds a new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        self.adjacency_dict[vertex1].add(vertex2)
        self.adjacency_dict[vertex2].add(vertex1)

    def get_list_of_adjacent_vertices(self, vertex: int) -> List[int]:
        """Returns a 0/1 list for a given vertex that indicates vertices adjacent to it.

        Positions of 1-s in the result list correspond to vertices that are adjacent to a given vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} the following list should be returned for the vertex 0: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        adjacency_list = [0] * self.number_of_vertices
        for adj_vertex in self.adjacency_dict[vertex]:
            adjacency_list[adj_vertex] = 1
        return adjacency_list

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns the number of adjacent vertices for a given vertex.

        NOTE: O(1) complexity is expected for this operation.
        """
        return len(self.adjacency_dict[vertex])

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks whether there is an edge in the graph between 2 given vertices.

        NOTE: O(1) complexity is expected for this operation.
        """
        return vertex2 in self.adjacency_dict[vertex1]
