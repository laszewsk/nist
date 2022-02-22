from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {}


@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return {"This": "is Amaan's Api"}


@app.get("/inv/{item_id}")
def about(item_id: int = Path(None, description="ID of the item you want to view", gt=0, )):
    return inventory[item_id]


@app.get("/get-name")
def find(*, example: Optional[str] = None, title: str):
    for item_id in inventory:

        # if inventory[item_id]["name"] == title:
        # another way of writing this is (since we converted item into object now)
        if inventory[item_id].name == title:
            return inventory[item_id], {"": ""}, {"You did a search via": "NAME"}
        raise HTTPException(status_code=404, detail="Item name does not exist")

        # The code below is only for my understanding
        # if inventory[item_id]["brand"] == title:
        #     return inventory[item_id], {"":""}, {"You did a search via": "BRAND" }


@app.post("/create-item/{item_id}")
def create(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID is already taken")
    # inventory[item_id] = {"name" : Item.name, "price" : Item.price, "brand" : Item.brand}
    # shorter way of doing the upper step
    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    if item.name is not None:
        inventory[item_id].name = item.name

    if item.price is not None:
        inventory[item_id].price = item.price

    if item.brand is not None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="Id of the item you wanna delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")

    del inventory[item_id]
    return {"Success": "Item deleted"}
