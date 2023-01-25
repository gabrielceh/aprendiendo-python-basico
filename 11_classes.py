# Classes

# creando una clase
print("\n" + ("*~" * 10), "Creando una clase" ,("*~" * 10))

class MyEmptyClass:
	pass

print(MyEmptyClass) # <class '__main__.MyEmptyClass'>
print(MyEmptyClass()) #< __main__.MyEmptyClass object at 0x00000202CF6EF450>


# Constructor y metodos
print("\n" + ("*~" * 10), "Constructor y métodos de una clase" ,("*~" * 10))

class Person:
	def __init__(self, name:str, last_name:str, age:int, alias = ""):
		self.name = name # propiedad publica
		self.last_name = last_name
		self.age = age
		self.alias = alias  
		self.__hi = "Hola"  # propiedad privada

	def info(self):
		return f"{self.name} {self.last_name}. He is {self.age} years old."

	# get
	def get_hi(self):
		return self.__hi

	def set_hi(self, hi:str):
		self.__hi = hi

	def walk(self, place = "parque"):
		return f"{self.name} camina por {place}"



persona_1 = Person("Gabriel","Cervantes",32,"Gabo")
print(persona_1)
print(persona_1.name)
print(persona_1.last_name)
print(persona_1.age)
print(persona_1.alias)
# print(persona_1.__hi) # 'Person' object has no attribute '__hi'
print(persona_1.info())
print(persona_1.walk("el supermercado"))
print(persona_1.get_hi())
persona_1.set_hi('Hello world')
print(persona_1.get_hi())


# Herencia
print("\n" + ("*~" * 10), "Herencia de una clase" ,("*~" * 10))

class Student(Person):
	pass

student_1 = Student("Angie","Cervantes", 20)
print(student_1.name)
print(student_1.info())


class Worker(Person):
	# añadimos la propiedad salary, pero llamamos al super y le pasamos las propiedades que el padre necesita 
	def __init__ (self, name:str, last_name:str, age:int, salary:float):
		super().__init__(name, last_name, age)
		self.salary = salary

	# reescribimos el metodo info
	def info(self):
		return {"name":self.name, "last_name": self.last_name, "age":self.age, "salary":self.salary}


worker_1 = Worker("Gabriel", "Cervantes", 32, 1500.00)
print(worker_1.alias)
print(worker_1.info())
print(worker_1.walk('la oficina'))
