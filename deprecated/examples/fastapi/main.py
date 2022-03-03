from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {"name": "Milk",
       "price": 30},
    2: {"name": "bread",
        "price": 45}
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/about")
def about():
    return {"Message": "This is an Api"}