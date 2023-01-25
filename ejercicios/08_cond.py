"""
1. Write a code which gives grade to students according to theirs scores:
	80-100, A
	70-79, B
	60-69, C
	50-59, D
	0-49, F

"""
print(("*" * 10), "Ejercicio 1" ,("*" * 10))

score = 49

if score >= 80 and score <= 100:
	print("A")

elif score >= 70 and score <= 79:
	print("B")

elif score >= 60 and score <= 69:
	print("C")

elif score >= 50 and score <= 59:
	print("D")

else:
	print("F")



"""
2. Check if the season is Autumn, Winter, Spring or Summer. 
	If the user input is: September, October or November, the season is Autumn. 
	December, January or February, the season is Winter. 
	March, April or May, the season is Spring 
	June, July or August, the season is Summer
"""

print(("*" * 10), "Ejercicio 2" ,("*" * 10))
month = "JULY"
# month = input("Enter a month: ")

month = month.lower()

if month == 'september' or month == 'october' or month == 'november':
	print("Autum")

elif month == 'december' or month == 'january' or month == 'february':
	print("Winter")

elif month == 'march' or month == 'april' or month == 'may':
	print("Spring")

elif month == 'june' or month == 'july' or month == 'august': 
	print("Summer")

else:
	print(f"'{month}' is not valid")




"""
3. The following list contains some fruits:
	fruits = ['banana', 'orange', 'mango', 'lemon']
	If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
	If the fruit exists print('That fruit already exist in the list')

"""
print(("*" * 10), "Ejercicio 3" ,("*" * 10))

fruits = ['banana', 'orange', 'mango', 'lemon']

# my_fruit = input('Enter a fruit: ')
my_fruit = "apple"

my_fruit = my_fruit.lower()

if not my_fruit in fruits:
	fruits.append(my_fruit)
	print(f"My fruits: {fruits}")

else:
	print('That fruit already exist in the list')




"""
4. Here we have a person dictionary. Feel free to modify it!

    person={
		'first_name': 'Asabeneh',
		'last_name': 'Yetayeh',
		'age': 250,
		'country': 'Finland',
		'is_marred': True,
		'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
		'address': {
			'street': 'Space street',
			'zipcode': '02210'
		}
    }
	* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
	* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
	* If a person skills has only JavaScript and React, print('He is a front end developer'), 
		if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
		if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
		else print('unknown title') - for more accurate results more conditions can be nested!
	* If the person is married and if he lives in Finland, print the information in the following format:
		Asabeneh Yetayeh lives in Finland. He is married.
"""
print(("*" * 10), "Ejercicio 4" ,("*" * 10))


person={
	'first_name': 'Asabeneh',
	'last_name': 'Yetayeh',
	'age': 250,
	'country': 'Finland',
	'is_marred': True,
	'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
	'address': {
		'street': 'Space street',
		'zipcode': '02210'
	}
}

if "skills" in person:
	index = (len(person['skills']) - 1) // 2
	middle_skill = person['skills'][2]
	print(f"middle skill: {middle_skill}")

	if "Python" in person['skills']:
		print("Python is a skill")
	else :
		print("Python is not a skill")

	if len(person['skills']) == 2  and ('JavaScript' and 'React' in person['skills']):
		print('He is a front end developer')
	
	elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
		print('He is a fullstack developer')
	
	elif 'JavaScript' and 'React' and 'MongoDB' in person['skills']:
		print('He is a fullstack developer')
	else:
		 print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
	print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")





