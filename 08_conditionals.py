# Conditionals

my_condition = False

if my_condition:
	print("my_condition is True")

print("La ejecucion continua")

age = 17

if age >= 18:
	print("Es mayor de edad")

if age < 18:
	print('Es menor de edad')	


# if else
print(("*" * 10), "if else" ,("*" * 10))
age = 21
if age  >= 18 and age > 20:
	print("Es mayor de edad y puede tomar")
else:
	print("Es menor de edad o Es mayor de edad pero no puede tomar")


my_string = "   ".strip(" ")

if my_string:
	print(f"my_string: {my_string}")
else:
	print(f"my_string esta vacia")

if not my_string:
	print("La cadena esta vacia, agegale valor")


# elif
print(("*" * 10), "elif" ,("*" * 10))

my_num = 5 * 5

if my_num <= 10:
	print("my_num es menor o igual a 10")

elif my_num > 10 and my_num < 20:
	print("my_num es mayor a 10 y menor a 20")

else:
	print("my_num es mayor a 20")


# short
print(("*" * 10), "short hand" ,("*" * 10))

is_online = False

print("Estoy en linea") if is_online else print("No estoy en linea")





