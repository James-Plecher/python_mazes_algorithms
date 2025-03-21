# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# This is the entry point to run the program.
# Refer to usage() for exact format of input expected to the program.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


import sys
import time
import json
import random
from typing import List

from maze.util import Coordinates
from maze.maze import Maze
from maze.arrayMaze import ArrayMaze
from maze.graphMaze import GraphMaze

from generation.mazeGenerator import MazeGenerator
from generation.recurBackGenerator import RecurBackMazeGenerator


# this checks if Visualizer has been imported properly.
# if not, likely missing some packages, e.g., matplotlib.
# in that case, regardless of visualisation flag, we should set the canVisualise flag to False which will not call the visuslisation part.
canVisualise = True
try:
	from maze.maze_viz import Visualizer
except:
	Visualizer = None
	canVisualise = False

def randomize_config(file_path):
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        config = json.load(file)

    # Randomize rowNum and colNum
    config['rowNum'] = 5 # Choose a suitable range
    config['colNum'] = 5 # Choose a suitable range

	#small range
	# config['rowNum'] = random.randint(5, 20) # Choose a suitable range
    # config['colNum'] = random.randint(5, 20) # Choose a suitable range

	# #medium range
	# config['rowNum'] = random.randint(40, 60) # Choose a suitable range
    # config['colNum'] = random.randint(40, 60) # Choose a suitable range

	# #large range
	# config['rowNum'] = random.randint(80, 100) # Choose a suitable range
	# config['colNum'] = random.randint(80, 100)  # Choose a suitable range

    # # Randomize entrances and exits
	#only places entrance on bottom and exits on right of maze
    config['entrances'] = [[-1, random.randint(-1, config['colNum']-1)] for _ in config['entrances']]
    config['exits'] = [[random.randint(0, config['rowNum']-1), config['colNum']] for _ in config['exits']]
	
    # Save the modified JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)
		

def usage():
	"""
	Print help/usage message.
	"""

	# On Teaching servers, use 'python3'
	# On Windows, you may need to use 'python' instead of 'python3' to get this to work
	print('python3 mazeTester.py', '<configuration file>')
	sys.exit(1)


#
# Main.
#
if __name__ == '__main__':
	# Fetch the command line arguments
	args = sys.argv

	if len(args) != 2:
		print('Incorrect number of arguments.')
		usage()

	for i in range(1):
	# open configuration file		
		fileName: str = args[1]
		randomize_config(fileName)
		with open(fileName,"r") as configFile:
			# use json parser
			configDict = json.load(configFile)

			# assign to variables storing various parameters
			dsApproach: str = configDict['dataStructure']
			rowNum: int = configDict['rowNum']
			colNum: int = configDict['colNum']
			entrances: List[List[int]] = configDict['entrances']
			exits: List[List[int]] = configDict['exits']
			genApproach: str = configDict['generator']
			bVisualise: bool = configDict['visualise']

			#
			# Initialise maze object (which also selects which data structure implementation is used).
			#
			maze: Maze = None
			if dsApproach == 'array':
				maze = ArrayMaze(rowNum, colNum)
			elif dsApproach == 'adjlist':
				maze = GraphMaze(rowNum, colNum, dsApproach)
			elif dsApproach == 'adjmat':
				maze = GraphMaze(rowNum, colNum, dsApproach)
			else:
				print('Unknown data structure approach specified.')
				usage()

			# add the entraces and exits
			for [r,c] in entrances:
				maze.addEntrance(Coordinates(r, c))
			for [r,c] in exits:
				maze.addExit(Coordinates(r, c))

			
			#
			# Generate maze
			#
			generator: MazeGenerator = None
			if genApproach == 'recur':
				generator = RecurBackMazeGenerator()
			else:
				print('Unknown generator approach specified.')
				usage()


		
# Repeat the process 30 times
		
			startGenTime = time.perf_counter()

			generator.generateMaze(maze)

			# stop timer
			endGenTime = time.perf_counter()

			# print(f'Generation {i+1} took {endGenTime - startGenTime:0.6f} seconds')
			# print(f'{endGenTime - startGenTime:0.7f}')

			# add/generate the entrances and exits
			generator.addEntrances(maze)
			generator.addExits(maze)
		#
		# Display maze.
		#
		if bVisualise and canVisualise:
			cellSize = 1
			visualiser = Visualizer(maze, cellSize) 
			visualiser.show_maze()
			
