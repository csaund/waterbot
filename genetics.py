
#Have consistent functional expressions which can be broken apart
# format (operator (exp))

import numpy as np
from colorama import Fore
import math
import random

VALID_MOVES = ['^',',','<','>']
MAX_PATH_LEN = 200	#arbitrary, I should play with this.
greens = []
browns = []

class WaterBot():
	def __init__(self):
		self.radius = (random.random() * 100) % 3
		self.path = []

	def random_path(self):
		for i in range(MAX_PATH_LEN):
			self.path.append(random.choice(VALID_MOVES))


class PlotSquare():
	def __init__(self):
		self.water = 0
		self.runover = 0
		self.color = Fore.GREEN + ' '


class Field():
	def __init__(self, n, m):
		self.field = []
		for row in range(n):
			col = [PlotSquare() for r in range(m)]
			self.field.append(col)

	def print_field(self):
		for row in self.field:
			print map(lambda s: s.water, row)
	#one liner?
	#print [map(lambda s: s.water, row) for row in grid]



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
