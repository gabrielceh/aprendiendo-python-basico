"""
1. Using the len() built-in function, find the length of your first name
2. Compare the length of your first name and your last name
3. Declare 5 as num_one and 4 as num_two
      i. Add num_one and num_two and assign the value to a variable total
      ii. Subtract num_two from num_one and assign the value to a variable diff
      iii. Multiply num_two and num_one and assign the value to a variable product
      iv. Divide num_one by num_two and assign the value to a variable division
      v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
      vi. Calculate num_one to the power of num_two and assign the value to a variable exp
      vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
4. The radius of a circle is 30 meters.
      i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
      ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
      iii. Take radius as user input and calculate the area.
5. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
"""

# ############ EJERCICIO 1 #################
print(("*" * 10),"Ejercicio 1", ("*" * 10))

print(len('Gabriel'))

# ############ EJERCICIO 2 #################
print(("*" * 10),"Ejercicio 2", ("*" * 10))

print(f"first name: Gabriel: {len('Gabriel')} characters")
print(f"last name name: Cervantes: {len('Cervantes')} characters")

# ############ EJERCICIO 3 #################
print(("*" * 10),"Ejercicio 3", ("*" * 10))

num_one, num_two = 5 , 4

total : int = num_one + num_two
diff: int = num_two - num_two
product: int = num_one * num_two
division : float = num_one / num_two
remainder : int = num_two % num_one
exp : int = num_one ** num_two
floor_division : int = num_one // num_two

print(f"{num_one} + {num_two} = {total}")
print(f"{num_one} - {num_two} = {diff}")
print(f"{num_one} * {num_two} = {product}")
print(f"{num_one} / {num_two} = {division}")
print(f"{num_two} % {num_one} = {remainder}")
print(f"{num_one} ** {num_two} = {exp}")
print(f"{num_one} // {num_two} = {floor_division}")



# ############ EJERCICIO 4 #################
print(("*" * 10),"Ejercicio 4", ("*" * 10))

circle_radius = 30
PI = 3.141592

area_of_circle = PI * (circle_radius ** 2)
circum_of_circle = (2 * PI) * circle_radius

print(f"area del circulo: {area_of_circle:.2f}")
print(f"circunferencia: {circum_of_circle:.2f}")

circle_radius = input("Ingrese el area del circulo: ")
area_of_circle = PI * (int(circle_radius) ** 2)
print(f"area del circulo del usuari: {area_of_circle:.2f}")


# ############ EJERCICIO 5 #################
print(("*" * 10),"Ejercicio 5", ("*" * 10))

name = input("ingrese su nombre: ")
lastname = input("ingrese su apellido: ")
age = input("ingrese su edad: ")
country = input("ingrese su pais: ")

print(f"Name: {name}")
print(f"Last name: {lastname}")
print(f"Age: {age}")
print(f"Country: {country}")
