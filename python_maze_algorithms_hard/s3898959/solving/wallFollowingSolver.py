# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Wall following maze solver.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------

from enum import Enum
from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D

## just to assign directions. Could have used normal variables or something else but this felt better
class d(Enum):
    NORTH = 1
    UP = 2
    EAST = 3
    SOUTH = 4
    DOWN = 5
    WEST = 6

class WallFollowingMazeSolver(MazeSolver):
    """
    Wall following solver implementation.  You'll need to complete its implementation for task B.s
    """
    def __init__(self):
        super().__init__()
        self.m_name = "wall"

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        # Define the movement vectors for each direction
        north = Coordinates3D(0, -1, 0)
        up = Coordinates3D(1, 0, 0)
        east = Coordinates3D(0, 0, 1)
        south = Coordinates3D(0, 1, 0)
        down = Coordinates3D(-1, 0, 0)
        west = Coordinates3D(0, 0, -1)
        # Select starting cell
        currentCoord: Coordinates3D = entrance
        currentDirection = d.NORTH
        count = 0
        # test = []
        # x = maze.getExits()
        # for y in x:
        #     test.append(y)

        #while solver agent hasnt exited maze
        while currentCoord not in maze.getExits():
            count +=1
            self.solverPathAppend(currentCoord, False)
            neighbours: list[Coordinates3D] = maze.neighbours(currentCoord)

            # Filter to ones that haven't been visited, are within boundaries, and don't have a wall between them
            rNeigh: list[Coordinates3D] = [
                neigh for neigh in neighbours if not maze.hasWall(currentCoord, neigh) and
                (neigh.getRow() >= 0) and (neigh.getRow() < maze.rowNum(neigh.getLevel())) and
                (neigh.getCol() >= 0) and (neigh.getCol() < maze.colNum(neigh.getLevel()))
            ]
            rNeigh.append(maze.getExits()[0])
            rNeigh.append(maze.getExits()[1])

#DONE NORTH
            ##CHECK which direction solver agent is facing, then proceed to hug the right wall
            #depending on which direction is being face and the walls around the currentCoord to the neighbour nodes

            #its not very elegant but it gets the job done, manually listing all of these insead of cycling through a list
            if currentDirection == d.NORTH:
                if (currentCoord + down) in rNeigh:
                    currentDirection = d.DOWN
                    currentCoord += down

                elif (currentCoord + west) in rNeigh:
                    currentDirection = d.WEST
                    currentCoord += west

                elif (currentCoord + north) in rNeigh:
                    currentDirection = d.NORTH
                    currentCoord += north

                elif (currentCoord + up) in rNeigh:
                    currentDirection = d.UP
                    currentCoord += up

                elif (currentCoord + east) in rNeigh:
                    currentDirection = d.EAST
                    currentCoord += east

                elif (currentCoord + south) in rNeigh:
                    currentDirection = d.SOUTH
                    currentCoord += south
#DONE?
            elif currentDirection == d.EAST:
                if (currentCoord + north) in rNeigh:
                    currentDirection = d.NORTH
                    currentCoord += north

                elif (currentCoord + up) in rNeigh:
                    currentDirection = d.UP
                    currentCoord += up

                elif (currentCoord + east) in rNeigh:
                    currentDirection = d.EAST
                    currentCoord += east

                elif (currentCoord + south) in rNeigh:
                    currentDirection = d.SOUTH
                    currentCoord += south

                elif (currentCoord + down) in rNeigh:
                    currentDirection = d.DOWN
                    currentCoord += down

                elif (currentCoord + west) in rNeigh:
                    currentDirection = d.WEST
                    currentCoord += west
#DONE UP
            elif currentDirection == d.UP:
                if (currentCoord + west) in rNeigh:
                    currentDirection = d.WEST
                    currentCoord += west

                elif (currentCoord + north) in rNeigh:
                    currentDirection = d.NORTH
                    currentCoord += north

                elif (currentCoord + up) in rNeigh:
                    currentDirection = d.UP
                    currentCoord += up

                elif (currentCoord + east) in rNeigh:
                    currentDirection = d.EAST
                    currentCoord += east

                elif (currentCoord + south) in rNeigh:
                    currentDirection = d.SOUTH
                    currentCoord += south

                elif (currentCoord + down) in rNeigh:
                    currentDirection = d.DOWN
                    currentCoord += down
#DONE SOUTH
            elif currentDirection == d.SOUTH:
                if (currentCoord + up) in rNeigh:
                    currentDirection = d.UP
                    currentCoord += up

                elif (currentCoord + east) in rNeigh:
                    currentDirection = d.EAST
                    currentCoord += east

                elif (currentCoord + south) in rNeigh:
                    currentDirection = d.SOUTH
                    currentCoord += south

                elif (currentCoord + down) in rNeigh:
                    currentDirection = d.DOWN
                    currentCoord += down

                elif (currentCoord + west) in rNeigh:
                    currentDirection = d.WEST
                    currentCoord += west

                elif (currentCoord + north) in rNeigh:
                    currentDirection = d.NORTH
                    currentCoord += north
#DONE
            elif currentDirection == d.WEST:
                if (currentCoord + south) in rNeigh:
                    currentDirection = d.SOUTH
                    currentCoord += south

                elif (currentCoord + down) in rNeigh:
                    currentDirection = d.DOWN
                    currentCoord += down

                elif (currentCoord + west) in rNeigh:
                    currentDirection = d.WEST
                    currentCoord += west

                elif (currentCoord + north) in rNeigh:
                    currentDirection = d.NORTH
                    currentCoord += north

                elif (currentCoord + up) in rNeigh:
                    currentDirection = d.UP
                    currentCoord += up

                elif (currentCoord + east) in rNeigh:
                    currentDirection = d.EAST
                    currentCoord += east

            elif currentDirection == d.DOWN:
                if (currentCoord + east) in rNeigh:
                    currentDirection = d.EAST
                    currentCoord += east

                elif (currentCoord + south) in rNeigh:
                    currentDirection = d.SOUTH
                    currentCoord += south

                elif (currentCoord + down) in rNeigh:
                    currentDirection = d.DOWN
                    currentCoord += down

                elif (currentCoord + west) in rNeigh:
                    currentDirection = d.WEST
                    currentCoord += west
                
                elif (currentCoord + north) in rNeigh:
                    currentDirection = d.NORTH
                    currentCoord += north

                elif (currentCoord + up) in rNeigh:
                    currentDirection = d.UP
                    currentCoord += up

            # if count == 200:
            #     break
                        
        self.solverPathAppend(currentCoord, False)
        # self.solverPathAppend(currentCoord, True)
        self.solved(entrance, currentCoord)

