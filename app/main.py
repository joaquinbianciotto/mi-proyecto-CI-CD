from fastapi import FastAPI
from app.routers import items
from datetime import date
from dateutil.relativedelta import relativedelta

app = FastAPI(
    title="Mi Proyecto CI/CD",
    description="API de ejemplo con FastAPI y pruebas",
    version="0.1.0"
)

app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "¡Bienvenido a mi API con FastAPI!"}

def edad(fecha_nacimiento):
    return 21