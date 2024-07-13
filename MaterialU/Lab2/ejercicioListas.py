
numeros=[]
while True:
    elemento=int(input("Ingrese elementos a la lista: "))
    # .append agrega un elemento al final de la lista
    numeros.append(elemento)
    opcion=input("Desea agregar otro elemento: ")
    if opcion.lower()=="n":
        break


for i in (numeros):
    print(i,end="-")
'''
print("El tamaño de la lista es de :",len(numeros))
numeros.insert(2,"Hola")
print(numeros)
numeros.append(45)
print("El tamaño de la lista es de :",len(numeros))
'''