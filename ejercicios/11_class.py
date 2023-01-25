"""
Plantear una clase que administre un listado de diccionarios con nombres de estudiantes y notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.
"""

class Colegio:
	def __init__(self):
		self.__alumnos = []

	def menu(self):
		opt = ''

		while opt != "4":
			print("""
				*** Bienvenido ***
				Seleeccione una opción:
				1. Cargar alumnos
				2. Listar alumnos
				3 Mostrar alumnos con notas mayores a 7
				4. Salir
			""")
			opt = input('Ingrese su opcion: ')
			match opt:
				case "1":
					self.cargar_alumnos()
				case "2":
					self.listar_alumnos()
				case "3":
					self.notas_mayores_7()
				case "4":
					self.salir()
				case _:
					print("No es una opción valida")

	def cargar_alumnos(self):
		if len(self.__alumnos) < 5:
			for num in range(5):
				nombre = input(f"Ingresa el nombre del alumno {num + 1}: ")
				nota = float(input(f"Ingresa la nota del alumno {num + 1}: "))
				alumno = {
					"nombre":nombre,
					"nota": nota	
				}
				self.__alumnos.append(alumno)
			print("Registro completo!!!\n")
		else:
			print('Ya no puede cargar mas alumnos')


	def listar_alumnos(self):
		print(("*~" * 5) + "Listado de alumnos" + ("*~" * 5))
		if len(self.__alumnos) > 0:
			for alumno in self.__alumnos:
				print(f"Nombre: {alumno['nombre']} - Nota: {alumno['nota']}")
		else:
			print('No hay alumnos en el sistema')
		print('')


	def notas_mayores_7(self):
		print(("*~" * 5) + "Listado de alumnos con notas mayores a 7" + ("*~" * 5))
		if len(self.__alumnos) > 0:
			for alumno in self.__alumnos:
				if(alumno["nota"] > 7.0):
					print(f"Nombre: {alumno['nombre']} - Nota: {alumno['nota']}")
		else:
			print("No hay alumnos en el sistema")
		print('')

	
	def salir(self):
		print("Gracias por usar nuestro sistema")
		

colegio = Colegio()
colegio.menu()

