'''
dict.-
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las
listas indices numericos tienen alfanumericos.Es decir algo parecido como los objetos

Tambien se conoce como un arreglo asosiativo u Objeto JSON

El diccionario es una coleccion ordenada** y modificable.
No hay miembros duplicados.
'''
import os
os.system("cls")

#Lista de paises
paises=["Mexico","Brasil","Brasil","Canada","España"]

#dict u objeto
pais_mexico={
        "Nombre":"Mexico",
        "capital":"CDMEX",
        "poblacion":12000000,
        "idioma":"español",
        "status":True
        }

pais_brasil={
        "Nombre":"Brasil",
        "capital":"Brasilia",
        "poblacion":10000000,
        "idioma":"portugues",
        "status":True
        }

pais_canada={
        "Nombre":"Canada",
        "capital":"Ottawa",
        "poblacion":9000000,
        "idioma":["ingles","frances"],
        "status":False
        }

alumno1={
    "nombre":"Daniel",
    "apellido_paterno":"Hernandez",
    "apellido_materno":"Gomez",
    "carrera":"TI",
    "matricula":"123456",
    "area":"Softwware Multiplataforma",
    "modalidad":"Bilingue",
    "cuatrimestre":"2"

}

#Mostrar el contenido del dict
print(alumno1)

for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar un campo o atributo
alumno1["telefono"]="6181234567"
for i in alumno1:
    print(f"{i}={alumno1[i]}")
