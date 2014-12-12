import fieldbots
import random

def crossover(p1, p2):
	l = len(p1)
	m = 0
	#this can easily be changed to support different path lengths
	while(m < l):
		if (random.random() < 0.9):		#10% chance of splitting at every move! High rate...
			#randomly decide how much to split
			split_at = int((random.random() * 100) % (l - m))
			p1, p2 = cross(p1, p2, m + split_at)
			m += split_at
		else:
			m += 1
	return p1, p2

#given two lists, crosses them over at index n
# l1 = [a, b, c, d, e]
# l2 = [f, g, h, i ,j]
# cross(l1, l2, 3) == ([a, b, c, i, j], [f, g, h, d, e])
def cross(l1, l2, n):
	temp = l1[n:]
	l1[n:] = l2[n:]
	l2[n:] = temp
	return l1, l2

def mutate(p): 
	for m in p:
		if (random.random() < 0.9):		#10% chance of mutation at every move! High rate...
			m = random.choice(fieldbots.VALID_MOVES)		
	return p