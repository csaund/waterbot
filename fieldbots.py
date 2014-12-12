
#Have consistent functional expressions which can be broken apart
# format (operator (exp))

import numpy as np
from colorama import Fore
import math
import random

VALID_MOVES = ['^',',','<','>']
MAX_PATH_LEN = 200	#arbitrary, I should play with this.
greens = []	#can I print out colors in the terminal!?
browns = []

class WaterBot():
	def __init__(self):
		self.radius = int((random.random() * 100) % 3)
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
			self.water_radius(field)
			field[self.rpos][self.cpos].runover += 1
			#field.print_field()

	#this enables a "stay in place" move
	#still buggy: if it goes off the side, doesn't do anything.
	#I'll implement it like this because maybe it'll learn to
	# not go off the friggin side
	def water_radius(self, field):
		r_min = max(0, self.rpos - self.radius)
		r_max = min(field.rows, self.rpos + self.radius)
		c_min = max(0, self.cpos - self.radius)
		c_max = min(field.cols, self.cpos + self.radius)
		for i in range(r_min, r_max):
			for j in range(c_min, c_max):
				field[i][j].water += 1



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
			print map(lambda s: s.water, row)
		#one liner?
		#print [map(lambda s: s.water, row) for row in grid]

	def fitness(self):
		watered = 0
		for row in self.field:
			watered += sum(map(lambda s: s.water, row))
		print watered
		runover = 0
		for row in self.field:
			runover += sum(map(lambda s: s.runover, row))
		print runover

		fitness = watered - runover #some function of watered and runover

		return fitness

		#find total watered
		#find total runover
		#find std_dev watered
		#find avg watered
