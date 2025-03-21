# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Pledge maze solver.

# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D
from enum import Enum
from random import choice
import time

class d(Enum):
    NORTH = 1
    UP = 2
    EAST = 3
    SOUTH = 4
    DOWN = 5
    WEST = 6

class PledgeMazeSolver(MazeSolver):
    """
    Pledge solver implementation.  You'll need to complete its implementation for task B.
    """

    def __init__(self):
        super().__init__()
        self.m_name = "pledge"

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        north = Coordinates3D(0, -1, 0)
        up = Coordinates3D(1, 0, 0)
        east = Coordinates3D(0, 0, 1)
        south = Coordinates3D(0, 1, 0)
        down = Coordinates3D(-1, 0, 0)
        west = Coordinates3D(0, 0, -1)

        currentCoord: Coordinates3D = entrance
        initialDirection = choice((d.NORTH, d.SOUTH, d.EAST, d.WEST))
        # initialDirection = d.EAST
        # moveForward = east
        if initialDirection == d.NORTH:
            moveForward = north
        elif initialDirection == d.SOUTH:
            moveForward = south
        elif initialDirection == d.EAST:
            moveForward = east
        elif initialDirection == d.WEST:
            moveForward = west
        elif initialDirection == d.UP:
            moveForward = up
        elif initialDirection == d.DOWN:
            moveForward = down

        currentDirection = initialDirection
        angleCounter = 0
        count = 0
        l = 0
        r = 0

        while currentCoord not in maze.getExits():
            count += 1
            self.solverPathAppend(currentCoord, False)
            neighbours: list[Coordinates3D] = maze.neighbours(currentCoord)

            rNeigh: list[Coordinates3D] = [
                neigh for neigh in neighbours if not maze.hasWall(currentCoord, neigh) and
                (neigh.getRow() >= 0) and (neigh.getRow() < maze.rowNum(neigh.getLevel())) and
                (neigh.getCol() >= 0) and (neigh.getCol() < maze.colNum(neigh.getLevel()))
            ]
            rNeigh.append(maze.getExits()[0])
            rNeigh.append(maze.getExits()[1])
            # t = input()
            # if count == 8000:
            #     break
            if angleCounter == 0:
                print("000000000000000000000000", currentDirection)

            #THIS IS PLEDGE part, checks for angle to be 0 (left - right turns = 0) and for a wall in the prefered direction
            #if there is no wall, pledge can keep going, otherwise it switches back to wall follower beloow
            if angleCounter == 0 and (currentCoord + moveForward) in rNeigh:
            # if l - r == 0 and (currentCoord + moveForward) in rNeigh:
                currentCoord += moveForward
                # currentDirection = d.NORTH
                print("NEIENEINEINEN")
            
            else:
                print(count, ": Current Direction: ", currentDirection, "Cureent Coord", currentCoord, "Angle: ", angleCounter)
                ##BELOW is the same as the Wall follwer, except for counting the angles/turns. 
                if currentDirection == d.NORTH:
                    if (currentCoord + down) in rNeigh:
                        currentDirection = d.DOWN
                        currentCoord += down
                        angleCounter += 1.5
                        
                    elif (currentCoord + west) in rNeigh:
                        currentDirection = d.WEST
                        currentCoord += west
                        angleCounter += 1

                    elif (currentCoord + north) in rNeigh:
                        currentDirection = d.NORTH
                        currentCoord += north

                    elif (currentCoord + up) in rNeigh:
                        currentDirection = d.UP
                        currentCoord += up
                        angleCounter -= 0.5
                    elif (currentCoord + east) in rNeigh:
                        currentDirection = d.EAST
                        currentCoord += east
                        angleCounter -= 1
                    elif (currentCoord + south) in rNeigh:
                        currentDirection = d.SOUTH
                        currentCoord += south
                        angleCounter -= 2
                        
                elif currentDirection == d.EAST:
                    if (currentCoord + north) in rNeigh:
                        currentDirection = d.NORTH
                        currentCoord += north
                        angleCounter += 1
                    elif (currentCoord + up) in rNeigh:
                        currentDirection = d.UP
                        currentCoord += up
                        angleCounter += 0.5
                    elif (currentCoord + east) in rNeigh:
                        currentDirection = d.EAST
                        currentCoord += east
                    elif (currentCoord + south) in rNeigh:
                        currentDirection = d.SOUTH
                        currentCoord += south
                        angleCounter -= 1
                    elif (currentCoord + down) in rNeigh:
                        currentDirection = d.DOWN
                        currentCoord += down
                        angleCounter -= 1.5
                    elif (currentCoord + west) in rNeigh:
                        currentDirection = d.WEST
                        currentCoord += west
                        angleCounter -= 2

                elif currentDirection == d.UP:
                    if (currentCoord + west) in rNeigh:
                        currentDirection = d.WEST
                        currentCoord += west
                        angleCounter += 1.5
                    elif (currentCoord + north) in rNeigh:
                        currentDirection = d.NORTH
                        currentCoord += north
                        angleCounter += 0.5
                    elif (currentCoord + up) in rNeigh:
                        currentDirection = d.UP
                        currentCoord += up
                    elif (currentCoord + east) in rNeigh:
                        currentDirection = d.EAST
                        currentCoord += east
                        angleCounter -= 0.5
                    elif (currentCoord + south) in rNeigh:
                        currentDirection = d.SOUTH
                        currentCoord += south
                        angleCounter -= 1.5
                    elif (currentCoord + down) in rNeigh:
                        currentDirection = d.DOWN
                        currentCoord += down
                        angleCounter -= 2

                elif currentDirection == d.SOUTH:
                    if (currentCoord + up) in rNeigh:
                        currentDirection = d.UP
                        currentCoord += up
                        angleCounter += 1.5
                    elif (currentCoord + east) in rNeigh:
                        currentDirection = d.EAST
                        currentCoord += east
                        angleCounter += 1
                    elif (currentCoord + south) in rNeigh:
                        currentDirection = d.SOUTH
                        currentCoord += south
                    elif (currentCoord + down) in rNeigh:
                        currentDirection = d.DOWN
                        currentCoord += down
                        angleCounter -= 0.5
                    elif (currentCoord + west) in rNeigh:
                        currentDirection = d.WEST
                        currentCoord += west
                        angleCounter -= 1
                    elif (currentCoord + north) in rNeigh:
                        currentDirection = d.NORTH
                        currentCoord += north
                        angleCounter -= 2

                elif currentDirection == d.WEST:
                    if (currentCoord + south) in rNeigh:
                        currentDirection = d.SOUTH
                        currentCoord += south
                        angleCounter += 1
                    elif (currentCoord + down) in rNeigh:
                        currentDirection = d.DOWN
                        currentCoord += down
                        angleCounter += 0.5
                    elif (currentCoord + west) in rNeigh:
                        currentDirection = d.WEST
                        currentCoord += west
                    elif (currentCoord + north) in rNeigh:
                        currentDirection = d.NORTH
                        currentCoord += north
                        angleCounter -= 1
                    elif (currentCoord + up) in rNeigh:
                        currentDirection = d.UP
                        currentCoord += up
                        angleCounter -= 1.5
                    elif (currentCoord + east) in rNeigh:
                        currentDirection = d.EAST
                        currentCoord += east
                        angleCounter -= 2

                elif currentDirection == d.DOWN:
                    if (currentCoord + east) in rNeigh:
                        currentDirection = d.EAST
                        currentCoord += east
                        angleCounter += 1.5
                    elif (currentCoord + south) in rNeigh:
                        currentDirection = d.SOUTH
                        currentCoord += south
                        angleCounter += 0.5
                    elif (currentCoord + down) in rNeigh:
                        currentDirection = d.DOWN
                        currentCoord += down
                    elif (currentCoord + west) in rNeigh:
                        currentDirection = d.WEST
                        currentCoord += west
                        angleCounter -= 0.5
                    elif (currentCoord + north) in rNeigh:
                        currentDirection = d.NORTH
                        currentCoord += north
                        angleCounter -= 1.5
                    elif (currentCoord + up) in rNeigh:
                        currentDirection = d.UP
                        currentCoord += up
                        angleCounter -= 2
                
            # if count == 2000:
            #     break
        self.solverPathAppend(currentCoord, False)
        self.solved(entrance, currentCoord)

