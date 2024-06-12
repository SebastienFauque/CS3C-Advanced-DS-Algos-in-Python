"""
3C Lab5 Student solution - Sebastien Fauque
Topic: Graphs
Application: Graph Abstract Data Type Representation
Description: ADT of a Graph's vertex representation. The vertex is also known
            as the node or vertices when plural. Nodes/Vertexes are
            connected by edges/links.
Development environment: Ubuntu 20.04
Version: Python 3.12.1
Solution FIle: sebastienfauqueLab5.py
Date: 06/11/2024
"""
from typing import Dict, Optional
class Vertex:
    """Implementation of a vertex/node for a Graph ADT."""
    def __init__(self, node: str):
        """Initializes a vertex.

        Params:
        node (str): The identifier for the vertex/node.
        """
        self._id: str = node
        self._adjacent: Dict[Vertex, int] = {}
        self._visited: bool = False
        self._previous: Optional[Vertex] = None
        self.distance: Optional[int] = None

    def addNeighbor(self, neighbor: 'Vertex', weight: int = 0) -> None:
        """Adds a new node neighbor along a weighted edge.

        Params:
        neighbor (Vertex): The vertex that is a neighbor
        weight (int): The weight/influence of the connection(edge) to the
            neighbor
        """
        self._adjacent[neighbor] = weight

    def getConnections(self) -> Dict['Vertex', int]:
        """Gets all neighbors of the vertex."""
        return self._adjacent.keys()

    def getVertexID(self) -> str:
        """Get the identifier of this vertex."""
        return self._id

    def getWeight(self, neighbor: 'Vertex') -> int:
        """Gets the wegiht of the edge to a neighbor."""
        return self._adjacent[neighbor]

    def setDistance(self, dist: int) -> None:
        """Sets the distance attribute.

        Params:
            dist (int): The distance to the next edge."""
        self.distance = dist

    def getDistance(self) -> int:
        """Gets the distance."""
        return self.distance

    def setPrevious(self, prev: 'Vertex') -> None:
        """Sets the previous vertex in the path.

        Params:
            prev (Vertex): The previous vertex/node."""
        self._previous = prev

    def __str__(self) -> str:
        """Gets the string representation of the vertex."""

        return (f"{self._id} adjacent:"
                f" {[(x._id, self._adjacent[x]) for x in self._adjacent]}")
