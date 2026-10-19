import conexion

def ejecutar_consulta(query: str, parametros: tuple = ()):
    """
    Ejecuta una consulta SQL de lectura en PostgreSQL (Neon) y retorna los resultados.
    """
    conn = None
    try:
        conn = conexion.obtener_conexion()
        with conn.cursor() as cursor:
            cursor.execute(query, parametros)
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Error al ejecutar consulta en la BD: {e}")
        return []
    finally:
        if conn:
            conn.close()

def ejecutar_comando(query: str, parametros: tuple = ()):
    """
    Ejecuta un comando SQL de modificación (INSERT, UPDATE, DELETE) en PostgreSQL (Neon).
    """
    conn = None
    try:
        conn = conexion.obtener_conexion()
        with conn.cursor() as cursor:
            cursor.execute(query, parametros)
            conn.commit()
            return True, "Operación realizada con éxito."
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error al ejecutar comando en la BD: {e}")
        return False, str(e)
    finally:
        if conn:
            conn.close()