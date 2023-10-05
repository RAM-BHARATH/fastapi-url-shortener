import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import motor.motor_asyncio

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI"])
db = client.college

class Item(BaseModel):
    key: str
    long_url: str 
    short_url: str

@app.get("/items")
async def read_item(request: Request) -> list[Item]:
    return [
        Item(key="aa", long_url='http://', short_url=str(request.url)+"/aa")
    ]

@app.get("/items/{item_id}")
async def read_item(item_id: str, request: Request) -> Item:
    return [
        Item(key="aa", long_url='http://', short_url=str(request.url)+key)
    ]

@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item