#main stuff

import genetics

if __name__ == "__main__":
	field = genetics.init_field(10,10)
	genetics.print_field(field)
	genetics.fitness(field)