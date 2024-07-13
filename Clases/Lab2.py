dic = {"nombre":"Pikachu", "edad": 23 }
productos = ["arroz", "matequilla","carne"]
listaDic = [
	dic,
	{"nombre": "Meetwo", "edad": 2000}
]
dicInventario = {
	"TiendaHeredia": ["computadoras", "mouse", "teclado"],
	"TiendaAlajuela": productos
}
dicInventario["TiendaCartago"] = ["Galletas", "Postres"]
listaDic.append({"nombre": "Charmander", "edad": 5})

print(listaDic)

def  sumar(num1, num2):
	return num1 + num2

def resta(num1, num2):
	try:
		numero1 = int(num1)
		numero2 = int(num2)
		return numero1 - numero2 # Otra forma de hacer int(num1) - int(num2)
	except ValueError:
		return

while True:
	try:
		print("1. Ingresar")
		print("2. Eliminar")
		print("3. Sumar")
		print("4. Resta")
		print("5. Salir")

		opcion = int(input("Ingrese una opcion >"))
		
		if opcion == 1:
			print("opcion 1")
		elif opcion == 2:
			print("opcion 2")
		elif opcion == 3:
			while True:
				try:
					numero1 = int(input("Ingrese el primer numero a sumar >"))
					numero2 = int(input("Ingrese el segundo numero a sumar >"))
					print(sumar(numero1, numero2))
					break
				except ValueError:
					print("Ingrese valores validos para suma")
		elif opcion == 4:
			numero1 = input("Ingrese el primer numero a restar > ")
			numero2 = input("Ingrese el segundo numero a restar > ")
			resultado = resta(numero1, numero2)
			if resultado == None:
				print("Algo salio mal, vuelva a intentarlo.")
			else:
				print(f"El valor de la resta es {resultado}")
		elif opcion == 5:
			break
		else:	
			print("opcion otra")
	except ValueError:
		print("Ingrese una opcion valida")

numero = 0
try:
	numero = int(input("Ingrese numero > "))
	file = open("archivito.txt")
except FileNotFoundError:
	open("archivito.txt", "w")
except ValueError:
	numero = -1
	print(f"Ingrese un valor correcto {numero}")

cliente = [
	{"nombre":"Carlos Perez",
  	"edad":20,"provincia":"Alajuela"},
	{"nombre":"Carlos Alpizar",
     "edad":21,"provincia":"Puntarenas"},
    {"nombre": "Roberto Alpizar",
     "edad": 23, "provincia": "San Jose"}
]

for c in cliente:
    print(f"Nombre: {c["nombre"]} Edad: {c["edad"]} Provincia: {c["provincia"]} \n")
    
try:
	buscarEdad = int(input("Que persona cumple con esta edad > "))
	loEncontre = False

	for c in cliente:
		if buscarEdad == c["edad"]:
			print(f"Nombre: {c["nombre"]}")
			loEncontre = True
		# else:
		#     print(f"Esta persona no cumple: {c["nombre"]}")

	if(not loEncontre):
		print(f"Nadie cumple con la edad {buscarEdad}")
except ValueError:
	print("La edad es invalida. intentelo de nuevo")