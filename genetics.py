
#Have consistent functional expressions which can be broken apart
# format (operator (exp))

import numpy as np
from colorama import Fore
import random

VALID_MOVES = ['^',',','<','>']
MAX_PATH_LEN = 200	#arbitrary, I should play with this.

class WaterBot():
	def __init__(self):
		self.radius = (math.random() * 100) % 3
		self.moves = []

	def random_path(self):
		for i in range(MAX_PATH_LEN):
			self.moves.append(random.choice(VALID_MOVES))

greens = []
browns = []


class PlotSquare():
	def __init__(self):
		self.water = 0
		self.runover = 0
		self.color = Fore.GREEN + ' '


def init_field(n, m):
	field = []
	for row in range(n):
		col = [PlotSquare() for r in range(m)]
		field.append(col)
	return field


#def generate_expression():
	


#def crossover(exp1, exp2):

def fitness(grid):
	watered = 0
	for row in grid:
		watered += sum(map(lambda s: s.water, row))
	runover = 0
	for row in grid:
		runover += sum(map(lambda s: s.runover, row))

	#find total watered
	#find total runover
	#find std_dev watered
	#find avg watered


def print_field(grid):
	for row in grid:
		print map(lambda s: s.water, row)
	#one liner?
	#print [map(lambda s: s.water, row) for row in grid]