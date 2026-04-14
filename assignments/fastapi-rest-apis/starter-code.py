from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    name: str
    description: str
    price: float


items = {
    1: {"name": "Notebook", "description": "Caderno de estudos", "price": 19.9},
    2: {"name": "Mouse", "description": "Mouse sem fio", "price": 89.9},
}


@app.get("/")
def read_root():
    return {"message": "API online"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(item: Item):
    new_id = max(items.keys(), default=0) + 1
    items[new_id] = item.model_dump()
    return {"id": new_id, **items[new_id]}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.model_dump()
    return {"id": item_id, **items[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"message": "Item removed", "item": deleted_item}
