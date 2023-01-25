# Exceptions

print("\n" + ("*~" * 10), "Manejo de excepciones: try - except" ,("*~" * 10))

number_one = 5
number_two = "1"

try:
	print(f"{number_one} + {number_two} = {number_one + number_two}")
	print("No hay errores")
except:
	print("Se produjo un error")


# Flujo cimpleto del maneji de errores
print("\n" + ("*~" * 10), "Flujo completo: try - except - else - finally" ,("*~" * 10))

try:
	print(f"{number_one} + {number_two} = {number_one + number_two}")
	print("try: No hay errores - exception de flujo completo")
except:
	print("except: Se produjo un error - excepcion de flujo completo")
else:
	print("else: Me ejecuto si lo del try es correcto")
finally:
	print("Finally: Siempre me ejecutaré")


# Excepciones por tipo
print("\n" + ("*~" * 10), "Excepciones por tipo" ,("*~" * 10))

try:
	print(f"{number_one} + {number_two} = {number_one + number_to}")
	print("try: No hay errores")
except ValueError:
	print("Error de ValueError")
except TypeError:
	print("Error de TypeError")
except NameError:
	print("Error de NameError")

try:
	print(f"{number_one} + {number_two} = {number_one + number_two}")
	print("try: No hay errores")
except ValueError:
	print("Error de ValueError")
except TypeError:
	print("Error de TypeError")
except NameError:
	print("Error de NameError")


# Capturando la informacion de la excepcion
print("\n" + ("*~" * 10), "Información de la excepcion" ,("*~" * 10))

try:
	print(f"{number_one} + {number_two} = {number_one + number_to}")
	print("try: No hay errores")
except ValueError as error:
	print(f"ValueError: {error}")
except TypeError as error:
	print(f"TypeError: {error}")
except NameError as error:
	print(f"NameError: {error}")

try:
	print(f"{number_one} + {number_two} = {number_one + number_to}")
	print("try: No hay errores")
except Exception as error:
	print(f"Exception: {error}")
