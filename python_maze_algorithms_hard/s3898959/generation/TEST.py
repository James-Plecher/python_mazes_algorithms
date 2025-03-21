# # # -------------------------------------------------------------------
# # # PLEASE UPDATE THIS FILE.
# # # Wilson's algorithm maze generator.
# # #
# # # __author__ = 'Jeffrey Chan'
# # # __copyright__ = 'Copyright 2024, RMIT University'
# # # -------------------------------------------------------------------


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
#         #Perform a random walk from this 2nd selected cell, until this random walk visits a cell that is finalised
#             while True:
#                     #get neighbours in range and not in temp list
#                 print("TempySecondy ", tempySecondy)
#                 neighbours : list[Coordinates3D] = maze.neighbours(tempySecondy)
#                 for x in neighbours:
#                     print(x)
#                 rNeigh : list[Coordinates3D] = [neigh for neigh in neighbours if \
#                                             neigh.getRow() >= 0 and neigh.getRow() < maze.rowNum(neigh.getLevel()) and\
#                                             neigh.getCol() >= 0 and neigh.getCol() < maze.colNum(neigh.getLevel())]
#                 print("NINININININEIGH")
#                 for x in rNeigh:
#                     print(x)
#                     #choose random neighbour to walk to
                
#                 temp = random.choice(rNeigh)

#                 if temp in fin:
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
#                     if temp in tempList:
#                         tempList = tempList[:tempList.index(temp) + 1]
#                     else:
#                         tempList.append(temp)
#                         tempySecondy = temp
        
#         self.m_mazeGenerated = True
from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator
from random import choice

class WilsonMazeGenerator(MazeGenerator):
    """
    Wilson algorithm maze generator.
    """

    def generateMaze(self, maze: Maze3D):
        # Initialize the maze with walls between all pairs of adjacent cells
        maze.initCells(True)

        # Initialize sets of finalized and unfinalized cells
        unfin = set()
        fin = set()
        for l in range(maze.levelNum()):
            for r in range(maze.rowNum(l)):
                for c in range(maze.colNum(l)):
                    coord = Coordinates3D(l, r, c)
                    unfin.add(coord)

        # Randomly select the starting cell and mark it as finalized
        startCoord = choice(list(unfin))
        fin.add(startCoord)
        unfin.remove(startCoord)

        while unfin:
            # Select another cell, at random, that isn’t finalized yet
            secondCoord = choice(list(unfin))
            tempList = [secondCoord]

            # Perform a random walk from this second selected cell
            while True:
                current = tempList[-1]
                neighbours = maze.neighbours(current)

                # Filter neighbours to ensure they are within bounds
                rNeigh = [neigh for neigh in neighbours if \
                          0 <= neigh.getRow() < maze.rowNum(neigh.getLevel()) and \
                          0 <= neigh.getCol() < maze.colNum(neigh.getLevel())]

                # Choose a random neighbour to walk to
                nextCell = choice(rNeigh)

                if nextCell in fin:
                    # Carve a path from the initial selected cell to the final cell
                    for i in range(len(tempList) - 1):
                        maze.removeWall(tempList[i], tempList[i + 1])
                        fin.add(tempList[i])
                        unfin.remove(tempList[i])

                    fin.add(tempList[-1])
                    unfin.remove(tempList[-1])
                    break
                else:
                    if nextCell in tempList:
                        # Avoid loops by truncating the loop
                        loop_index = tempList.index(nextCell)
                        tempList = tempList[:loop_index + 1]
                    else:
                        tempList.append(nextCell)

        self.m_mazeGenerated = True

