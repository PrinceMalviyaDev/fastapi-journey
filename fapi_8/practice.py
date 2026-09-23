from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name : str
    age : int

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {
        "message" : "User created successfully"
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User, notify: bool = False):
    if user_id < len(users):
        users[user_id] = updated_user
        return {
            "message" : "User updated successfully",
            "data" : updated_user,
            "notify" : notify
        }
    return {
        "message" : "Error ocurred"
    }

@app.get("/users")
def get_users():
    return {
        "Users" : users
    }