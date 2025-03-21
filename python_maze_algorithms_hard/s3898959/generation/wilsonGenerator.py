# # -------------------------------------------------------------------
# # PLEASE UPDATE THIS FILE.
# # Wilson's algorithm maze generator.
# #
# # __author__ = 'Jeffrey Chan'
# # __copyright__ = 'Copyright 2024, RMIT University'
# # -------------------------------------------------------------------


# from maze.maze3D import Maze3D
# from maze.util import Coordinates3D
# from generation.mazeGenerator import MazeGenerator
# from random import randint, choice
# import random

# class WilsonMazeGenerator(MazeGenerator):
#     """
#     Wilson algorithm maze generator.
#     TODO: Complete the implementation (Task A)
#     """
#     def generateMaze(self, maze:Maze3D):
#         # TODO: Implement this method for task A.
#         #maze with walls between all pairs of adjacent cells
#         maze.initCells(True)

#         #every cell in the maze is considered as not finalised.
#         unfin = set()
#         fin = set()
#         for l in range(maze.levelNum()):
#             for r in range(maze.rowNum(l)):
#                 for c in range(maze.colNum(l)):
#                     coord = Coordinates3D(l, r, c)
#                     unfin.add(coord)

#         #randomly selecting a starting cell, that is the first cell to be considered as finalised
#         startCoord = random.choice(list(unfin))
#         fin.add(startCoord)
#         unfin.remove(startCoord)

#         while unfin:
#             #Select another cell, at random, that isn’t finalised yet
#             secondCoord = random.choice(list(unfin))
#             tempySecondy = secondCoord
#             tempList = [tempySecondy]
#             #Perform a random walk from this 2nd selected cell, until this random walk visits a cell that is finalised
#             while True:
#                     #get neighbours in range and not in temp list
#                 neighbours : list[Coordinates3D] = maze.neighbours(tempySecondy)
                
#                 rNeigh : list[Coordinates3D] = [neigh for neigh in neighbours if \
#                                             neigh.getRow() >= 0 and neigh.getRow() < maze.rowNum(neigh.getLevel()) and\
#                                             neigh.getCol() >= 0 and neigh.getCol() < maze.colNum(neigh.getLevel())]
#                 if len(rNeigh) == 0:
#                     break
               
#                 temp = random.choice(rNeigh)

#                 if temp in tempList:
#                     tempList = tempList[:tempList.index(temp) + 1]

#                 elif temp in fin:
#                         # Iterate over pairs of adjacent coordinates in tempList
#                         #####THIS MIGHT CAUSE AN INDEXING ISSUE#####
#                     for index in range(len(tempList) - 1):
#                         currentCoord = tempList[index]
#                         nextCoord = tempList[index + 1]
                        
#                         # Remove the wall between currentCoord and nextCoord and set to finalised
#                         maze.removeWall(currentCoord, nextCoord)
#                         fin.add(currentCoord)
#                         unfin.remove(currentCoord)

#                     fin.add(tempList[-1])
#                     unfin.remove(tempList[-1])
#                     break
                        
#                 else:
#                     tempList.append(temp)
#                     tempySecondy = temp
        
#         self.m_mazeGenerated = True
#DUHDQUDHWIUQHU FUUUUUUUCK doing something wrong :/



##restarts attempt 2
from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator
from random import choice

class WilsonMazeGenerator(MazeGenerator):
    """
    Wilson's algorithm maze generator.
    TODO: Complete the implementation (Task A)
    """

    def generateMaze(self, maze: Maze3D):
        # TODO: Implement this method for task A.
        # starts with a maze with walls between all pairs of adjacent cells
        maze.initCells(True)

        # Also initially every cell in the maze is considered as not finalised
        unfin = set()
        fin = set()
        for l in range(maze.levelNum()):
            for r in range(maze.rowNum(l)):
                for c in range(maze.colNum(l)):
                    coord = Coordinates3D(l, r, c)
                    unfin.add(coord)

        # randomly selecting a starting cell, that is the first cell to be considered as finalised
        startCoord = choice(list(unfin))
        fin.add(startCoord)
        unfin.remove(startCoord)

        #while unfinalsied has elements in it (not finished)
        while unfin:
            # Select another cell, at random, that isn’t finalised ye
            currentCoord = choice(list(unfin))
            path = [currentCoord]

            # Perform a random walk from this 2nd selected cell, until this random walk visits a cell that is finalised
            while currentCoord not in fin:
                neighbours : list[Coordinates3D] = maze.neighbours(currentCoord)
                
                valid_neigh : list[Coordinates3D] = [neigh for neigh in neighbours if \
                                            neigh.getRow() >= 0 and neigh.getRow() < maze.rowNum(neigh.getLevel()) and\
                                            neigh.getCol() >= 0 and neigh.getCol() < maze.colNum(neigh.getLevel())]

                #Select a random valid neighbor
                nextCoord = choice(valid_neigh)

                # If the randomly choses neighbour is a node that is already in the path but not finalised, remove it from path
                if nextCoord in path:
                    path = path[:path.index(nextCoord) + 1]

                else:
                    #add to path is condidtions are met
                    path.append(nextCoord)
                
                #move to next node
                currentCoord = nextCoord

            # and carve a path from that cell to the last visited cell
            for i in range(len(path) - 1):
                if path[i] not in fin:
                    fin.add(path[i])
                    unfin.remove(path[i])
                    maze.removeWall(path[i], path[i + 1])

        self.m_mazeGenerated = True
