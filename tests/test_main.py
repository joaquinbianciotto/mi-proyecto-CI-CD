from fastapi.testclient import TestClient
from app.main import app, edad

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Bienvenido a mi API con FastAPI!"}


def test_edad():
    respuesta = edad("24/10/2003")
    assert respuesta == 21