def add_two_number(*numbers):
	try:
		acc = 0
		for number in numbers:
			acc += number
		return acc
	except Exception as er:
		print(f"Ocurrió un error {er}")


def subtract_two_number(*numbers):
	try:
		acc = numbers[0]
		for ind, number in enumerate(numbers):
			if ind == 0:
				continue
			acc -= number
		return acc
	except Exception as er:
		print(f"Ocurrió un error {er}")


def multiply_two_number(*numbers):
	try:
		acc = numbers[0]
		for ind, number in enumerate(numbers):
			if ind == 0:
				continue
			acc *= number
		return acc
	except Exception as er:
		print(f"Ocurrió un error {er}")


def divide_two_number(*numbers):
	try:
		acc = numbers[0]
		for ind, number in enumerate(numbers):
			if ind == 0:
				continue
			acc /= number
		return acc
	except Exception as er:
		print(f"Ocurrió un error {er}")
