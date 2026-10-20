import os
import psycopg2
from psycopg2.extras import RealDictCursor

# URL de conexión de Neon (lee la variable de entorno o usa la cadena por defecto)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "TU_URL_DE_NEON_AQUI"  # Reemplazá con tu cadena de conexión si es necesario
)

def obtener_conexion():
    """Establece y devuelve una conexión a la base de datos PostgreSQL en Neon."""
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        return conexion
    except Exception as e:
        print(f"Error al conectar con la base de datos en Neon: {e}")
        raise e