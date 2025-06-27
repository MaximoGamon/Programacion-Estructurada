#Lista=[
#["Ruben,10,10,10"]  fila
#]


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n \U0001F552 \t ...Oprima cualquier tecla para continuar \U0001F552...")  

def menu_principal():
  print("\t\t ..::: Sistema de Gestión de Calificaciones :::...\n\t\t 1️⃣  Agregar  \n\t\t 2️⃣  Mostrar \n\t\t 3️⃣  Calcular Promedios  \n\t\t 4️⃣ SALIR ")
  opcion=input("\t 👉 Elige una opción (1-4): ").upper()
  return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
  print("\t\t\t .:: \U0001F4DD Agregar Calificaciones \U0001F4DD::.")
  nombre = input(" \t\t \U0001F464  Nombre del alumno: ").upper().strip()
  calificaciones = []
  for i in range(1,4):
    continua=True
    while continua:
      try:
        cal=float(input(f"Calificacion {i}: "))
        if cal >= 0 and cal< 11:
            calificaciones.append(cal)
            continua=False
        else:
            print("\u26A0 Ingresa un numero valido \u26A0")
      except ValueError:
        print("\u26A0 Ingresa un valor numerico \u26A0")
  lista.append([nombre]+calificaciones)
  print(" \u2705 Accion realizada con exito \u2705 ")

def mostrar_calificaciones(lista):
    #for i in range (len(lista)):
      #print(f"{i} {lista[i]}")
  borrarPantalla()
  print( " \t\t\t \U0001F50D  Mostrar Calificaciones \U0001F50D")
  if len(lista)>0:
      print(f"{'Nombre':<15} {'Calf. 1':<10} {'Calf. 2':<10} {'Calf. 3':<10} ")
      print(f"{'-'*40}")
      for fila in lista:
        print(f"{fila[0]:<15}    {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
      print(f"{'-'*40}")
      cuantos=len(lista)
      print(f"son {cuantos} alumnos")
  else:
    print(" \u26A0 No hay calificaciones registradas en el sistema \u26A0 ")


def calcular_promedio2(lista):
  borrarPantalla()
  if len(lista)>0:
    print(f"{'Alumno':<15} {'promedio':<10}")
    print(f"{'-'*30}")
    promedio_grupal=0
    for fila in lista:
      nombre=fila[0]
      i=1
      suma=0
      promedio=0
      while i <=3:
        suma += fila[i]
        i+=1
      promedio=suma/3
      print(f"{nombre:<15} {promedio:.2f}")
      promedio_grupal+=promedio
    print(f"{'-'*30}")
    promedio_grupal=promedio_grupal/len(lista)
    print(f"El promedio grupal es: {promedio_grupal}")
  
  else:
    print("\u26A0 No hay calificaciones registradas en el sistema \u26A0")
    
def calcular_promedio(lista):
  borrarPantalla()
  print("\t\t\t .:: 📊 Calcular promedio 📊 ::.")
  if len(lista)>0:
    print(f"{'Alumno':<15} {'promedio':<10}")
    print(f"{'-'*30}")
    promedio_grupal=0
    for fila in lista:
      nombre=fila[0]
      promedio=sum(fila[1:])/3
      print(f"{nombre:<15} {promedio:.2f}")
      promedio_grupal+=promedio
    print(f"{'-'*30}")
    promedio_grupal=promedio_grupal/len(lista)
    print(f"{'-'*30}")
    print(f"El promedio grupal es: {promedio_grupal}")
  
  else:
    print("\u26A0 No hay calificaciones registradas en el sistema \u26A0")


