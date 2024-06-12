"""
3C Lab5 Student Driver
Topic: Graphs
Application: Graph Abstract Data Type Representation
Description: Test driver and demo code for implementation of a Graph. Contains
             tests using Pytest and demo output.
Development environment: Ubuntu 20.04
Version: Python 3.12.1
Solution File: demo5_sebastienfauque.py
Date: 06/11/2024
"""
import pytest
from sebastienfauquegraph import Graph
from sebastienfauquevertex import Vertex

def test_vertex_creation():
    v = Vertex('a')
    assert v.getVertexID() == 'a'
    assert v._adjacent == {}

def test_add_neighbor():
    v1 = Vertex('a')
    v2 = Vertex('b')
    v1.addNeighbor(v2, 4)
    assert v1._adjacent[v2] == 4
    assert list(v1.getConnections()) == [v2]

def test_get_weight():
    v1 = Vertex('a')
    v2 = Vertex('b')
    v1.addNeighbor(v2, 4)
    assert v1.getWeight(v2) == 4

def test_distance_and_previous():
    v = Vertex('a')
    v.setDistance(10)
    v.setPrevious(Vertex('b'))
    assert v.getDistance() == 10
    assert v._previous.getVertexID() == 'b'

def test_vertex_str():
    v1 = Vertex('a')
    v2 = Vertex('b')
    v1.addNeighbor(v2, 4)
    assert str(v1) == "a adjacent: [('b', 4)]"

def test_graph_creation():
    g = Graph()
    assert g._numVertices == 0
    assert g._vertDictionary == {}

def test_add_vertex():
    g = Graph()
    g.addVertex('a')
    assert 'a' in g._vertDictionary
    assert g._numVertices == 1

def test_add_edge():
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addEdge('a', 'b', 4)
    assert g._vertDictionary['a']._adjacent[g._vertDictionary['b']] == 4

def test_get_vertex():
    g = Graph()
    g.addVertex('a')
    assert g.getVertex('a').getVertexID() == 'a'
    assert g.getVertex('b') is None

def test_get_vertices():
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    assert set(g.getVertices()) == {'a', 'b'}

def test_get_edges():
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addEdge('a', 'b', 4)
    g.addEdge('a', 'c', 1)
    g.addEdge('b', 'a', 3)
    assert set(g.getEdges()) == {('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 3)}

def test_graph_str():
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addEdge('a', 'b', 4)
    assert str(g._vertDictionary['a']) == "a adjacent: [('b', 4)]"

def main():
    g = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e']
    for vertex in vertices:
        g.addVertex(vertex)

    edges = [('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 3), ('b', 'd', 2), ('c', 'a', 1), ('c', 'b', 5)]
    for edge in edges:
        g.addEdge(edge[0], edge[1], edge[2])

    print("Adjacency list of the graph:")
    for v in g:
        print(v)

    print("\nList of all edges in the graph:")
    print(g.getEdges())

if __name__ == "__main__":
    main()

# Program test run validation:
# Adjacency list of the graph:
# a adjacent: [('b', 4), ('c', 1)]
# b adjacent: [('a', 3), ('d', 2)]
# c adjacent: [('a', 1), ('b', 5)]
# d adjacent: []
# e adjacent: []

# List of all edges in the graph:
# [('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 3), ('b', 'd', 2), ('c', 'a', 1), ('c', 'b', 5)]
