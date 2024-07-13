lista=[]

lista=[12,34,5,67,"HOLA"]

print(lista[1])
# len es para ver cuantos elementos hay en la lista(diccionario/tupla/cadena...)
print(len(lista))


lista1=[1,2,3,4]
lista2=[5,6,7,1]
lista3=[lista1,lista2,8,9,10]
print(lista3[0])
print(lista3)
print(lista3[2:4])
# .extend es para agregar todos los elementos de una lista (lista2) a otra (lista1)
lista1.extend(lista2)
lista1.append(30)
print(lista1)

clientes=['maritn','lorena', 'manuel']
empleados=['albert','carlos', 'josefina']
doctores=['ruben','kimberly']

# .extend es para agregar todos los elementos de una lista (empleados/doctores) a otra (clientes)
clientes.extend(empleados)
print(clientes)
clientes.extend(doctores)
print(clientes)

# .append es para agregar un elemento "victor" al final de la lista clientes,
clientes.append("victor")
print(clientes)

# del es para borrar un elemento de la lista clientes pocision 0
del clientes[0]
clientes.remove('kimberly')
print(clientes)
