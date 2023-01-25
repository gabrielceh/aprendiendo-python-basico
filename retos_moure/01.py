"""
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama(word_one:str, word_two:str):
	if not isinstance(word_one, str) and not isinstance(word_two, str):
		print("Deben ser strings")
		return False
	elif len(word_one) != len(word_two):
		return False
	elif word_one.lower() == word_two.lower():
		return False
	else:
		list_word_one = list(word_one.lower())
		list_word_two = list(word_two.lower())
		list_word_one.sort()
		list_word_two.sort()
		count = 0

		for ind in range(len(list_word_one)):
			if list_word_one[ind] == list_word_two[ind]:
				count += 1
		
		return len(word_one) == count


print(is_anagrama("Gabriel", "agbriel"))

