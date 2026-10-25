# pip install python dotenv   // For loading environment variables from a .env file

'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

origins = os.getenv("CORS_ORIGINS", "").split(",")  
SECRET_KEY = os.getenv("SECRET_KEY")  
DB_URL = os.getenv("DB_URL")  

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def home():
    return {"message": "CORS ENABLED FastAPI application is running!"}

'''