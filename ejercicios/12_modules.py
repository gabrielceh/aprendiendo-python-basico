from generates_id import random_user_id, user_id_gen_by_user
from generates_colors import rgb_color_gen, list_of_hexa_colors, list_of_rgb_colors, generate_colors
"""
1. Writ a function which generates a six digit/character random_user_id.
  	print(random_user_id()) #'1ee33d'
"""
print("\n" + ("*~" * 10), "Ejercicio 1" ,("*~" * 10))

print(random_user_id())

"""
2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print(user_id_gen_by_user()) # user input: 5 2
#kcsy2
#SMFYb

print(user_id_gen_by_user()) # 16 1
#1GCSgPLMaBAVQZ26
"""
print("\n" + ("*~" * 10), "Ejercicio 2" ,("*~" * 10))
# print(user_id_gen_by_user())



"""
3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
"""
print("\n" + ("*~" * 10), "Ejercicio 3" ,("*~" * 10))
print(rgb_color_gen())


"""
4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f
"""
print("\n" + ("*~" * 10), "Ejercicio 4" ,("*~" * 10))
print(list_of_hexa_colors(5))
print(list_of_hexa_colors(3))


"""
5. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
"""
print("\n" + ("*~" * 10), "Ejercicio 5" ,("*~" * 10))
print(list_of_rgb_colors(5))
print(list_of_rgb_colors(2))
print(list_of_rgb_colors(10))


"""
6. Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""
print("\n" + ("*~" * 10), "Ejercicio 6" ,("*~" * 10))

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 1))
print(generate_colors('rgb', 5))
print(generate_colors('hexa', 2))
