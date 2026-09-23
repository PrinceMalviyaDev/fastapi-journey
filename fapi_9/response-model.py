from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class UserResponse(BaseModel):
    name: str
    age: int

@app.get("/user", response_model = UserResponse)
def get_user():
    return {
        "name" : "Prince",
        "age" : "24y",   #internal server error due to type mismatch
        # "age" : 22,
        "password" : "123456"
    }