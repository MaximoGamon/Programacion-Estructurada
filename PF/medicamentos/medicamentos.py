from conexionDB import *
from mysql.connector import Error

def agregar(nombre,desc,precio,mg,inventario):
    try:
        sql="INSERT INTO medicamentos (nombre,descripcion,precio,miligramos,inventario) VALUES (%s,%s,%s,%s,%s)"
        val=(nombre,desc,precio,mg,inventario)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False

def consultar():
    try:
        sql="SELECT * FROM medicamentos"
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        return []
    
def modificar(id,nombre,descripcion,precio,miligramos,inventario):
    try:
        cursor.execute("UPDATE medicamentos SET nombre=%s,descripcion=%s,precio=%s,miligramos=%s,inventario=%s WHERE id=%s",(nombre,descripcion,precio,miligramos,inventario,id))
        conexion.commit()
        return True
    except:
        return False

def eliminar(id):
    try:
        cursor.execute("DELETE FROM medicamentos WHERE id=%s",(id,))
        conexion.commit()
        return True
    except Error as e:
        print(e)
        return False

def exportar():
    try:
        sql="SELECT * FROM medicamentos"
        cursor.execute(sql,)
        columns = [desc[0] for desc in cursor.description]
        return cursor.fetchall(),columns
    except:
        return [] 