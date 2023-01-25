# Loops

# while
print("\n" + ("*~" * 10), "while" ,("*~" * 10))

my_condition = 0

while my_condition < 10:
	print(f"my_condition en el bucle: {my_condition}")
	my_condition += 2
else: # OPCIONAL: podemos agregarle un else para que se ejecute si la condicion no se cumple
	print(f"my_condition en el else: {my_condition}")

print("**La ejecución continúa**")


print("\n" + ("*~" * 10), "break & continue" ,("*~" * 10))

while my_condition < 20:
	my_condition += 1
	if(my_condition == 15):
		print('BREAK')
		break # se saldrá del bucle, no ejecutará el else
	print(my_condition)
else:
	print('else y break')

print("**La ejecución continúa**")

my_condition = 10

while my_condition < 20:
	my_condition += 1
	if(my_condition == 15):
		print('CONTINUE')
		continue ## no seguira ejecutando en esta iteracion
	print(my_condition)

print("**La ejecución continúa**")


print("\n" + ("*~" * 10), "for" ,("*~" * 10))

# for and strings
print("*** for con strings ***")
name = "gabriel"

for letter in name:
	print(f"letter '{letter}' in {name}")


# for and list
print("*** for con listas ***")
fruits = ["🍉","🍇","🍊","🍍","🍎","🍐","🍑","🍓"]
for fruit in fruits:
	print(f"fruit: {fruit} en el listado de frutas")

#for and tuples
print("*** for con tuplas ***")
my_tuple = ("Gabriel", "Cervantes", 32, 1.72, "Barranquilla")

for data in my_tuple:
	print(f"Elemento de la tupla: {data}")

#for and sets
print("*** for con sets ***")
my_set = {"Gabriel", "Cervantes", 32, 1.72, "Barranquilla"}

for data in my_set:
	print(f"Elemento del set: {data}")

#for and dict
print("*** for con dict ***")
persona = {
  "name": "Gabriel",
  "surname": "Cervantes",
  "age": 32,
  "is_marred" : False,
  "skills" : ["Js","Css","Html"],
  "social":{
    "twitter": "@gabrielcehu",
    "instagram" : "gabo_cervantes"
  }
}

for data in persona:
	if data == 'is_marred':
		print(f"Elemento: {data} - Value: Si") if persona[data] else print(f"Elemento: {data} - Value: No")
		continue
	print(f"Elemento: {data} - Value: {persona[data]}")

for value in persona.values():
	print(f"Value: {value}")
else:
	print('else fuera del for')



print("\n" + ("*~" * 10), "range" ,("*~" * 10))

my_numbers = list(range(11))
print(f"range(11): {my_numbers}")

pair_numbers = list(range(0,11,2))
print(f"range(0,11,2): {pair_numbers}")

for number in range(11): # excluye al 11
	print(f"for in range(11): {number}")



fruits = ["🍉","🍇","🍊","🍍","🍎","🍐","🍑","🍓"]
for index in range((len(fruits))):  # le resta -1
	print(f"fruit: {fruits[index]} en el index {index}")


print("\n" + ("*~" * 10), "enumerate" ,("*~" * 10))
# enumerate recibe un iterable(list, dict, etc) y devuelve una tupla con la posicion y el elemento

fruits = ["🍉","🍇","🍊","🍍","🍎","🍐","🍑","🍓"]
print(list(enumerate(fruits)))

for ind, fruit in enumerate(fruits):
	print(f"fruta: {fruit} - index: {ind}")




