# SETS

# Declarando sets
print("**************** Declarando sets **************")
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set)) # inicialmente es un dict
my_other_set = {"Gabriel","Cervantes", 32, 1.72}
print(my_other_set)
print(type(my_other_set))
print(len(my_other_set))


# Accediendo
print("**************** Accediendo sets **************")
# print(my_other_set[0]) TypeError: 'set' object is not subscriptable
print(f"'Gabriel' in my_other_set: {'Gabriel' in my_other_set}")
print(f"34 in my_other_set: {34 in my_other_set}")


# Metodos
print("**************** Metodos sets **************")
my_set = {"Landis","Anderson",20,1.72}
print(f"my_other_set original: {my_other_set}")
print(f"my_set: {my_set}")

my_other_set.add('Rojo')
print(f"add('Rojo'): {my_other_set}")

my_other_set.update(['Landis','Anderson'])
print(f"update([...]). {my_other_set}")

my_other_set.remove('Rojo')
print(f"remove('Rojo'): {my_other_set}")

print(f"intersection(): {my_other_set.intersection(my_set)}")
print(f"difference(): {my_other_set.difference(my_set)}")

my_third_set = my_other_set.union(my_set)
print(f"union(): {my_third_set}")

my_other_set.pop()
print(f"pop(): {my_other_set}")
my_other_set.pop()
print(f"pop(): {my_other_set}")

my_third_set.clear()
print(f"clear(): {my_third_set}")
print(f"clear(): {len(my_third_set)}")

del my_third_set
# print(my_third_set) not defined


# Transformacion *Peligroso porque los sets no tienen orden*
print("**************** Transformacion sets **************")
print(f"my_set original: {my_set}")
my_list = list(my_set)
print(f"set like list: {my_list}")
my_list[0] = 1.60
print(f"modificando el primer elemento: {my_list}")
