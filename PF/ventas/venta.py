from conexionDB import * 

def consultar():
    try:
        sql="SELECT * FROM ventas "
        cursor.execute(sql,)
        columns = [desc[0] for desc in cursor.description]
        return cursor.fetchall(),columns
    except:
        return [] 

def venta_Nueva(cliente,producto,precio,cantidad,total,id_medicamento):
    if conexion is None:
        return
    try:
        # Insertar la nueva venta si ya hay registros
        sql = "INSERT INTO ventas (cliente,producto,precio,cantidad,total,id_medicamento) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (cliente,producto,precio,cantidad,total,id_medicamento)
        cursor.execute(sql, valores)
        conexion.commit()
        print("✅ Medicamento registrado con éxito.")
        inserted_id = cursor.lastrowid
        return True,inserted_id
    except Exception as e:
        print("❌ No se pudo Realizar la venta intentelo mas tarde:", e)
        return False


def consultarVenta(id_ventas):
    try:
        sql="SELECT * FROM ventas WHERE id_ventas = %s"
        val=(id_ventas,)
        cursor.execute(sql,val)
        return cursor.fetchall()
    except:
        return []
     


    

