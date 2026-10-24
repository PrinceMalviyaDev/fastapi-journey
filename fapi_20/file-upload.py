from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil  # Built-in module for file and folder operations, provides utilities for copying and managing files

app = FastAPI()

# Step-1: Ensure upload folder exists

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


# We are making a public path for the upload file so that we can give it to frontend

# Step-2: Static file setup
# URL: http://127.o.o.1:8080/files/<filename>
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


# Step-3: Creating upload file API
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(status = 400, detail = "file not selected")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message" : "Uploaded successfully",
        "filename" : filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# Step-4: Get file API

@app.get("/files/{filename}")
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return{
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return {
        "message": "File uploaded api running"
    }