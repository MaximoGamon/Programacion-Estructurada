import funciones
from usuarios import usuario
from medicamentos import medicamentos
from clientes import clientes
from ventas import venta
from Proveedores import Proveedor
import getpass
import pandas as pd

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()
        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t¿Cual es tu nombre de usuario?: ").upper().strip()
            opt=True
            while opt:
                if len(nombre)>0:
                    opt=False
                else:
                    nombre=input("\tNo se ha ingresado ningun nombre, intentelo de nuevo...\n\t")

            email=input("\tIngresa tu email: ").lower().strip()
            opt=True
            while opt:
                if len(email)>0:
                    resultado=usuario.comprobar(email)
                    if resultado:
                        email=input("\tEl email ingresado ya esta en uso, ingrese otro... \n\t").lower().strip()
                    else:
                        opt=False
                else:
                    email=input("\tNo se ha ingresado ningun email, intentelo de nuevo...\n\t")
            
            password=getpass.getpass("\tIngresa tu contraseña: ").strip()
            opt=True
            while opt:
                if len(password)>0:
                    opt=False
                else:
                    password=getpass.getpass("\tNo se ha ingresado ninguna contraseña, intentelo de nuevo...\n\t")
            #La carpeta usuarios
            resultado=usuario.registrar(nombre,email,password)
            if resultado:
                print(f"\n\t{nombre}, se registro correctamente, con el email {email}")
            else:
              print(f"\n\t...Por favor intentelo denuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Carpeta de usuarios
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_principal(registro[1],registro[2])
            else:
                print(f"\n\tE-mail y/o contraseña incorrectas, vuelva a intentarlo...")
            funciones.esperarTecla()

        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema \n\n\t🗿\n")
            opcion=False
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_principal(nombre,apellidos):
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_principal()
        match opcion:
            case "1":
                opcion_secundaria=True
                while opcion_secundaria:
                    opcion_secundaria=funciones.menu_medicamentos()
                    match opcion_secundaria:
                        case "1":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F4DD Agregar Medicamentos \U0001F4DD ::.\n")
                            print(f"{'-'*40}")
                            nombre=input("\tNombre del medicamento: ").upper().strip()
                            desc=input("\tDescripcion del medicamento: ").upper().strip()
                            op=True
                            while op:
                                try:
                                    precio=float(input("\tPrecio unitario del medicamento: ").strip())
                                    if precio!=None:
                                        op=False
                                except ValueError:
                                    print("\tDato no aceptado, favor de ingresar un dato numerico")
                            op=True
                            while op:
                                try:
                                    mg=int(input("\tMg. por caja del medicamento: ").strip())
                                    if mg!=None:
                                        op=False
                                except ValueError:
                                    print("\tDato no aceptado, favor de ingresar un dato numerico entero")
                            op=True
                            while op:
                                try:
                                    inventario=int(input("\tCantidad en inventario: ").strip())
                                    if inventario!=None:
                                        op=False
                                except ValueError:
                                    print("\tDato no aceptado, favor de ingresar un dato numerico entero ")
                            print(f"{'-'*40}")
                            respuesta=medicamentos.agregar(nombre,desc,precio,mg,inventario)
                            if respuesta:
                                print("\n\t\t\t\u2705 Accion realizada con exito ")
                            else:
                                print(f"\n\tNo fue posible agregar el medicamento en este momento, vuelva a intentar ...")
                            funciones.esperarTecla()
                        case "2":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F501 Modificar Medicamento \U0001F501 ::.\n")
                            print(f"{'-'*40}")
                            respuesta=medicamentos.consultar()
                            if len(respuesta)>0:
                                cont=1
                                for i in respuesta:
                                    print(f"\t\t{cont}: {i[1]}")
                                    print(f"{'-'*40}")
                                    cont+=1
                                op=True
                                res=input("¿Deseas modificar algun medicamento? (Si/No) ").upper().strip()
                                opc=True
                                while opc:
                                    if res=="SI":
                                        while op:
                                            try:
                                                modif=int(input("Teclea el numero de medicamento a modificar "))
                                                if modif!=None:
                                                    if modif>0 and modif<=len(respuesta):
                                                        op=False
                                                    else:
                                                        print("No hay medicamento con ese numero asignado")
                                            except ValueError:
                                                print("Dato no aceptado, favor de ingresar un dato numerico entero")
                                        print(f"{'-'*40}")
                                        modif=modif-1
                                        print(f"\tNombre: {respuesta[modif][1]}\n\tDescripcion: {respuesta[modif][2]}\n\tPrecio: {respuesta[modif][3]}\n\ttMiligramos: {respuesta[modif][4]}\n\tInventario: {respuesta[modif][5]}")
                                        print(f"{'-'*40}")
                                        opc2=True
                                        while opc2:
                                            nom=input(f"¿Deseas modificar el nombre '{respuesta[modif][1]}'? (Si/No) ").strip().upper()
                                            if nom=="SI":
                                                nom=input("Teclea el nuevo valor para nombre: ").upper().strip()
                                                opc2=False
                                            elif nom=="NO":
                                                opc2=False
                                                nom=respuesta[modif][1]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        opc2=True
                                        while opc2:
                                            desc=input(f"¿Deseas modificar la descripcion '{respuesta[modif][2]}'? (Si/No) ").strip().upper()
                                            if desc=="SI":
                                                desc=input("Teclea el nuevo valor para descripcion: ").upper().strip()
                                                opc2=False
                                            elif desc=="NO":
                                                opc2=False
                                                desc=respuesta[modif][2]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        opc2=True
                                        while opc2:
                                            precio=input(f"¿Deseas modificar el precio '{respuesta[modif][3]}'? (Si/No) ").strip().upper()
                                            if precio=="SI":
                                                op=True
                                                while op:
                                                    try:
                                                        precio=float(input("Teclea el nuevo valor para el precio: ").upper().strip())
                                                        if precio!=None:
                                                            op=False
                                                    except ValueError:
                                                        print("Dato no aceptado, favor de ingresar un dato numerico ")
                                                opc2=False
                                            elif precio=="NO":
                                                opc2=False
                                                precio=respuesta[modif][3]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        opc2=True
                                        while opc2:
                                            milig=input(f"¿Deseas modificar los miligramos '{respuesta[modif][4]}'? (Si/No) ").strip().upper()
                                            if milig=="SI":
                                                op=True
                                                while op:
                                                    try:
                                                        milig=float(input("Teclea el nuevo valor para los miligramos: ").upper().strip())
                                                        if milig!=None:
                                                            op=False
                                                    except ValueError:
                                                        print("Dato no aceptado, favor de ingresar un dato numerico ")                    
                                                opc2=False
                                            elif milig=="NO":
                                                opc2=False
                                                milig=respuesta[modif][4]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        opc2=True
                                        while opc2:
                                            invent=input(f"¿Deseas modificar el inventario '{respuesta[modif][5]}'? (Si/No) ").strip().upper()
                                            if invent=="SI":
                                                op=True
                                                while op:
                                                    try:
                                                        invent=int(input("Teclea el nuevo valor para el inventario: ").upper().strip())
                                                        if invent!=None:
                                                            op=False
                                                    except ValueError:
                                                        print("Dato no aceptado, favor de ingresar un dato numerico entero ")
                                                opc2=False
                                            elif invent=="NO":
                                                opc2=False
                                                invent=respuesta[modif][5]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        medicamentos.modificar(respuesta[modif][0],nom,desc,precio,milig,invent)
                                        opc=False
                                    elif res=="NO":
                                        print("La operacion se ha cancelado")
                                        opc=False
                                    else:
                                        print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        res=input("¿Deseas modificar algun medicamento? (Si/No) ").upper().strip()
                                print("\n\t\t\t\u2705 Accion realizada con exito ") 
                            else:
                                print("No hay medicamentos en el sistema ")
                            funciones.esperarTecla()
                        case "3":
                            funciones.borrarPantalla()
                            print("\n\t.:: Eliminar Medicamento ::. \n")
                            respuesta=medicamentos.consultar()
                            print(f"{'-'*40}")
                            if len(respuesta)>0:
                                cont=1
                                for i in respuesta:
                                    print(f"\t\t{cont}: {i[1]}")
                                    print(f"{'-'*40}")
                                    cont+=1
                                elim=input("¿Deseas eliminar un medicamento? (Si/No) ").upper().strip()
                                op=True
                                while op:
                                    if elim=="SI":
                                        op=True
                                        while op:
                                            try:
                                                elim=int(input("Teclea el numero de medicamento a eliminar "))
                                                if elim!=None:
                                                    if elim>0 and elim<=len(respuesta):
                                                        op=False
                                                    else:
                                                        print("No hay medicamento con ese numero asignado ")    
                                                else:
                                                    print("No hay medicamento con ese numero asignado ")
                                            except ValueError:
                                                print("Dato no aceptado, favor de ingresar un dato numerico entero")
                                        elim=elim-1
                                        res=medicamentos.eliminar(respuesta[elim][0])
                                        if res:
                                            print("\n\t\t\t\u2705 Accion realizada con exito ")  
                                        else:
                                            print("La eliminacion no su pudo realizar, vuelva a intentarlo... ")
                                    elif elim=="NO":
                                        print("La operacion se ha cancelado")
                                        op=False
                                    else:
                                        print("No se ha seleccionado una opcion valida, por favor volver a intntar")
                                        elim=input("¿Deseas eliminar un medicamento? (Si/No)").upper().strip()
                            else:
                                print("No hay medicamentos en el sistema")
                            funciones.esperarTecla()
                        case "4":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F50D Consultar Medicamento \U0001F50D ::. \n")
                            print(f"{'-'*40}")
                            respuesta=medicamentos.consultar()
                            if len(respuesta)>0:
                                for i in respuesta:
                                    print(f"Nombre: {i[1]}")
                                    print(f"Descripcion: {i[2]}")
                                    print(f"Precio: {i[3]}")
                                    print(f"Miligramos: {i[4]}")
                                    print(f"Inventario: {i[5]}")
                                    print(f"{'-'*40}")
                            else:
                                print("No hay medicamentos en el sistema")
                            funciones.esperarTecla()
                        case "5":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F50D Exportar inventario \U0001F50D ::. \n")
                            imprimida,columns=medicamentos.exportar()
                            if len(imprimida)>0:
                                op=True
                                while op:
                                    expo= input("¿Deseas exportar el inventario en excel? (Si/No) ").upper().strip()
                                    if expo=="SI":
                                        df=pd.DataFrame(imprimida,columns=columns)
                                        df.to_excel("bd_medicamentos.xlsx", index=False)
                                        print("Accion realizada exitosamente")
                                        op=False
                                    elif expo=="NO":
                                        print("Se cancelo la operacion...")
                                        op=False
                                    else:
                                        print("No se ha seleccionad una opcion valida")
                            else:
                                print("No hay ventas en el sistema")
                            funciones.esperarTecla()
                        case "6":
                            opcion_secundaria=False
                        case _:
                            input("\n\t\u26A0 \033[31m Opción invalida vuelva a intentarlo ... por favor \033[0m\u26A0 ")
            case "2":
                opcion_secundaria=True
                while opcion_secundaria:
                    opcion_secundaria=funciones.menu_clientes()
                    match opcion_secundaria:
                        case "1":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F4DD Agregar Clientes \U0001F4DD ::.\n")
                            print(f"{'-'*40}")
                            nombre=input("\t\U0001F464 Nombre del cliente: ").upper().strip()
                            alergias=input("\t\u26A0 Alergias que possea el cliente: ").upper().strip()
                            op=True
                            while op:
                                try:
                                    telefono=int(input("\t\U0001F4DE Numero de contacto del cliente (10 digitos): ").strip())
                                    if telefono!=None:
                                        if len(str(telefono))==10:
                                            op=False
                                        else:
                                            print("Dato no aceptado, favor de ingresar un dato numerico de 10 digitos")
                                except ValueError:
                                    print("\tDato no aceptado, favor de ingresar un dato numerico")
                            respuesta=clientes.agregar(nombre,alergias,telefono)
                            if respuesta:
                                print("\n\t\t\t\u2705 Accion realizada con exito ")
                            else:
                                print(f"\n\tNo fue posible agregar a el cliente en este momento, vuelva a intentar ...")
                            funciones.esperarTecla()
                        case "2":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F501 Editar Clientes \U0001F501 ::. \n")
                            print(f"{'-'*40}")
                            respuesta=clientes.consultar()
                            if len(respuesta)>0:
                                cont=1
                                for i in respuesta:
                                    print(f"\t\t{cont}: {i[1]}")
                                    print(f"{'-'*40}")
                                    cont+=1
                                op=True
                                res=input("¿Deseas modificar algun Cliente? (Si/No) ").upper().strip()
                                opc=True
                                while opc:
                                    if res=="SI":
                                        while op:
                                            try:
                                                modif=int(input("Teclea el numero del cliente a modificar "))
                                                if modif!=None:
                                                    if modif>0 and modif<=len(respuesta):
                                                        op=False
                                                    else:
                                                        print("No hay cliente con ese numero asignado ")
                                            except ValueError:
                                                print("Dato no aceptado, favor de ingresar un dato numerico entero ")      
                                        modif=modif-1
                                        print(f"{'-'*40}")
                                        print(f"\tNombre: {respuesta[modif][1]}\n\tAlergias: {respuesta[modif][2]}\n\tContacto: {respuesta[modif][3]}")
                                        print(f"{'-'*40}")
                                        opc2=True
                                        while opc2:
                                            nom=input(f"¿Deseas modificar el nombre '{respuesta[modif][1]}'? (Si/No) ").strip().upper()
                                            if nom=="SI":
                                                nom=input("Teclea el nuevo valor para nombre: ").upper().strip()
                                                opc2=False
                                            elif nom=="NO":
                                                opc2=False
                                                nom=respuesta[modif][1]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")

                                        opc2=True
                                        while opc2:
                                            alergias=input(f"¿Deseas modificar las alergias '{respuesta[modif][2]}'? (Si/No) ").strip().upper()
                                            if alergias=="SI":
                                                alergias=input("Teclea el nuevo valor para alergias: ").upper().strip()
                                                opc2=False
                                            elif alergias=="NO":
                                                opc2=False
                                                alergias=respuesta[modif][2]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")

                                        opc2=True
                                        while opc2:
                                            telefono=input(f"¿Deseas modificar el numero de contacto '{respuesta[modif][3]}'? (Si/No) ").strip().upper()
                                            if telefono=="SI":
                                                op=True
                                                while op:
                                                    try:
                                                        telefono=int(input("Teclea el nuevo valor para el numero de contacto: ").upper().strip())
                                                        if telefono!=None:
                                                            if len(str(telefono))==10:
                                                                op=False
                                                                opc2=False
                                                            else:
                                                                print("Dato no aceptado, favor de ingresar un dato numerico de 10 digitos ")
                                                    except ValueError:
                                                        print("Dato no aceptado, favor de ingresar un dato numerico ")
                                            elif telefono=="NO":
                                                opc2=False
                                                telefono=respuesta[modif][3]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        print(f"{'-'*40}")
                                        respuesta=clientes.modificar(respuesta[modif][0],nom,alergias,telefono)
                                        if respuesta:
                                            print("\n\t\t\t\u2705 Accion realizada con exito ")
                                        else:
                                            print(f"\n\tNo fue posible modificar a el cliente en este momento, vuelva a intentar ... ")
                                        opc=False  
                                    elif res=="NO":
                                        print("La operacion se ha cancelado")
                                        opc=False
                                    else:
                                        print("No se ha seleccionado una opcion valida, por favor volver a intentar ")
                                        res=input("¿Deseas modificar algun Cliente? (Si/No) ").upper().strip()
                            else:
                                print("No hay clientes en el sistema ")
                            funciones.esperarTecla()
                        case "3":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F50D Buscar Clientes \U0001F50D ::. \n")
                            print(f"{'-'*40}")
                            respuesta=clientes.consultar()
                            res=0
                            if len(respuesta)>0:
                                busc=input("Ingresa el nombre del cliente que desea buscar: ").upper().strip()
                                for i in respuesta:
                                    if i[1]==busc:
                                        print(f"{'-'*40}")
                                        print(f"Nombre: {i[1]}")
                                        print(f"Alergias: {i[2]}")
                                        print(f"Contacto: {i[3]}")
                                        print(f"{'-'*40}")
                                        res=1
                                if res==0:
                                    print("No se encontro cliente con ese nombre")
                                else:
                                    print("\n\t\t\t\u2705 Accion realizada con exito ")  
                            else:
                                print("No hay clientes en el sistema")
                            funciones.esperarTecla()
                        case "4":
                            opcion_secundaria=False
                        case _:
                            input("\n\t\u26A0 \033[31m Opción invalida vuelva a intentarlo ... por favor \033[0m\u26A0 ")
            case "3":
                opcion_secundaria=True
                while opcion_secundaria:
                    opcion_secundaria=funciones.menu_ventas()
                    match opcion_secundaria:
                        case "1":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F4DD Agregar nueva venta \U0001F4DD ::.\n")
                            respuesta=medicamentos.consultar()
                            if len(respuesta)>0:
                                res=input("¿Deseas comprar algun medicamento? (Si/No)").upper().strip()
                                if res=="SI":
                                    cliente=input("Ingresa el nombre del cliente ")
                                    repetir=True
                                    while repetir:
                                        print(f"{'-'*40}")
                                        cont=1
                                        print("Medicamentos")
                                        print(f"\t{'ID':<10}{'Nombre':<20}{'Precio':<20}")
                                        for i in respuesta:
                                            print(f"\t{cont:<10}{i[1]:<20}{i[3]:<20}")
                                            cont+=1
                                        print(f"{'-'*40}")
                                        op=True
                                        opc=True
                                        while opc:
                                            while op:
                                                try:
                                                    modif=int(input("Teclea el numero de medicamento a comprar "))
                                                    if modif!=None:
                                                        if modif>0 and modif<=len(respuesta):
                                                            op=False
                                                        else:
                                                            print("No hay medicamento con ese numero asignado ")
                                                except ValueError:
                                                    print("Dato no aceptado, favor de ingresar un dato numerico entero ")
                                            modif=modif-1
                                            op=True
                                            while op:
                                                try:
                                                    cantidad = int(input("Ingrese la cantidad de productos que compro: "))
                                                    if cantidad!=None:
                                                        op=False
                                                except ValueError:
                                                    print("Dato no aceptado, favor de ingresar un dato numerico entero")
                                            producto=respuesta[modif][1]
                                            precio=respuesta[modif][3]
                                            total=precio*cantidad
                                            id_medicamento=respuesta[modif][0]
                                            res,id=venta.venta_Nueva(cliente,producto,precio,cantidad,total,id_medicamento)
                                            if res:
                                                print(f"{'-'*140}")
                                                print("Ticket")
                                                print(f"\t{'ID':<10}{'Cliente':<20}{'Producto':<20}{'Precio':<20}{'Cantidad':<20}{'Total':<20}{'ID Medicamento':<20}")
                                                print(f"\t{id:<10}{cliente:<20}{producto:<20}{precio:<20}{cantidad:<20}{total:<20}{id_medicamento:<20}")
                                                print(f"{'-'*140}")
                                            opc=False
                                            opc3=True
                                            while opc3:
                                                repetir=input("¿Deseas comprar otro medicamento? (Si/No)").upper().strip()
                                                if repetir=="SI":
                                                    opc3=False
                                                    funciones.borrarPantalla()
                                                    print("\n\t.:: \U0001F4DD Agregar nueva venta \U0001F4DD ::.\n")
                                                elif repetir=="NO":
                                                    opc3=False
                                                    repetir=False
                                                else:
                                                    print("No se selecciono una opcion")
                                elif res=="NO":
                                    print("La operacion se ha cancelado")
                                    opc=False
                                else:
                                    print("No se ha seleccionado una opcion valida, por favor volver a intentar")
                                    res=input("¿Deseas comprar algun medicamento? (Si/No)").upper().strip()
                            else:
                                print("No hay medicamentos en el sistema valida, por favor volver a intentar")
                            funciones.esperarTecla()
                        case "2":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F50D Consultar ventas \U0001F50D ::. \n")
                            id_ventas= input("Ingrese el id de la venta a buscar ")
                            imprimida=venta.consultarVenta(id_ventas)
                            if len(imprimida)>0:
                                print(f"\n{'-'*80}")
                                print(f"{'Id Ventas':<10}{'Cliente':<10}{'Produto':<10}{'Precio':<10}{'Cantidad':<10}{'Total':<10}{'Id_medicamento':<10}")
                                print("-"*80)
                                for i in imprimida:
                                    print(f"{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<10}{i[5]:<10}{i[6]:<10}")
                            else:
                                print("No hay ventas registradas con ese ID")
                            funciones.esperarTecla()
                        case "3":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F50D Exportar ventas \U0001F50D ::. \n")
                            imprimida,columns=venta.consultar()
                            if len(imprimida)>0:
                                op=True
                                while op:
                                    expo= input("¿Deseas exportar las ventas en excel? (Si/No) ").upper().strip()
                                    if expo=="SI":
                                        df=pd.DataFrame(imprimida,columns=columns)
                                        df.to_excel("bd_ventas.xlsx", index=False)
                                        print("Accion realizada exitosamente")
                                        op=False
                                    elif expo=="NO":
                                        print("Se cancelo la operacion...")
                                        op=False
                                    else:
                                        print("No se ha seleccionad una opcion valida")
                            else:
                                print("No hay ventas en el sistema")
                            funciones.esperarTecla()
                        case "4":
                            opcion_secundaria=False
                        case _:
                            input("\n\t\u26A0 \033[31m Opción invalida vuelva a intentarlo ... por favor \033[0m\u26A0 ")
            case "4":
                opcion_secundaria=True
                while opcion_secundaria:
                    opcion_secundaria=funciones.menu_proveedores()
                    match opcion_secundaria:
                        case "1":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F4C2 REGISTRAR PROVEEDOR \U0001F4C2 ::.\n")
                            print(f"{'-'*40}")
                            op=True
                            while op:
                                proveedor=input("Nombre del proveedor: ").upper().strip()
                                res=Proveedor.buscarProveedor(proveedor)
                                if len(res)>0:
                                    print(f"El nombre {proveedor} ya esta en uso en este sistema, ingrese otro por favor")
                                else:
                                    op=False
                            direccion=input("Direccion: ").upper().strip()
                            email=input("E-mail: ").lower().strip()
                            op=True
                            while op:
                                try:
                                    telefono=input("Telfono (10 digitos): ")
                                    if telefono!=None:
                                        if len(str(telefono))==10:
                                            op=False
                                        else:
                                            print("Dato no aceptado, favor de ingresar un dato numerico de 10 digitos ")
                                except ValueError:
                                    print("Dato no aceptado, favor de ingresar un dato numerico ")
                            Proveedor.registrarProveedor(proveedor,direccion,email,telefono)
                            funciones.esperarTecla()
                        case "2":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F501 Editar proveedor \U0001F501 ::. \n")
                            print(f"{'-'*40}")
                            respuesta=Proveedor.consultar_Provededores()
                            if len(respuesta)>0:
                                cont=1
                                for i in respuesta:
                                    print(f"\t\t{cont}: {i[1]}")
                                    print(f"{'-'*40}")
                                    cont+=1
                                op=True
                                res=input("¿Deseas modificar algun proveedor? (Si/No) ").upper().strip()
                                opc=True
                                while opc:
                                    if res=="SI":
                                        while op:
                                            try:
                                                modif=int(input("Teclea el numero del proveedor a modificar "))
                                                if modif!=None:
                                                    if modif>0 and modif<=len(respuesta):
                                                        op=False
                                                    else:
                                                        print("No hay cliente con ese numero asignado ")
                                            except ValueError:
                                                print("Dato no aceptado, favor de ingresar un dato numerico entero ")
                                        modif=modif-1
                                        print(f"{'-'*40}")
                                        print(f"\tProveedor: {respuesta[modif][1]}\n\tDireccion: {respuesta[modif][2]}\n\tE-mail: {respuesta[modif][3]}\n\tTelefono: {respuesta[modif][4]}")
                                        print(f"{'-'*40}")
                                        opc2=True
                                        while opc2:
                                            nom=input(f"¿Deseas modificar el nombre del proveedor '{respuesta[modif][1]}'? (Si/No)").strip().upper()
                                            if nom=="SI":
                                                nom=input("Teclea el nuevo valor para nombre: ").upper().strip()
                                                opc2=False
                                            elif nom=="NO":
                                                opc2=False
                                                nom=respuesta[modif][1]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar")

                                        opc2=True
                                        while opc2:
                                            direccion=input(f"¿Deseas modificar la direccion '{respuesta[modif][2]}'? (Si/No)").strip().upper()
                                            if direccion=="SI":
                                                direccion=input("Teclea el nuevo valor para la direccion: ").upper().strip()
                                                opc2=False
                                            elif direccion=="NO":
                                                opc2=False
                                                direccion=respuesta[modif][2]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar")

                                        opc2=True
                                        while opc2:
                                            email=input(f"¿Deseas modificar el E-mail'{respuesta[modif][3]}'? (Si/No)").strip().upper()
                                            if email=="SI":
                                                email=input("Teclea el nuevo E-mail: ").upper().strip()
                                                opc2=False
                                            elif email=="NO":
                                                opc2=False
                                                email=respuesta[modif][3]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar")


                                        opc2=True
                                        while opc2:
                                            telefono=input(f"¿Deseas modificar el numero de contacto '{respuesta[modif][4]}'? (Si/No)").strip().upper()
                                            if telefono=="SI":
                                                op=True
                                                while op:
                                                    try:
                                                        telefono=int(input("Teclea el nuevo valor para el numero de contacto: ").upper().strip())
                                                        if telefono!=None:
                                                            if len(str(telefono))==10:
                                                                op=False
                                                                opc2=False
                                                            else:
                                                                print("Dato no aceptado, favor de ingresar un dato numerico de 10 digitos")
                                                    except ValueError:
                                                        print("Dato no aceptado, favor de ingresar un dato numerico ")
                                            elif telefono=="NO":
                                                opc2=False
                                                telefono=respuesta[modif][4]
                                            else:
                                                print("No se ha seleccionado una opcion valida, por favor volver a intentar")
                                        print(f"{'-'*40}")
                                        respuesta=Proveedor.modificar(respuesta[modif][0],nom,direccion,email,telefono)
                                        if respuesta:
                                            print("\n\t\t\t\u2705 Accion realizada con exito ")
                                        else:
                                            print(f"\n\tNo fue posible modificar a el cliente en este momento, vuelva a intentar ...")
                                        opc=False  
                                    elif res=="NO":
                                        print("La operacion se ha cancelado")
                                        opc=False
                                    else:
                                        print("No se ha seleccionado una opcion valida, por favor volver a intntar")
                                        res=input("¿Deseas modificar algun Cliente? (Si/No)").upper().strip()
                            else:
                                print("No hay clientes en el sistema")
                            funciones.esperarTecla()                  
                        case "3":
                            funciones.borrarPantalla()
                            print("\n\t.:: \U0001F50D Buscar provedores \U0001F50D ::.\n")
                            provedor= input("Ingrese el nombre del proveedor a buscar: ")
                            print(f"{'-'*140}")
                            imprimida=Proveedor.buscarProveedor(provedor)
                            if len(imprimida)>0:
                                print(f"{'Id Proveedores':<20}{'Proveedor':<20}{'direccion':<20}{'Email':<20}{'Telefono':<20}")
                                print("-"*140)
                                for i in imprimida:
                                    print(f"{i[0]:<20}{i[1]:<20}{i[2]:<20}{i[3]:<20}{i[4]:<20}")
                                    print(f"{'-'*140}")
                            else:
                                print("No hay proveedores registrados con ese ID")
                            funciones.esperarTecla()   
                        case "4":
                            opcion_secundaria=False
                        case _:
                            input("\n\t\u26A0 \033[31m Opción invalida vuelva a intentarlo ... por favor \033[0m\u26A0 ")
            case "5":
                opcion=False
                print("\n\t\t\t\t🗿Terminaste la ejecucion del SW")
            case _:
                input("\n\t\u26A0 \033[31m Opción invalida vuelva a intentarlo ... por favor \033[0m\u26A0 ")

if __name__=="__main__":
    main()