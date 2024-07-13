# Esto es un commentario

'''
Esto tambien es un comenntario, pero
usando varias lineas del archivo
'''

#Variables

texto = "Hola Isabel" #string
numero = 1 #int integer
existe = True #boolean 
lista = ["juan", "pepe", "carlos", "Jose"] #List
diccionario = { "clave": "valor", "nombre":"Keslerth"} #diccionario

lista[3]
nombre = diccionario["clave"]

# Condiciones

opcion = 1

if(opcion == 1):
	print("Esta opcion es ", opcion)
elif(opcion == 2):
	print("Texto de la opcion ", opcion)

if(existe):
	print("Esto es otra condicion")
else:
	print("El tamaño de la lista es ", len(lista))

# Ciclos
repetir = len(lista)
indice = 0
while (indice < repetir):
	print("ejecutar este codigo > ", lista[indice])
	indice += 1
	# indice = indice + 1


indice = len(lista) - 1
while (indice >= 0):
	print("ejecutar este codigo > ", lista[indice])
	indice -= 1

# lista = ["juan", "pepe", "carlos", "Jose"] #List
i = 0
for nombre in lista:
	print("En esta vuelta el valor es " + nombre +" posicion "+ str(i))
	i+= 1


for i in range(len(lista), 2):
	print("ejecutacion numero ", i)

listaProductos = []

for _ in range(5):
	producto = input("Escriba el producto > ")
	listaProductos.append(producto)


salir = True
while(True):
	print("1) Agregar")
	print("2) Modificar")
	print("3) Eliminar")
	print("4) Salir")
	otraOpcion = input("Elegir opcion> ")
	if(otraOpcion == "4"):
		break

# Funciones
listaPersonas = [
	{"nombre":"Juan", "edad":27, "estudia?":False},
	{"nombre":"Pancho", "edad":30, "estudia?":True},
	{"nombre":"Pablito", "edad":11, "estudia?":False}
]

def sumar(num1, num2):
	print(num1+num2)
	return "Ya lo sume"

# def sumar(num1, num2, num3):
# 	return num1+num2+num3

print("Suma",sumar(5, 7))

def Agregar(pNombre, pEdad, pEstudia):
	# persona = {"nombre":nombre, "edad":edad, "estudia?":estudia}
	persona = {}
	persona["nombre"] = pNombre
	persona["edad"] = pEdad
	persona["estudia?"] = pEstudia
	listaPersonas.append(persona)
	return pNombre

def Eliminar(nombre):
	for persona in listaPersonas:
		if(persona["nombre"] == nombre):
			listaPersonas.remove(persona)
			return True
	return False

# {"nombre":"Juan", "edad":27, "estudia?":False}
def VerPersonas():
	for persona in listaPersonas:
		estaEstudiando = "No"
		if(persona["estudia?"]):
			estaEstudiando = "Si"
		print("nombre> "+persona["nombre"]+ " edad> "+ str(persona["edad"])+ " estudia> "+ estaEstudiando)

def Menu():
	opcion = 0
	salir = True
	while(salir):
		print("1) Agregar")
		print("2) Eliminar")
		print("3) Ver Personas")
		print("4) Salir")
		opcion = int(input("Elegir opcion> "))
		if(opcion == 1):
			nombre = input("Introduce el nombre> ")
			edad = int(input("Introduce la edad> "))
			estudia = input("Estudia? Y/N >") == "Y"
			nombrePersonaAgregada = Agregar(nombre, edad, estudia)
			print("Agregado ", nombrePersonaAgregada)
		elif(opcion == 2):
			nombre = input("Nombre a Eliminar > ")
			seElimino = Eliminar(nombre)
			if(seElimino):
				print("Se elimino la persona", nombre)
			else:
				print("No se encontro a la persona")
		elif(opcion == 3):
			VerPersonas()
		if(opcion == 4):
			salir = False
Menu()