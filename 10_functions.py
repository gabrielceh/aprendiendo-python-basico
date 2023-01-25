# Functions

# declarando funciones
print("\n" + ("*~" * 10), "Declarando funciones" ,("*~" * 10))

def my_first_function():
	print('Usamos la palabra reservada "def"')
	print('def my_first_function():')
	print("\t# código")

my_first_function()
my_first_function()


# Parametros
print("\n" + ("*~" * 10), "Parametros de funciones" ,("*~" * 10))

def sum_two_values(first_number:int, second_number):
	if 	isinstance(first_number, int) and isinstance(second_number, int):
		print(f"{first_number} + {second_number} = {first_number + second_number}")
	else:
		print("Deben ser numeros enteros")

sum_two_values(3, 7)
sum_two_values(3, "7")


# retornar parametros
print("\n" + ("*~" * 10), "Retornar parametros de funciones" ,("*~" * 10))

def diff_two_values(first_val, second_val):
	diff = first_val - second_val
	return diff

difference = diff_two_values(10, 6)
print(difference)
print(diff_two_values(17, 4))


# Argumentos clave
print("\n" + ("*~" * 10), "Parametros claves de funciones" ,("*~" * 10))

def print_full_name(first_name, last_name):
	print(f"{first_name} {last_name}")

print_full_name(last_name="Cervantes", first_name="Gabriel")


# parametros por defecto
print("\n" + ("*~" * 10), "Parametros por defecto de funciones" ,("*~" * 10))

def grettings(name, gretting = "Buenos dias"):
	print(f"{gretting}, {name}")

grettings("Gabriel", "Buenas noches")
grettings("Angie")


# Paramtros arbitrarios
print("\n" + ("*~" * 10), "Parametros arbirtrarios en funciones" ,("*~" * 10))

def print_names(*names):
	print(names, type(names))
	for name in names:
		print(name.upper())

print_names("Gabriel")
print_names('Gabriel','Angie','Mauricio','Vilma')
