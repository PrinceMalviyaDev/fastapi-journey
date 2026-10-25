# pip install requests

from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/posts")
def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    return response.json()

@app.get("/posts/{post_id}")
def get_post(post_id:int):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    return response.json()