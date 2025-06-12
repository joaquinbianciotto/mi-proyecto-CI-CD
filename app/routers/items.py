from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "No encontrado"}}
)

# Modelo de datos
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None


# Base de datos simulada
items_db = {
    1: Item(id=1, name="Martillo", description="Herramienta para clavar mucho", price=19.99, is_offer=True),
    2: Item(id=2, name="Destornillador", description="Herramienta para tornillos", price=9.99, is_offer=False)
}

@router.get("/", response_model=List[Item])
async def read_items():
    return list(items_db.values())

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return items_db[item_id]

@router.post("/", response_model=Item)
async def create_item(item: Item):
    if item.id in items_db:
        raise HTTPException(status_code=400, detail=f"El item con id {item.id} ya existe")
    items_db[item.id] = item
    return item

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    if item_id != item.id:
        raise HTTPException(status_code=400, detail="El ID en el path debe coincidir con el ID del item")
    items_db[item_id] = item
    return item

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    del items_db[item_id]
    return {"message": f"Item con id {item_id} eliminado correctamente"}
