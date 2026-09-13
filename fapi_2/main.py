# Multiple routes

from fastapi import FastAPI

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message" : "Welcome to FastAPI"}

# About Route
@app.get("/about")
def about():
    return {"message" : "Welcome to about page"}

# Users Route
@app.get("/users")
def users():
    return {"users" : ["Prince", "Srishti", "Tinku"]}