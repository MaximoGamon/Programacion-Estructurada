import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_farmacia"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("ERROR, intentelo mas tarde...")
