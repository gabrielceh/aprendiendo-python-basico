# TUPLES

# Definir una tupla
print("***************** Definir tupas ******************")

my_tuple = tuple()
my_other_tuple = ("🥞", "🍪", "🌮", "🌭", "🍫", "🥐")

my_tuple = (32, 1.72, "Gabriel", "Cervantes")
print(f"my_tuple: {my_tuple}")
print(my_tuple[0])
print(my_tuple[-1])

# my_other_tuple[1] = 1.80  # TypeError: 'tuple' object does not support item assignment

# Metodos
print("***************** Metodos de tuplas ******************")
print(f"my_tuple: {my_tuple}")
print(f"count('Gabriel'): {my_tuple.count('Gabriel')}")
print(f"count('🥐'): {my_tuple.count('🥐')}")
print(f"index(32): {my_tuple.index(32)}")
print(f"index('Gabriel'): {my_tuple.index('Gabriel')}")
# print(f"index('Gabo'): {my_tuple.index('Gabo')}") ValueError: tuple.index(x): x not in tuple


# Uniendo tupas
print("***************** Uniendo tupas ******************")
my_third_tuple = my_tuple + my_other_tuple
print(f"My_third_tuple: {my_third_tuple}")

# Subtuples
print("***************** Subtuplas ******************")
print(f"subtupla: {my_third_tuple[3:7]}")

# Convirtiendo a lista
print("***************** Convirtiendo una tupla a lista ******************")
print(f"my_tuple: {my_tuple}")
my_tuple_to_list = list(my_tuple)
print(f"my_tuple_to_list: {my_tuple_to_list}")
my_tuple_to_list.append('Azul')
print(my_tuple_to_list)
my_tuple_to_list[4] = 'Rojo'
print(my_tuple_to_list)