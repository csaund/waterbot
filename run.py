#main stuff

import fieldbots as fb
import genetics as gen

BATCH_SIZE = 100 	#arbitrary batch size.
GENERATIONS = 100 #arbitrary generations. This should converge, I hope.


if __name__ == "__main__":
	#starting population
	population = []
	field = fb.Field()
	for bot in range(BATCH_SIZE):
		b = fb.WaterBot()
		b.random_path()
		b.execute_path(field)
		population.append((b, field.fitness()))

	for gen in range(GENERATIONS):
		#sort population by fitness
		population.sort(key=lambda x: x[1])
		#keep best half
		population = population[50:]

		#randomly segment into 3 lists
			#crossover
			#mutation
			#leave the same

		#leave most fit 50 in the population?





