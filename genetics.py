
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
		self.rpos = 0
		self.cpos = 0

	def random_path(self):
		for i in range(MAX_PATH_LEN):
			self.path.append(random.choice(VALID_MOVES))

	def execute_path(self, field):
		# start in bottom left
		rows = field.rows - 1
		cols = field.cols - 1
		self.rpos = rows
		self.cpos = 0
		field[self.rpos][self.cpos].color = "R"
		# do moves (checking if move is good)
		for move in self.path:
			if move == "^" and self.rpos >= 0:
				self.rpos -= 1
			elif move == "," and self.rpos < rows:
				self.rpos += 1
			elif move == ">" and self.cpos < cols:
				self.cpos += 1
			elif move == "<" and self.cpos >= 0:
				self.cpos -= 1
			#else:
			#	print "Error: invalid move found"
			#self.water_radius()
			field[self.rpos][self.cpos].color = "R"

	#this enables a "stay in place" move
	#def water_radius(self):
		#for i in range(self.radius)



#		# moves alter field


class PlotSquare():
	def __init__(self):
		self.water = 0
		self.runover = 0
		self.color = '-'


class Field():
	def __init__(self, n, m):
		self.field = []
		for row in range(n):
			col = [PlotSquare() for r in range(m)]
			self.field.append(col)
		self.rows = n
		self.cols = m

	#huh this only gives back the row. I'm going to go ahead and not
	# worry about this.
	def __getitem__(self, n):
		return self.field[n]

	def print_field(self):
		for row in self.field:
			print map(lambda s: s.color, row)
		#one liner?
		#print [map(lambda s: s.water, row) for row in grid]

	def fitness(self):
		watered = 0
		for row in self.field:
			watered += sum(map(lambda s: s.water, row))
		runover = 0
		for row in self.field:
			runover += sum(map(lambda s: s.runover, row))

		#find total watered
		#find total runover
		#find std_dev watered
		#find avg watered
