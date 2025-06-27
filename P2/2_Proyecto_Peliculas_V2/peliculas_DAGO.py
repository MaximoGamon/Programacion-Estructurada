

#Dict u objeto  para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma)

#peliculas={
 #  "nombre":"",
  # "categoria":"",
   #"clasificacion":"",
   #"genero":"",
   #"idioma":","
   #""
#}
pelicula={}
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t ...Oprima cualquier tecla para continuar ...")  

def crearPeliculas():
  borrarPantalla()
  print(".:: \U0001F4DD Alta de Peliculas \U0001F4DD ::. \n ")
  pelicula.update({"nombre":input("Ingrese  el nommbre: ").upper().strip()})
  pelicula.update({"categoria":input("Ingrese  la categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("Ingrese  la clasificación : ").upper().strip()})
  pelicula.update({"genero":input("Ingrese el genero: ").upper().strip()})
  pelicula.update({"idioma":input("Ingrese el idioma: ").upper().strip()})
  input("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705 :::")

def mostrarPeliculas():
  borrarPantalla()
  print("\n\t\t.:: \U0001F50D Consultar o Mostrar las Peliculas \U0001F50D ::.")
  if len(pelicula)>0:
    for i in pelicula:
       print(f"\t {(i)} : {pelicula[i]}")
  else:
       print("\.:: No hay peliculas en el sistema ::.")

def borrarPeliculas():#
   borrarPantalla()
   print("\n\t\t.:: \u274C Borrar o quitar TODAS las Peliculas \u274C ::.\n")
   resp=input("¿Deseas quitar o borrar todas las peliculas del sistema (si/no)")

   if resp=="si":
    pelicula.clear()
    input("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705 :::")
    
    
   else:
       print("\.:: No hay peliculas en el sistema ::.")

def agregarCaracteristicaPeliculas():
   borrarPantalla()
   print("\n\t\t.::  Agregar caracteristicas a las Peliculas ::.\n")
   atributo=input(" \U0001F501 Ingresa la nueva caractersitica de la pelicla: ").lower().strip()
   valor=input(" \U0001F501 Ingesa el valor de la caracteristica de la pelicula").upper().strip()
   pelicula.update({atributo:input("Ingresa el nombre").upper().strip()})
   pelicula[atributo]=valor
   pelicula.update({atributo:valor})
   input("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705 :::")

def modificarCaracteristicaPeliculas():
   borrarPantalla()
   print("\n\t .::\U0001F501 Modificar caracteristicas a Peliculas \U0001F501::. \n ")
   if len(pelicula)>0:
      print(f"\n\t Valores acruales: \n")
      for i in pelicula:
         print(f"\t {(i)} : {pelicula[i]} ")
         resp=input(f"\t ¿Deseas cambiar el valor de {i}? (si/no)").lower().strip()
         if resp =="si":
            pelicula.update({f"{i}": input("\t \U0001F501 el nuevo valor: ").upper().strip()}) 
            print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705:::")
            esperarTecla()
            borrarPantalla()
         else:
            print("\t .:: \u26A0 No hay peliculas en el sitema ::. \u26A0 ")
            esperarTecla()


def borrarCaracteristicaPeliculas():
   borrarPantalla()
   try:
      print("\n\t .::\U0001F4DB  Borrar  caracgeristica a Peliculas  \U0001F4DB::. \n")
      if len(pelicula)>0:
         print(f"\n\t Valores acruales: \n")
         for i in pelicula:
            print(f"\t {(i)} : {pelicula[i]} ")
            opc=True
            while opc:
               resp=input(f"\t ¿Deseas borrar una caracteristica (si/no)").lower().strip()
               if resp =="si":
                  atributo=input("Escribe la caracteristica que deseas borrar o quitar: ")
                  pelicula.pop(atributo)
                  print("\n\t\t ::: \u2705 !LA OPERACION SE REALIZO CON EXITO¡ \u2705::.")
               elif resp =="no":
                  opc=False
                  esperarTecla()
                  borrarPantalla()
      else:
               print("\t .:: \u26A0 No hay peliculas en el sitema ::. \u26A0 ")
               esperarTecla()
   except KeyError:
      print("\u26A0 No existe esa caracteristica porfavor verifique \u26A0....")






















#def vaciarPeliculas():
   #borrarPantalla()
  # print("\n\t .::Borrar o quitar TODAS las peliculas ::. ")
   #resp=input("¿Deseas quitar o borrar TODAS las peliculas del sistema? (si/no)").lower()
  # if resp=="si":
     # pelicula.clear()
     # input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")

#def buscarPeliculas():
   
 #  borrarPantalla()
  # print("\n\t .::Buscar peliculas ::. ")
   #pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
  # encontro=0
   #if not(pelicula_buscar in peliculas):
    #  print("\n\t\t No se encontro la pelicula a buscar")
   #else:
    #  for i in range(0, len(peliculas)):
     
     #    if pelicula_buscar==peliculas[i]:
      #      print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
       #     encontro+=1
      #if encontro>0:
       # print(f"Tenemmos {encontro} pelicula(s) con este titulo ")
       # input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")

#def eliminarPeliculas():
   #borrarPantalla()
   #pel=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
   #encontro=0
   #if (not pel in pelicula):
     # #input("\n\t\t .:: OPRIMA UNA TECLA PARA CONTINUAR ::.")
 #  else:
    #  opc="si"
      
     # while pel in pelicula and opc=="si":
        # opc=input("¿Desea quitar o borrar la pelicula del sistema? (si/no)").lower() .strip()
        # if opc == "si":
        #    posicion=pelicula.index(pel)
        #    print(f"La pelicula que se borro es: {pel} y estaba en la casilla{posicion+1}")
        #    pelicula.remove(pel)
        #    encontro+=1
         #   input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")
     # print(f"se borro {encontro} pelicula(s) con este titulo")


#def modificarCaracteristicaPeliclas():
  # borrarPantalla()
  # print("\n\t.:: Modificar caracteristicas Películas ::. \n")
  # pelicula_modificar=input("Ingrese la pelicula a la que le quiera modificar la caracteristica: ").upper().strip()
  # if len(pelicula)>0:
   #   for i in range(0,len(pelicula)):
  #       if pelicula_modificar==pelicula[i]:
   #         resp=input("¿Deseas actualizar una caracteristica de la pelicula? (si/no)").lower().strip()
   #         if resp=="si":
   #           atributo=input("Ingresa la nueva caractersitica de la pelicula: ").lower().strip()
   #           valor=input("Ingesa el valor de la caracteristica de la pelicula").upper().strip()             
   #           pelicula_modificar=pelicula.update({atributo:valor})
       
  # else:
   #   print("\n\t\t ¡No se encuentra la película a buscar!")  
      




#def modificarPeliculas():
  # #borrarPantalla()
  # print("\n\t.:: Modificar Películas ::. \n")
  # pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
  # encontro=0
  # if not(pelicula_buscar in peliculas): 
 #     print("\n\t\t ¡No se encuentra la película a buscar!")   
  # else:   
  #    for i in range(0,len(peliculas)):
  #      if pelicula_buscar==peliculas[i]:
  #        resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
  #        if resp=="si":
   #          pelicula[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
  #           encontro+=1
  #           print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
  #    
   #   print(f"\nSe modifico {encontro} pelicula(s) con este titulo")

#Hacer la opcion 5 y 6




''' 
       peliculas.remove(pel)
       for i in range (0,len(peliculas)):
          if pel == peliculas[i]:
             print(f"La pelicula que se borro es: {pel} y estaba en la casilla{i+1}")
             borradas+=1
       print(f"se borro {borradas} pelicula(s) con ese titulo")
       input("\n\t\t ...Oprima cualquier tecla para continuar...")
'''      