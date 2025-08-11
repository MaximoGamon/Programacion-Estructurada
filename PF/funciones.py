def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar ...")

def menu_usurios():
   print("\n \t.:: Sistema de Gestión de una farmacia ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
   opcion=input("\t\t Elige una opción: ").upper().strip() 
   return opcion

def menu_principal():
    borrarPantalla()
    print("\n\t\t\t\U0001F50D...::: Sistema informatico en consola para la gestion de una farmacia :::...\U0001F50D\n\t\t\t\t" \
    "1️⃣- Gestion de medicamentos\n\t\t\t\t" \
    "2️⃣- Gestion de clientes\n\t\t\t\t" \
    "3️⃣- Ventas\n\t\t\t\t" \
    "4️⃣- Provedores\n\t\t\t\t" \
    "\U0001F6AA - Salir")
    opcion=input("\t\t\t\tElige una opción (1-5): ").upper()
    return opcion

#Medicamentos
def menu_medicamentos():
    borrarPantalla()
    print("\n\t\t\t\U0001F50D...::: Gestion de medicamentos :::...\U0001F50D\n\t\t\t\t" \
    "1️⃣- Agregar nuevo medicamento\n\t\t\t\t" \
    "2️⃣- Modificar medicamento\n\t\t\t\t" \
    "3️⃣- Eliminar medicamento\n\t\t\t\t" \
    "4️⃣- Consultar medicamento\n\t\t\t\t" \
    "5️⃣- Exportar inventario\n\t\t\t\t" \
    "\U0001F6AA - Volver al menu principal")
    opcion=input("\t\t\t\tElige una opción (1-6): ").upper()
    return opcion

#Clientes
def menu_clientes():
    borrarPantalla()
    print("\n\t\t\t\U0001F4C2...::: Gestion de clientes :::...\U0001F4C2\n\t\t\t\t" \
    "1️⃣- Registrar nuevo cliente\n\t\t\t\t" \
    "2️⃣- Editar datos de cliente\n\t\t\t\t" \
    "3️⃣ - Buscar cliente\n\t\t\t\t" \
    "\U0001F6AA - Volver al menu principal")
    opcion=input("\t\t\t\tElige una opción (1-4): ").upper()
    return opcion

#Ventas
def menu_ventas():
    borrarPantalla()
    print("\n\t\t\t\t\U0001F50D...::: Ventas :::...\U0001F50D\n\t\t\t\t" \
    "1️⃣ - Realizar nueva venta\n\t\t\t\t" \
    "2️⃣- Consultar venta por ID\n\t\t\t\t" \
    "3️⃣ - Exportar ventas en excel\n\t\t\t\t" \
    "\U0001F6AA - Volver al menu principal")
    opcion=input("\t\t\t\tElige una opción (1-4): ").upper()
    return opcion

#Proveedores
def menu_proveedores():
    borrarPantalla()
    print("\n\t\t\t\t\U0001F464 ...::: Proveedores :::...\U0001F464\n\t\t\t\t" \
    "1️⃣ - Registrar proveedor\n\t\t\t\t" \
    "2️⃣ - Editar proveedor\n\t\t\t\t" \
    "3️⃣ - Buscar proveedor\n\t\t\t\t" \
    "\U0001F6AA - Volver al menu principal")
    opcion=input("\t\t\t\tElige una opción (1-4): ").upper()
    return opcion