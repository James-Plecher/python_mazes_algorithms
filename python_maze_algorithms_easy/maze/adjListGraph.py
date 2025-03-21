from typing import List, Dict, Tuple
import time
from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph using an adjacency list.
    """

    def __init__(self):
        # Initialize the adjacency list as a dictionary.
        # Each key is a vertex, and the value is a list of tuples (neighbour, wallStatus)
        self.adjList: Dict[Coordinates, List[Tuple[Coordinates, bool]]] = {}

    def addVertex(self, label: Coordinates):
        # Add a vertex only if it is not already in the adjacency list
        if label not in self.adjList:
            self.adjList[label] = []

    def addVertices(self, vertLabels: List[Coordinates]):
        # Add multiple vertices
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        # Add an undirected edge between vert1 and vert2 with wall status
        if vert1 in self.adjList and vert2 in self.adjList and not self.hasEdge(vert1, vert2):
            self.adjList[vert1].append((vert2, addWall))
            self.adjList[vert2].append((vert1, addWall))
            return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        # startGenTime : float = time.perf_counter()
        updated = False
        if vert1 in self.adjList and vert2 in self.adjList:
            for i, (neighbor, _) in enumerate(self.adjList[vert1]):
                if neighbor == vert2:
                    self.adjList[vert1][i] = (neighbor, wallStatus)
                    updated = True
                    break
            if updated:
                for i, (neighbor, _) in enumerate(self.adjList[vert2]):
                    if neighbor == vert1:
                        self.adjList[vert2][i] = (neighbor, wallStatus)
                        break
        # endGenTime: float = time.perf_counter()
        # print(f'{endGenTime - startGenTime:0.10f}')
        return updated

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Remove the undirected edge between vert1 and vert2
        if self.hasEdge(vert1, vert2):
            self.adjList[vert1] = [pair for pair in self.adjList[vert1] if pair[0] != vert2]
            self.adjList[vert2] = [pair for pair in self.adjList[vert2] if pair[0] != vert1]
            return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        # Check if the vertex exists in the graph
        return label in self.adjList

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Check if there is an edge between vert1 and vert2
        return any(neighbor == vert2 for neighbor, _ in self.adjList.get(vert1, []))

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Get the wall status between vert1 and vert2, if the edge exists
        for neighbor, wallStatus in self.adjList.get(vert1, []):
            if neighbor == vert2:
                return wallStatus
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # Return a list of neighbors for the given vertex
        return [neighbor for neighbor, _ in self.adjList.get(label, [])]

    
