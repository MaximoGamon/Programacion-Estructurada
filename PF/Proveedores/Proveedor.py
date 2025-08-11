from conexionDB import * 
from funciones import *

def consultar_Provededores():
    try:
        sql="SELECT * FROM proveedores "
        cursor.execute(sql,)
        return cursor.fetchall()
    except:
        return [] 

def registrarProveedor(proveedor,direccion,email,telefono):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO proveedores (provedor, direccion, email, telefono) VALUES (%s, %s, %s, %s)"
        valores = (proveedor,direccion,email,telefono)
        cursor.execute(sql, valores)
        conexion.commit()
        print("✅ Proveedor registrado con éxito.")
        return True
    except Exception as e:
        print("❌ No se pudo Realizar la venta intentelo mas tarde:", e)
        return False

def editarProvedores(contactos):
    borrarPantalla()
    print("\n\t .::🔁 Editar Proveedor 🔁::. \n")
    print(f"{'-'*40}")
    if len(contactos) > 0:
        for proveedor in contactos:
            print(f"\nDatos actuales del proveedor:")
            for clave, valor in proveedor.items():
                print(f"{clave}: {valor}")

            resp = input("\n¿Deseas editar este proveedor? (si/no): ").lower().strip()
            while resp !="si" and resp != "no":
                resp = input("\n¿Deseas editar este proveedor? (si/no): ").lower().strip()
            if resp == "si":
                for clave in proveedor:
                    nuevo = input(f"¿Deseas cambiar '{clave}'? Valor actual: '{proveedor[clave]}' (si/no): ").lower().strip()
                    while nuevo != "si" and nuevo!= "no":
                        nuevo = input(f"¿Deseas cambiar '{clave}'? Valor actual: '{proveedor[clave]}' (si/no): ").lower().strip()
                    if nuevo == "si":
                        proveedor[clave] = input(f"Ingrese nuevo valor para '{clave}': ").upper().strip()
                print("\n\t\t ✅ ¡Edición completada con éxito! ✅")
                esperarTecla()
                borrarPantalla()
            else:
                continue
    else:
        print("\n\t ⚠️ No hay proveedores registrados para editar.")
        esperarTecla()

def modificar(id,nom,direccion,email,telefono):
    try:
        cursor.execute("UPDATE proveedores SET provedor=%s,direccion=%s,email=%s,telefono=%s WHERE id_provedores=%s",(nom,direccion,email,telefono,id))
        conexion.commit()
        return True
    except:
        return False
   

def buscarProveedor(provedores):
    try:
        sql="SELECT * FROM proveedores WHERE provedor = %s"
        val=(provedores,)
        cursor.execute(sql,val)
        return cursor.fetchall()
    except:
        return []
    
   
    
