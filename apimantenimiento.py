from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# Importar el router de Mantenimiento
from ot_router import router as ot_router

app = FastAPI(title="Sistema de Gestión de Mantenimiento")

# Directorio base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Montar archivos estáticos (CSS, Imágenes, Íconos)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configurar carpeta de plantillas HTML
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Registrar el Router de Órdenes de Trabajo (API)
app.include_router(ot_router)

# Ruta principal para renderizar la pantalla de inicio
@app.get("/", response_class=HTMLResponse)
def leer_inicio(request: Request):
    return templates.TemplateResponse("principal.html", {"request": request})