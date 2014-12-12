#main stuff

import genetics

if __name__ == "__main__":
	field = genetics.Field(10,10)
	field.print_field()

	waterbot = genetics.WaterBot()
	waterbot.random_path()
	print waterbot.path