# Request body : The data that is sent by the client to the server or backend

# Example : The user fills the signup form and the data goes to the backend or server

# This data is sent mostly using JSON body

# POST Request: http method for sending the data to server mostly used to create the data.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/create-user")
def create_user(name: str, age: int):
    return {
        "name" : name,
        "age" : age
    }

class Product(BaseModel):  # solving validation problem with pydantic
    name : str
    price : int

# real world example
@app.post("/create-item")
def create_item(item:Product):
    return {
        "message": "Item Added to the Inventory",
        "item" : item
    }
