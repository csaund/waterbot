#main stuff

import genetics

if __name__ == "__main__":
	field = genetics.Field(10,10)

	waterbot = genetics.WaterBot()
	waterbot.random_path()
	print waterbot.path

	waterbot.execute_path(field)
	field.print_field()