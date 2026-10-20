import os
import psycopg2
from psycopg2.extras import RealDictCursor

# URL de conexión de Neon (lee la variable de entorno o usa la cadena por defecto)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_AH8J5qmRYDXZ@ep-raspy-leaf-b4r6bylb-pooler.c-6.us-east-2.aws.neon.tech/MANTENIMIENTODB?sslmode=require&channel_binding=require"  # Reemplazá con tu cadena de conexión si es necesario
)

def obtener_conexion():
    """Establece y devuelve una conexión a la base de datos PostgreSQL en Neon."""
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        return conexion
    except Exception as e:
        print(f"Error al conectar con la base de datos en Neon: {e}")
        raise e