peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingrese el nombre: ").upper().strip())
  input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")

def consultarPeliculas():
  borrarPantalla()
  print("\n\t\t.:: Consultar o Mostrar las Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
        print(f"{i+1}: {peliculas[i]}")
    else:
        print("\t .:: No hay peliculas en el Sistema ::.")

def vaciarPeliculas():
   borrarPantalla()
   print("\n\t .::Borrar o quitar TODAS las peliculas ::. ")
   resp=input("¿Deseas quitar o borrar TODAS las peliculas del sistema? (si/no)").lower()
   if resp=="si":
      peliculas.clear()
      input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")

def buscarPeliculas():
   
   borrarPantalla()
   print("\n\t .::Buscar peliculas ::. ")
   pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas):
      print("\n\t\t No se encontro la pelicula a buscar")
   else:
      for i in range(0, len(peliculas)):
         if pelicula_buscar==peliculas[i]:
            print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
            encontro+=1
      if encontro>0:
        print(f"Tenemmos {encontro} pelicula(s) con este titulo ")
        input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")

def eliminarPeliculas():
   borrarPantalla()
   pel=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
   encontro=0
   if (not pel in peliculas):
      print("No se encontro ningun elemento con ese nombre")
      input("\n\t\t .:: OPRIMA UNA TECLA PARA CONTINUAR ::.")
   else:
      opc="si"
      
      while pel in peliculas and opc=="si":
         opc=input("¿Desea quitar o borrar la pelicula del sistema? (si/no)").lower() .strip()
         if opc == "si":
            posicion=peliculas.index(pel)
            print(f"La pelicula que se borro es: {pel} y estaba en la casilla{posicion+1}")
            peliculas.remove(pel)
            encontro+=1
            input("\n\t\t :::!LA OPERACION SE REALIZO CON EXITO¡:::")
      print(f"se borro {encontro} pelicula(s) con este titulo")


def modificarPeliculas():
   borrarPantalla()
   print("\n\t.:: Modificar Películas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la película a buscar!")   
   else:   
      for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
          if resp=="si":
             peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
             encontro+=1
             print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")

          
''' 
       peliculas.remove(pel)
       for i in range (0,len(peliculas)):
          if pel == peliculas[i]:
             print(f"La pelicula que se borro es: {pel} y estaba en la casilla{i+1}")
             borradas+=1
       print(f"se borro {borradas} pelicula(s) con ese titulo")
       input("\n\t\t ...Oprima cualquier tecla para continuar...")
'''      