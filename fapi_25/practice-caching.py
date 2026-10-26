from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import time

app = FastAPI()

# Cache Storage
cached_data = []
last_fetch_time = 0

@app.get("/news")
def get_news():
    global last_fetch_time, cached_data
    url = "https://news.ycombinator.com/"

    start = time.time()

    if time.time() - last_fetch_time > 60:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.find_all("span", class_="titleline"):
            cached_data.append(item.text)

        last_fetch_time = time.time()

    end = time.time()

    time_taken = round((end - start), 4)

    return {
        "time_taken": time_taken,
        "data": cached_data[:5]
    } 