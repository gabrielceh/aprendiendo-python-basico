# LISTS

# Definir listas
print("***************** Definir listas ******************")
my_list = list()
my_other_list = []

print(my_list) # []
print(len(my_list)) # 0

my_list = ["🍕", "🍔", "🌭", "🍪", "🌮", "🍫", "🌮"]
print(my_list)
print(len(my_list))

my_other_list = [32, 1.72, "Gabriel", "Cervantes"]
print(my_other_list)

print(type(my_list))
print(type(my_other_list))


# Accediendo a los elementos de las listas
print("***************** Accediendo a elementos ******************")
print(f'Primer elemento de {my_list}: {my_list[0]}')
print(f'Segundo elemento de {my_list}: {my_list[1]}')
print(f'Último elemento de {my_list}: {my_list[-1]}')
print(f'Penúltimo elemento de {my_list}: {my_list[-2]}')
print(my_list.count("🌮"))


# Desempaquetando listas
print("***************** Desempaquetando listas ******************")
age, height, name, surname = my_other_list
print(name)

# Concatenar listas
print("***************** Concatenar listas ******************")
lista_concatenada = my_list + my_other_list
print(lista_concatenada)

# Insertar, eliminar, actualizar elementos
print("***************** Insertar, eliminar, actualizar elementos listas ******************")
print(my_list)
my_list.append('🥞')
print(f"Agregando 🥞: {my_list}")

my_list.insert(0, '🍝')
print(f'Insertando 🍝 al inicio: {my_list}')

my_list[0] = "🥐"
print(f"Actalizando el elemento 0: {my_list}")

my_list.remove('🍪')
print(f"Removiendo 🍪: {my_list}")

my_list.pop()
print(f"Eliminando el ultimo elemento: {my_list}")

my_list.pop(2)
print(f"Eliminando el tercer elemento:  {my_list}")

del my_list[3]
print(f"Eliminando el cuarto elemento: {my_list}")

del my_list
# print(my_list) NameError: name 'my_list' is not defined




# Operaciones con listas
print("***************** Operaciones con listas ******************")

my_list = ["🍕", "🍔", "🌭", "🍪", "🌮", "🍫", "🌮"]
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)
num_list = [45,12,67,20,31]
num_list.sort()
print(num_list)


# Sublistas
print("***************** Sublistas con listas ******************")
print(f"Lista original: {my_new_list}")
print(f"Sublista: {my_new_list[1:3]}")










