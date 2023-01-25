# Operadores

#Operadores aritmeticos
print("*********Operadores Aritmeticos************")
print("suma  3 + 4: ", 3 + 4)
print("resta 3 - 4: ", 3 - 4)
print("mult. 3 * 4: ", 3 * 4)
print("div.  3 / 4: ", 3 / 4)
print("div.  10 / 2: ", 10 / 2) # La division de dos enteros siempre dará un float como resultado
print("mod.  10 % 3: ", 10 % 3)
print("floor.  10 // 3: ", 10 // 3) # Floor division. Aproximará el resultado a un entero
print("expo.  10 ** 3: ", 10 ** 3) # Exponente
print(3 ^ 3)

# Concatenar
print("Hola" + "Python")
print("Hola" + str(5)) # Cancatenar cadenas mas numeros

# Repetir
print("Hola " *  3)
print("Hola " *  (2 ** 3))
print("Hola " * int(5.0))


# Operadores de comparacion
print("*********Operadores de comparacion************")

print("3 >  4:", 3 > 4)
print("3 <  4:", 3 < 4)
print("3 >= 4:", 3 >= 4)
print("3 <= 4:", 4 <= 4)
print("3 == 4:", 3 == 4)
print("3 != 4:", 3 != 4)

# Cuando comparamos string, se compara por el orden alfabetico en ASCII
print("Hola >  Bye:", "Hola" > "Bye") 
print("Hola >  zye:", "Hola" > "zye") 
print("Hola <  Bye:", "Hola" < "Bye") 
print("Hola <  zye:", "Hola" < "zye") 
print("Hola >=  Bye:", "Hola" >= "Bye") 
print("Hola <=  Bye:", "Hola" <= "Bye") 
print("Hola ==  Bye:", "Hola" == "Bye") 
print("Hola !=  Bye:", "Hola" != "Bye") 
print("aaa > aba:", "aaa" > "aba")

print('1 is 1:', 1 is 1)    # True               
print('1 is not 2:', 1 is not 2)    # True       
print('G in Gabriel:', 'G' in 'Gabriel')  # True
print('B in Gabriel:', 'B' in 'Gabriel')  # False
print("coding in coding for all:", 'coding' in 'coding for all')  # True
print('a in an:', 'a' in 'an') # True
print('4 is 2 ** 2:', 4 is 2 ** 2)  # True 


### Operadores Lógicos ###
print("*********Operadores Lógicos************")
# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print("3 > 4 and  Hola >  Python: ", 3 > 4 and "Hola" > "Python")
print("3 > 4 or  Hola  > Python: ", 3 > 4 or "Hola" > "Python")
print("3 < 4 and  Hola <  Python: ", 3 < 4 and "Hola" < "Python")
print("3 < 4 or  Hola >  Python: ", 3 < 4 or "Hola" > "Python")
print("3 < 4 or  (Hola >  Python and 4 == 4): ", 3 < 4 or ("Hola" > "Python" and 4 == 4))
print("not(3 > 4): ", not(3 > 4))