from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
import os, shutil

app = FastAPI()


# Step-1: Creating Uploads Directory

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


# Step-2: Mounting the files application / Static file setup / creating a public url

app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


# Step-3: Create a Post API for file upload

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(
            status_code=400,
            detail="file not selected"
        )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# Step-4: Get API

@app.get("/files/{filename}")
def get_file(filename:str):
    if not os.path.exists(filename):
        raise HTTPException (
            status_code=404,
            detail="file not found"
        )
    
    return {
        "file_url" : f"http://127.0.0.1:8000/files/{filename}"
    }


@app.get("/")
def home():
    return {
        "message" : "APIs working fine"
    }