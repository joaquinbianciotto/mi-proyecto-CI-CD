from fastapi.testclient import TestClient
from app.main import app, edad
from datetime import date

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Bienvenido a mi API con FastAPI!"}


def test_edad():
    respuesta = edad(date(2003,10,24))
    assert respuesta == 21
