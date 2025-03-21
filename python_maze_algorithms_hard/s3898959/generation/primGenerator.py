# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# Prim's maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------
from random import randint, choice
import random
from collections import deque

from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator


class PrimMazeGenerator(MazeGenerator):
    """
    Prim's algorithm maze generator.  
    TODO: Complete the implementation (Task A)
    """

    def generateMaze(self, maze: Maze3D):
        # TODO: Implement this method for task A.
        #stolen from recur kekekek
        # make sure we start the maze with all walls there
        maze.initCells(True)
        # Random start level
        startLevel = randint(0, maze.levelNum() - 1)
        # Random start coord
        startCoord: Coordinates3D = Coordinates3D(startLevel, randint(0, maze.rowNum(startLevel) - 1), randint(0, maze.colNum(startLevel) - 1))

        ##We select a random starting cell and put it into the visited set.
        visited_set = set()
        visited_set.add(startCoord)

        #We find all the neighbours of this cell, and this forms the frontier set.
        frontier_set = set()
        neighbours = maze.neighbours(startCoord)

        # Add valid neighbours to frontier set
        for x in neighbours:
            #cant let the walls on outsides be seen as neighbors or else it will break the outside wall
            if 0 <= x.getCol() < maze.colNum(x.getLevel()) and 0 <= x.getRow() < maze.rowNum(x.getLevel()):
                frontier_set.add(x)

        #stop once all cells are vidited (again stolen from recur :)
        totalCells = sum([maze.rowNum(l) * maze.colNum(l) for l in range(maze.levelNum())])
        while len(visited_set) < totalCells:
            #using random, choose a random element from a "list" of frontier_set. Random.choice cant iterate through sets or something
            #We select the cell/node with lowest weight in the frontier set
            currentCoord = random.choice(list(frontier_set))

            #We then add that selected cell/node to the visited set
            visited_set.add(currentCoord)

            # Find a neighbor that has already been visited
            visited_neighbors = [neighbour for neighbour in maze.neighbours(currentCoord) if neighbour in visited_set]

            #remove the wall between the selected cell and its neighbour that caused it to be added to the frontier set
            if visited_neighbors:
                prevCoord = random.choice(visited_neighbors)
                maze.removeWall(currentCoord, prevCoord)

            #remove it from the frontier set
            frontier_set.remove(currentCoord)

            #add all of the selected cell’s unvisited neighbours to the frontier set
            for y in maze.neighbours(currentCoord):
                if 0 <= y.getCol() < maze.colNum(y.getLevel()) and 0 <= y.getRow() < maze.rowNum(y.getLevel()):
                    if y not in visited_set:
                        frontier_set.add(y)

        self.m_mazeGenerated = True
