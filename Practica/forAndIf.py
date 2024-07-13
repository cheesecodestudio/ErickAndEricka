'''
### Descripción:

Escribe un programa en Python que reciba una lista de números del usuario y 
determine cuáles de esos números son pares y cuáles son impares. 
El programa debe imprimir los números pares e impares por separado.

### Instrucciones:

1. Solicita al usuario que ingrese una lista de números separados por comas.
2. Usa un ciclo `for` para iterar sobre los números de la lista.
3. Usa una estructura condicional `if` para determinar si cada número es par o impar.
4. Guarda los números pares en una lista y los números impares en otra lista.
5. Imprime las dos listas resultantes.
'''
numeros = input("Deme una lista de numeros separada por commas(,) >") # 1,20,85,53,22,10
pares = []
impares = []

for numero in numeros.split(','):
	if int(numero) % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)


print("Numeros pares: ", pares)
print("Numeros impares: ", impares)

'''
### Descripción:

Escribe un programa en Python que reciba un número entero positivo del usuario y 
determine si es un número primo. 
Un número primo es aquel que solo es divisible por 1 y por sí mismo.

### Instrucciones:

1. Solicita al usuario que ingrese un número entero positivo.
2. Usa un ciclo `for` para verificar si el número es divisible por algún número entre 2 y 
   la raíz cuadrada del número ingresado.
3. Usa una estructura condicional `if` para determinar si el número es primo.
4. Imprime un mensaje indicando si el número es primo o no.
'''
import math

numero = int(input("Ingrese un numero entero positivo >"))

esPrimo = True

if(numero < 2):
	esPrimo = False
else:
	for num in range(2, int(math.sqrt(numero)) + 1):
		if(numero%num == 0):
			esPrimo = False
			break
		
if(esPrimo):
	print("El numero " + str(numero) + " es primo")
	print(f"El numero {numero} es primo")
else:
	print("El numero " + str(numero)+ " no es primo")

'''
### Descripción:

Escribe un programa en Python que reciba una cadena de texto del usuario y 
cuente el número de vocales y consonantes en la cadena. 
El programa debe imprimir el número de vocales y consonantes por separado.

### Instrucciones:

1. Solicita al usuario que ingrese una cadena de texto.
2. Usa un ciclo `for` para iterar sobre cada carácter en la cadena.
3. Usa una estructura condicional `if` para determinar si cada carácter es una vocal o 
   una consonante.
4. Ignora los caracteres que no sean letras (como espacios, números, y símbolos).
5. Imprime el número total de vocales y consonantes.
'''
# Pedirle al usuario informacion
texto = input("Escriba algo bonito >") # Hola precioso espero que estes bien fiuu fiuu.

# Aqui voy a guardar la cantidad de vocales y consontantes
vocales = 0 
consonates = 0 

for letra in texto:
	if letra.isalpha():
		if letra in "aeiouAEIOU":
			vocales += 1
		else:
			consonates += 1

print(f"Numero de vocales: {vocales}")
print(f"Numero de consonates: {consonates}")

'''
### Descripción:

Escribe un programa en Python que me diga cuantas personas son mayores a 18 años y cuantas
son menores de edad.

### Instrucciones:

1. Usa un ciclo `for` para iterar sobre una lista de diccionarios para verificar la edad.
2. Usa una estructura condicional `if` para determinar si esa edad es mayor o igual a 18.
3. Imprimir la cantidad de personas mayores de 18 años y la cantidad de menores de edad.
'''

personas = [
	"Ericka", "Josue", "Keslerth", "Raquel", "Kike", "Gabriel", "Hanna", "Jessica"
]

edades = [
	25,	14, 74, 18, 30, 12, 10, 22
]

personasDicc = [
	{"nombre": "Ericka", "edad": 25}
]

mayores = 0
nombresMayores = []
jovenes = 0
nombresJovenes = []
menores = 0
nombresMenores = []

indice = 0
for edad in edades:
	if edad >= 18:
		mayores += 1
		nombresMayores.append(personas[indice])
	elif edad >= 12 and edad < 18:
		jovenes += 1
		nombresJovenes.append(personas[indice])
	else:
		menores += 1
		nombresMenores.append(personas[indice])
	indice += 1


for persona in personasDicc:
	if persona["edad"] >= 18:
		mayores += 1
		nombresMayores.append(persona["nombre"])
	elif persona["edad"] >= 12 and persona["edad"] < 18:
		jovenes += 1
		nombresJovenes.append(persona["nombre"])
	else:
		menores += 1
		nombresMenores.append(persona["nombre"])



print(f"Mayores de edad son {mayores}")
print(f"Jovenes de edad son {jovenes}")
print(f"Menores de edad son {menores}")

# indicePersona = 0
# nombre = personas[indicePersona]
# edad = edades[indicePersona]

# print(f"Nombre: {nombre}, edad: {edad}")