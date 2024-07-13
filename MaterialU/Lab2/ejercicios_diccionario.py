
lstPersona=[]
dicPersona={}

while True:
    cedula=input("Ingrese una cedula :")
    nombre=input("Ingrese un nombre :")
    edad=int(input("Ingrese una edad :"))

    dicPersona={
        "cedula":cedula,
        "nombre":nombre,
        "edad":edad}
    lstPersona.append(dicPersona)
    opcion=input("Desea agregar otra persona?")
    if opcion=="n":
        break
print(lstPersona)