from random import randint

def rgb_color_gen():
	try:
		index_color = []
		for i in range(3):
			ind = randint(0,255)
			index_color.append(ind)
		
		return f"rgb({index_color[0]}, {index_color[1]}, {index_color[2]})"

	
	except Exception as ex:
		return f"Error: {ex}"


def hexa_color_gen():
	try:
		list_of_characters = ["a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9"]
		hexa = "#"

		for j in range(0, 6):
			indx = randint(0, (len(list_of_characters) - 1))
			hexa += list_of_characters[indx]
	
		return hexa

	except Exception as ex:
		return f"Error: {ex}"



def list_of_hexa_colors(number_of_elemtes):
	try:
		list_of_hexa = []
		for i in range(0, number_of_elemtes):
			hexa = hexa_color_gen()
			list_of_hexa.append(hexa)
		
		return list_of_hexa

	except Exception as ex:
		return f"Error: {ex}"



def list_of_rgb_colors(number_of_elements):
	try:
		list_rgb = []
		for i in range(number_of_elements):
			color = rgb_color_gen()
			list_rgb.append(color)

		return list_rgb

	except Exception as ex:
		return f"Error: {ex}"



def generate_colors(type_color, number_of_colors):
	try:
		match type_color:
			case "hexa":
				return list_of_hexa_colors(number_of_colors)
			
			case "rgb":
				return list_of_rgb_colors(number_of_colors)

			case _:
				return f"Error: only rgb or hexa"

	except Exception as ex:
		return f"Error: {ex}"