import os
import sys
import psycopg2
import psycopg2.extras

# URL de conexión a la base de datos MANTENIMIENTODB en Neon
# Puedes setearla mediante la variable de entorno DATABASE_URL en Render/Vercel/Local
DATABASE_URL_DEFAULT = "postgresql://usuario:password@ep-xyz.us-east-1.aws.neon.tech/MANTENIMIENTODB?sslmode=require"

def obtener_conexion():
    """Establece y devuelve una conexión a la base de datos MANTENIMIENTODB en Neon.
    
    Retorna los resultados como diccionarios (RealDictCursor) para un manejo ágil en FastAPI.
    """
    database_url = os.environ.get("DATABASE_URL", DATABASE_URL_DEFAULT)
    
    conexion = psycopg2.connect(
        database_url,
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    return conexion

def obtener_ruta_icono(nombre_icono="icono.ico"):
    """Devuelve la ruta absoluta del ícono tanto en desarrollo como empaquetado en executable."""
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, nombre_icono)