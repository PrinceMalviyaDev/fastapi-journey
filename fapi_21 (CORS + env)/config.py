import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",")  
    SECRET_KEY = os.getenv("SECRET_KEY")  
    DB_URL = os.getenv("DB_URL")

settings = Settings()