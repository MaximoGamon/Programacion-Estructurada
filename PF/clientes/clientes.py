from conexionDB import *

def consultar():
    try:
        sql="SELECT * FROM clientes"
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        return []
    
def agregar(nombre,alergias,telefono):
    try:
        sql="INSERT INTO clientes (usuario,alergias,telefono) VALUES (%s,%s,%s)"
        val=(nombre,alergias,telefono)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False

def modificar(id,nom,alergias,telefono):
    try:
        cursor.execute("UPDATE clientes SET usuario=%s,alergias=%s,telefono=%s WHERE id_usuario=%s",(nom,alergias,telefono,id))
        conexion.commit()
        return True
    except:
        return False