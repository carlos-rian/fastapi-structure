from fastapi import FastAPI
from typing.get import UserType, ItemType
from models.models import User, Item
import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/user/{id_user}")
async def read_root(id_user: int = None) -> UserType:
    if not id_user:
        query = User.select().where(User.id == id_user)
    else:
        query = Item.select()
    result = await database.fetch_all(query)
    return {"result": result}


@app.get("/items/{item_id}")
async def read_item(item_id: int = None) -> ItemType:
    if not item_id:
        query = Item.select().where(Item.id == item_id)
    else:
        query = Item.select()
    result = await database.fetch_all(query)
    return {"result": result}