from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
    # Verificar que los items predefinidos existen
    item_ids = [item["id"] for item in data]
    assert 1 in item_ids
    assert 2 in item_ids

def test_read_item():
    # Probar obteniendo un item existente
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Martillo"
    
    # Probar obteniendo un item que no existe
    response = client.get("/items/999")
    assert response.status_code == 404

def test_create_item():
    # Crear un nuevo item
    new_item = {
        "id": 3,
        "name": "Llave inglesa",
        "description": "Herramienta ajustable",
        "price": 14.99,
        "is_offer": True
    }
    response = client.post("/items/", json=new_item)
    assert response.status_code == 200
    data = response.json()
    assert data == new_item
    
    # Intentar crear un item con un ID que ya existe
    response = client.post("/items/", json=new_item)
    assert response.status_code == 400

def test_update_item():
    # Actualizar un item existente
    updated_item = {
        "id": 2,
        "name": "Destornillador Phillips",
        "description": "Destornillador de cruz",
        "price": 12.99,
        "is_offer": True
    }
    response = client.put("/items/2", json=updated_item)
    assert response.status_code == 200
    data = response.json()
    assert data == updated_item
    
    # Intentar actualizar un item que no existe
    non_existent_item = {
        "id": 999,
        "name": "No existe",
        "description": "Este item no existe",
        "price": 0,
        "is_offer": False
    }
    response = client.put("/items/999", json=non_existent_item)
    assert response.status_code == 404
    
    # ID no coincidente
    mismatched_item = {
        "id": 5,  # ID diferente al de la ruta
        "name": "ID no coincidente",
        "description": "Este item tiene un ID que no coincide con la ruta",
        "price": 0,
        "is_offer": False
    }
    response = client.put("/items/2", json=mismatched_item)
    assert response.status_code == 400

def test_delete_item():
    # Eliminar un item existente
    # Primero crear un item para eliminar
    new_item = {
        "id": 4,
        "name": "Temporal",
        "description": "Item para eliminar",
        "price": 5.99,
        "is_offer": False
    }
    client.post("/items/", json=new_item)
    
    # Ahora eliminar el item
    response = client.delete("/items/4")
    assert response.status_code == 200
    
    # Verificar que se eliminó
    response = client.get("/items/4")
    assert response.status_code == 404
    
    # Intentar eliminar un item que no existe
    response = client.delete("/items/999")
    assert response.status_code == 404
