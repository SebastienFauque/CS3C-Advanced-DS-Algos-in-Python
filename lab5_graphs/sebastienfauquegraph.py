"""
3C Lab5 Student solution - Sebastien Fauque
Topic: Graphs
Application: Graph Abstract Data Type Representation
Description: Contains the Graph class
Development environment: Ubuntu 20.04
Version: Python 3.12.1
Solution File: sebastienfauquegraph.py
Date: 06/11/2024
"""

from sebastienfauquevertex import Vertex
from typing import Optional, List, Iterator, Tuple

class Graph:
    """Implementation of a graph ADT."""
    def __init__(self):
        """Initializes a Graph object."""
        self._vertDictionary = {}
        self._numVertices = 0

    def addVertex(self, node: str) -> Vertex:
        """Adds a new vertex to the graph ADT.

        Params:
            node (str): The identifier of the vertex.
        """
        self._numVertices += 1
        newVertex = Vertex(node)
        self._vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, key: str) -> Optional[Vertex]:
        """Get the vertex object for the given key"""
        return self._vertDictionary.get(key)

    def addEdge(self, fromVertex: str, toVertex: str, weight: int=0) -> None:
        """Add a new directed edge(link) to the graph.

        Params:
            fromVertex (str): The identifier of the from vertex.
            toVertex (str): The identifier of the to vertex.
            weight (int): The weight of the edge.
            """
        if fromVertex not in self._vertDictionary:
            self.addVertex(fromVertex)
        if toVertex not in self._vertDictionary:
            self.addVertex(toVertex)
        self._vertDictionary[fromVertex].addNeighbor(self._vertDictionary[
                                                        toVertex], weight)

    def getVertices(self) -> List[str]:
        """Get all verticies in the graph."""
        return self._vertDictionary.keys()

    def __iter__(self) -> Iterator[Vertex]:
        """Iterate over all vertices in the graph."""
        return iter(self._vertDictionary.values())

    def getEdges(self) -> List[Tuple[str, str, int]]:
        """Gets a list of all edges in the graph."""
        edges = []
        for v in self._vertDictionary.values():
            for w in v.getConnections():
                edges.append((v.getVertexID(), w.getVertexID(), v.getWeight(w)))
        return edges

    def setPrevious(self, current: Vertex) -> None:
        """Sets the previous vertex in the path for the given vertex."""
        self._vertDictionary[current.id].setPrevious(current)
