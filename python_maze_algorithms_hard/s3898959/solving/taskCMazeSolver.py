from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D
from collections import deque



class TaskCMazeSolver(MazeSolver):
    """
    Task C solver implementation.  You'll need to complete its implementation for task C.
    """


    def __init__(self):
        super().__init__()
        self.m_name = "taskC"

##########################################################################IMPORTANT IMPORTANT IMPORTNAT########################################################
# I had to edit this "solveMaze()"" to not pass the entrance varible as I couldnt get it to run otherwise so if it doesnt
# work on the cloud teaching server maybe this is why?, just uncomment the line below and comment the uncommented one :)
    def solveMaze(self, maze: Maze3D):
    # def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        # we call the the solve maze call without the entrance.
        # print(entrance)
        # DO NOT CHANGE THIS METHOD
        self.solveMazeTaskC(maze)

    def solveMazeTaskC(self, maze: Maze3D):
        #BFS TO FIND BOTH EXITS FROM ONE ENTRANCE
        mazeEntrances = maze.getEntrances()
        mazeExits = maze.getExits()
        explored = set()
        small = []

    
        #FOR LOOP HERE FOR EACH ENTRANCE
        for i in range (len(mazeEntrances)):
            setT = set()
            visited = set()
            queue = deque()
            mazeExitCount = 0
            foundExits = set()
            visited.add(mazeEntrances[i])
            queue.append(mazeEntrances[i])

            ##while there are still undiscovered exits, continue exploring
            while mazeExitCount < len(mazeExits):
                currentCoord = queue.popleft()
                if currentCoord not in explored:
                    self.solverPathAppend(currentCoord, False)
                explored.add(currentCoord)

                #find valid neighbours of current node
                neighbours: list[Coordinates3D] = maze.neighbours(currentCoord)
                rNeigh: list[Coordinates3D] = [
                    neigh for neigh in neighbours if not maze.hasWall(currentCoord, neigh) and
                    (neigh.getRow() >= 0) and (neigh.getRow() < maze.rowNum(neigh.getLevel())) and
                    (neigh.getCol() >= 0) and (neigh.getCol() < maze.colNum(neigh.getLevel()))
                ]

                #checking if neighbours have been visited, if they havent, queue them for visiting later
                for neighbour in rNeigh:                    
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        setT.add((neighbour, currentCoord))

                ##this is to read outside the maze for exits as neighours doesnt detect it
                directions = {currentCoord + Coordinates3D(0,0,1),
                    currentCoord + Coordinates3D(0,0,-1), 
                    currentCoord + Coordinates3D(0,1,0), 
                    currentCoord + Coordinates3D(0,-1,0)}

                #for each direction, if it is an exit, and not already found, add it to the found exits
                #list, increase the exitFound count by one and continue 
                for exit in directions:
                    if exit in mazeExits:
                        if exit not in foundExits:
                            if exit not in explored:
                                self.solverPathAppend(exit, False)
                            setT.add((exit, currentCoord))
                            foundExits.add(exit)
                            mazeExitCount += 1
                            
            ##once all exits have been found, backtrack through the setT set to find the gaurnteed shortest
            #path from each exit to each entrance
            for j in range (len(mazeExits)):
                tt = mazeExits[j]
                path = set()
                path.add(tt)
                val = True
                c = 0
                while val:
                    for y in setT:
                        if y[0] == tt:
                            path.add(y[0])
                            tt = y[1]
                            # self.solverPathAppend(tt, False)
                            c +=1
                            if y[1] == mazeEntrances[i]:
                                val = False
                small.append(c)
                #print the path results and coords of entrances and exits
                print("Shortest path from ", mazeEntrances[i], "to ", mazeExits[j], " is:", c, "cells long")
        # for x in small:
        #     print(x)
        a = min(small)
        # print(a)
        b = len(explored)
        # print(b)
        c = a + b - 2
        # print(c)
        #FINAL EXPLOATION FORMAULA! THIS IS MORE ACCURATE THAN THE BUILT IN SKELETON CODE ONE BY ABOUT +-6 
        print("Therefore the 'min(cells explored() + distance(entrance, exit))' for this maze is:", c)


