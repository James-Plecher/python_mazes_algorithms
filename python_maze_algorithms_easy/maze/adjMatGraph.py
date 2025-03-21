from typing import List
import time

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph using an adjacency matrix.
    """

    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices
        self.adj_matrix = []  # Adjacency matrix to store edges and wall statuses

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices[label] = len(self.vertices)  # Assign a unique index to each vertex
            # Expand the adjacency matrix to accommodate the new vertex
            for row in self.adj_matrix:
                row.append(False)  # Add a new column for the new vertex
            self.adj_matrix.append([False] * len(self.vertices))  # Add a new row for the new vertex

    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False

        id1 = self.vertices[vert1]
        id2 = self.vertices[vert2]

        # Add edge between vertices
        self.adj_matrix[id1][id2] = True
        self.adj_matrix[id2][id1] = True

        # Update wall status if needed
        self.adj_matrix[id1][id2] = addWall
        self.adj_matrix[id2][id1] = addWall

        return True

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        # startGenTime : float = time.perf_counter()
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False

        idx1 = self.vertices[vert1]
        idx2 = self.vertices[vert2]

        # Update wall status
        self.adj_matrix[idx1][idx2] = wallStatus
        self.adj_matrix[idx2][idx1] = wallStatus
        
        
		# stop timer
        # endGenTime: float = time.perf_counter()
        # print(f'{endGenTime - startGenTime:0.10f}')

        return True

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False
        
        # Remove edge between vertices
        self.adj_matrix[self.vertices[vert1]][self.vertices[vert2]] = False
        self.adj_matrix[self.vertices[vert2]][self.vertices[vert1]] = False

        return True

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False

        # Check if edge exists
        return self.adj_matrix[self.vertices[vert1]][self.vertices[vert2]]

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False
        # Get wall status
        return self.adj_matrix[self.vertices[vert1]][self.vertices[vert2]]

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # startGenTime : float = time.perf_counter()

        if label not in self.vertices:
            return []

        id = self.vertices[label]
        neighbours = []

        # Iterate through adjacent vertices and check for edges
        for neigh, has_edge in enumerate(self.adj_matrix[id]):
            if has_edge:
                for coord, index in self.vertices.items():
                    if index == neigh:
                        neighbours.append(coord)
                        break
                    ##HOPE THIS WORKS OML - returns 
        
        # endGenTime: float = time.perf_counter()
        # print(f'{endGenTime - startGenTime:0.10f}')
        return neighbours
