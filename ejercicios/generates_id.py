import string
from random import randint

letters = string.ascii_letters
digits = string.digits
letters_and_digits = list(letters + digits)

def random_user_id():
	new_id = ''
	try:	
		for num in range(0,6):
			indx = randint(0, (len(letters_and_digits) - 1))
			new_id += letters_and_digits[indx]
		
		return new_id

	except Exception as ex:
		return f"Error: {ex}"



def user_id_gen_by_user():
	new_id_list = []
	try:
		num_char = int(input("Number of characters: "))
		num_ids = int(input("Number of id's: "))

		for i in range(0, num_ids):
			id = ''
			for j in range(0, num_char):
				indx = randint(0, (len(letters_and_digits) - 1))
				id += letters_and_digits[indx]
			
			new_id_list.append(id)

		return new_id_list

	except Exception as ex:
		return f"Error: {ex}"
