#main stuff

import fieldbots as fb

if __name__ == "__main__":
	field = fb.Field(10,10)

	waterbot = fb.WaterBot()
	waterbot.random_path()
	print waterbot.path

	waterbot.execute_path(field)
	field.print_field()
	print field.fitness()