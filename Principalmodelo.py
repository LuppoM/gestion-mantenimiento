import os
from datetime import datetime
from conexion import obtener_conexion

def realizar_backup():
    """
    Nota: En bases de datos en la nube como Neon (PostgreSQL), los respaldos 
    se gestionan de forma nativa en el servidor. Esta función se mantiene 
    para no romper la compatibilidad con el controlador, informando que el 
    sistema está conectado a la nube.
    """
    try:
        # Verificamos que la conexión se pueda establecer correctamente
        conn = obtener_conexion()
        if conn:
            conn.close()
            return True, "Base de datos en la nube (Neon) activa. Los respaldos son administrados por el servidor."
        return False, "No se pudo establecer conexión con Neon."
    except Exception as e:
        return False, str(e)