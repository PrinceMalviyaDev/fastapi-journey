from fastapi import FastAPI

app = FastAPI()

# Users Route
@app.get("/users/{user_id}")
def get_user(user_id:int):   # Automatic type validation by FastAPI
    return {"user_id": user_id}