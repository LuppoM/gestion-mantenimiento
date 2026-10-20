# apimantenimiento.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Importar la conexión a la base de datos de Neon
from conexion import obtener_conexion

app = FastAPI(title="Sistema de Gestión de Mantenimiento")

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Montar archivos estáticos (CSS, íconos, imágenes como fondo.jpg e iconom.ico)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configurar carpeta de plantillas HTML
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# --- RUTAS DE NAVEGACIÓN Y VISTAS ---

@app.get("/", response_class=HTMLResponse)
def leer_inicio(request: Request):
    """Renderiza la pantalla principal del sistema."""
    return templates.TemplateResponse(request, "principal.html", {})

@app.get("/ot", response_class=HTMLResponse)
def vista_ordenes_trabajo(request: Request):
    """Vista para Órdenes de Trabajo."""
    # Aquí puedes retornar una plantilla específica o un mensaje temporal
    return HTMLResponse("<h1>Módulo de Órdenes de Trabajo en construcción</h1>")

@app.get("/tareas", response_class=HTMLResponse)
def vista_tareas(request: Request):
    """Vista para Tareas de fin de semana."""
    return HTMLResponse("<h1>Módulo de Tareas de fin de semana en construcción</h1>")

@app.get("/parte-diario", response_class=HTMLResponse)
def vista_parte_diario(request: Request):
    """Vista para Parte Diario."""
    return HTMLResponse("<h1>Módulo de Parte Diario en construcción</h1>")

@app.get("/notas-pedido", response_class=HTMLResponse)
def vista_notas_pedido(request: Request):
    """Vista para Notas de Pedido."""
    return HTMLResponse("<h1>Módulo de Notas de Pedido en construcción</h1>")

@app.get("/mecanicos", response_class=HTMLResponse)
def vista_mecanicos(request: Request):
    """Parámetro: Mecánicos."""
    return HTMLResponse("<h1>Módulo de Mecánicos en construcción</h1>")

@app.get("/sectores", response_class=HTMLResponse)
def vista_sectores(request: Request):
    """Parámetro: Sectores."""
    return HTMLResponse("<h1>Módulo de Sectores en construcción</h1>")

@app.get("/plantas", response_class=HTMLResponse)
def vista_plantas(request: Request):
    """Parámetro: Plantas."""
    return HTMLResponse("<h1>Módulo de Plantas en construcción</h1>")

@app.get("/salir")
def salir_sistema():
    """Redirige al inicio o cierra sesión."""
    return RedirectResponse(url="/", status_code=303)

# --- RUTA DE PRUEBA DE CONEXIÓN A NEON ---
@app.get("/test-db")
def probar_conexion():
    """Verifica que la conexión con la base de datos de Neon responda correctamente."""
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"estado": "Conexión exitosa a Neon", "version_db": version[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con la base de datos: {str(e)}")