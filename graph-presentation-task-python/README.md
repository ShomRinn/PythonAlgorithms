# Graph representation

## Purpose

The coding exercises are designed to test your knowledge of the following concepts:

* Representations of graphs in memory
* An adjacency matrix as a data structure for representing graphs in memory
* An adjacency dictionary as a data structure for representing graphs in memory

## Overview

The coding exercises cover the following practical problems:
* Implementing the `Adjacency matrix` interface for undirected graphs
* Implementing the `Adjacency dictionary` interface for undirected graphs

## Coding exercises

### Exercise 1: The adjacency matrix interface for undirected graphs

Your task is to implement the following interface for `Adjacency matrix` data structure for representing undirected graphs in memory:

```python
class GraphAdjacencyMatrix:
    """Default interface for supporting undirected graphs using adjacency matrix."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds a new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: int) -> List[int]:
        """Returns a 0/1 list for a given vertex that indicates vertices adjacent to it.

        Positions of 1-s in the result list correspond to vertices that are adjacent to a given vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} the following list should be returned for the vertex 0: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns the number of adjacent vertices for a given vertex.

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks whether there is an edge in the graph between 2 given vertices.

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass
```

As you can see, multiple details might need clarification:
* The class constructor expects the number `number_of_vertices`, which defines the number of vertices in the graph. You can assume that vertices are enumerated from *0* to *number_of_vertices - 1*.
* The `add_new_edge` method helps add of new edges to the graph
* The `get_number_of_adjacent_vertices` and `get_list_of_adjacent_vertices` methods are used to get information about vertices adjacent to a vertex of interest.
* The `is_edge` method simply checks whether certain edges of interest are present in the graph.

Please check the unit tests to gain an understanding of how to use the class *in the field*.

<br>

Please use the template `tasks/adjacency_matrix:GraphAdjacencyMatrix` for the implementation.


### Exercise 2: The adjacency dictionary interface for undirected graphs
Your task is to implement the following interface for the `Adjacency matrix` data structure, which is used to represent undirected graphs in memory:

```python
class GraphAdjacencyDictionary:
    """Default interface for supporting undirected graphs using adjacency dictionary."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds a new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: int) -> List[int]:
        """Returns a 0/1 list for a given vertex that indicates vertices adjacent to it.

        Positions of 1-s in the result list correspond to vertices that are adjacent to a given vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} the following list should be returned for the vertex 0: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns the number of adjacent vertices for a given vertex.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks whether there is an edge in the graph between 2 given vertices.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass
```

As you can see, the interface is identical to `GraphAdjacencyMatrix`, but please note that the time complexity requirements are different for the `get_number_of_adjacent_vertices` and `is_edge` methods (due to the different underlying data structures that are used to implement the interfaces).

Please check the unit tests to gain an understanding of how to use the class *in the field*.

<br>

Please use the template `tasks/adjacency_matrix:GraphAdjacencyDictionary` for the implementation.