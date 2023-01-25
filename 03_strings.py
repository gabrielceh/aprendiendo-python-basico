# STRINGS

my_string = "Mi String"
my_other_string = 'Mi otro string'

# longitud de un string
print("**************** Longitud de un string ***************")
print('len(my_string): ', len(my_string))
print('len(my_other_string): ', len(my_other_string))

# concatenar string
print("**************** Concatenar string ***************")
print(my_string, "***", my_other_string)

# string con caracteres especiales
print("**************** Escape strings ***************")
my_new_line_string = "String con \nsalto de linea(\\n)"
my_new_tab_string = "String con \ttabulacion(\\t)"
my_scape_string = "\"hola\""
print(my_new_line_string)
print(my_new_tab_string)
print(my_scape_string)

# cadena multilinea
print("**************** String Mutilinea ***************")
my_string_multiline = """Soy un
string con
multiples lineas
de texto"""
print(my_string_multiline)

# Formateo de strings
print("**************** Formateo de strings ***************")
name = "Gabriel"
surname = "Cervantes"
age = 32
pi = 3.141952
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # %s para strings, %d numeros enteros, %f floats
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # interpolacion
print(f"Número pi: {pi:.2f}")

# Desempaquetado de caracteres
print("**************** Desempaquetando caracteres ***************")
language = 'python'
a, b, c, d, e, f = language
print(a, b)

# Dividir string
print("**************** Dividir String ***************")
language_slice = language[1:3]
print('python dividido [1:3]: ', language_slice)
print(language[1:]) # desde el indice indicado hasta el final
print(language[-2]) # desde la ultima
print(language[0:6:2])

# Invertir
print("**************** Invertir string ***************")
reversed_language = language[::-1]
print(f'python invertido: {reversed_language}')

# funciones del sistema
print("**************** Funciones del sistema ***************")
language = 'Python is too good'
print(f"'{language}'.title(): {language.title()}")
print(f"'{language}'.capitalize(): {language.capitalize()}")
print(f"'{language}'.upper(): {language.upper()}")
print(f"'{language}'.lower(): {language.lower()}")
print(f"'{language}'.count('t'): {language.count('t')}")
print(f"'{language}'.isnumeric(): {language.isnumeric()}")
print(f"'1'.isnumeric(): {'1'.isnumeric()}")
print(f"'{language}'.lower().isupper(): {language.lower().isupper()}")
print(f"'{language}'.startswith('Py'): {language.startswith('Py')}")
print(f"'{language}'.strip('od'): {language.strip('od')}")
print(f"'{language}'.replace('Python','Js'): {language.replace('Python','Js')}") # 'thirt{language}