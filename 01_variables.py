# Variables

# Usamos letras minusculas, numeos y underscore, ademas en snake_case
my_string_variable = "Esta es mi variable de texto"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)


# Concatenacion de variables en print
print(my_string_variable, my_int_variable)
print('Este es mi valor del booleano: ', my_bool_variable)


# Algunas funciones del lenguaje
my_int_to_str_variable = str(my_int_variable) # convierte a str
print(type(my_int_to_str_variable))
print(len(my_string_variable))                # tamaño de una cadena o lista
cadena = "5"
str_a_int = int(cadena)                       # convierte a int
print(type(str_a_int)) 


# Variables en una sola linea, !Cuidado con abusar de esta sintaxis!
num_1, num_2, num_3 = 16, 70, 34
print(num_1)
name, last_name, year_birth = 'Gabriel', 'Cervantes', 1990
print('My name is', name, ', my last name is', last_name, ', and my year of birth is', year_birth)


# input
age = input("¿Cuál es tu edad? ")
print(type(age))
print(age)


# sobreescribir variables
age = 20
print(age)
# cambiando el tipo de la variable (Python no es un lenguaje de tipado fuerte)
age = 'Mi edad es 20'
print(age)


# ¿Forzamos el tipo?
address : str = 'Direccion' # solp lo hacemos de forma visual
address = 657
print(address)
print(type(address))


age : int = input('edad: ')
print(type(age))

