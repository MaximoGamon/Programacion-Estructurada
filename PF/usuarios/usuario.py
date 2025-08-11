from conexionDB import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def comprobar(email):
    try:
        sql="SELECT * FROM usuarios WHERE email=%s"
        val=(email,)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        return None


def registrar(nombre,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="INSERT INTO usuarios (nombre_de_usuario,email,password,fecha) VALUES (%s,%s,%s,%s)"
        val=(nombre,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False

def iniciar_sesion(email,contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="SELECT * FROM usuarios WHERE email=%s and password=%s"
        val=(email,contrasena)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        return None