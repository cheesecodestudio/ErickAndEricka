persona={
    "cedula":"202220222",
    "nombre":'alberto perez alvarez',
    "edad":19,
    "cursos":[1,3,4,5]
    }
print(persona["cursos"])
persona["cursos"].extend([7,90,9])
print(persona)

for k in persona:
  print(k, persona[k])

claves = persona.keys()
print(claves)
print(persona.values())

persona.get("cedula")