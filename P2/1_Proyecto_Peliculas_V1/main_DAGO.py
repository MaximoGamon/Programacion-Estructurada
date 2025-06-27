import peliculas_DAGO

opcion=True
while opcion:
    peliculas_DAGO.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_DAGO.agregarPeliculas()
            print(".:: Agregar Peliculas ::.")
            peliculas_DAGO.esperarTecla()
        case "2":
            peliculas_DAGO.eliminarPeliculas()
            print(".:: Eliminar Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
        case "3":
            peliculas_DAGO.modificarPeliculas()
            print(".:: Modificar Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
                
        case "4":
            peliculas_DAGO.consultarPeliculas()
            print(".:: Consultar Peliculas ::.")
            peliculas_DAGO.esperarTecla()
        case "5":
            peliculas_DAGO.buscarPeliculas()
            print(".:: Buscar Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
        case "6":
            peliculas_DAGO.vaciarPeliculas()
            peliculas_DAGO.esperarTecla()
            print(".:: Vacias Peliculas ::.") 
            peliculas_DAGO.esperarTecla()
        case "7":
            
            opcion=False   
            peliculas_DAGO.borrarPantalla() 
            print("\n\tTerminaste la ejecucion del SW")
        case _:
             
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")