# path + query + body
# path = identify the resource
# query = filtering
# Body = sending data to the users
 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example:
# PUT /users/101?notify=true
# {
#     "name" : "Srishti",
#     "age" : 19
# }


users = []

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message" : "user created",
        "data" : user
    }

@app.put("/users/{user_id}")
def update_user(user_id:int, user:User, notify: bool = False):
    if user_id < len(users):
        users[user_id] = user
        return {
            "message" : "User updated",
            "notify" : notify,
            "data" : user
        }
    return{
        "error" : "not found"
    }