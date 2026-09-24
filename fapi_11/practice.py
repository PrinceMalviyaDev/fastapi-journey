from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content = {
            "status" : "error",
            "message" : f"user {exc.name} not found"
        }
    )

@app.get("/user/{user_name}")
def get_user(user_name:str):
    if user_name != "prince":
        raise UserNotFoundException(user_name)
    return {
        "name" : user_name
    }