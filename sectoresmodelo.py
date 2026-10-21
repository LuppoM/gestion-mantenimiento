# sectoresmodelo.py
from conexion import obtener_conexion

def obtener_sectores():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, planta
        FROM sectores
        ORDER BY nombre
    """)
    filas = cursor.fetchall()
    cursor.close()
    conn.close()
    return filas

def agregar_sector(nombre: str, planta: str):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sectores (nombre, planta) VALUES (%s, %s)", (nombre, planta))
    conn.commit()
    cursor.close()
    conn.close()

def modificar_sector(id_sector: int, nombre: str, planta: str):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE sectores SET nombre = %s, planta = %s WHERE id = %s", (nombre, planta, id_sector))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_sector(id_sector: int):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sectores WHERE id = %s", (id_sector,))
    conn.commit()
    cursor.close()
    conn.close()