# pip install fastapi uvicorn python-dotenv
# pip freeze > requirements.txt

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI"
    }