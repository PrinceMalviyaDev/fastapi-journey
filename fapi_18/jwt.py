# pip install python-jose
# jose - JavaScript Object Signature and Encryption

from fastapi import FastAPI, Depends, HTTPException, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"  #basic algorithm

# Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = 30)
    to_encode.update({
        "exp": expire
    })
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token

# Login API(Token Generation)
@app.post("/login")
def login(username:str, password:str):
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Username or Password"
        )
    token = create_token({
        "sub":username
    })
    return {
        "access_token": token
    }

# Token Verify
def verify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except: 
        raise HTTPException(
            status_code = 401,
            detail = "Invalid or Expired Token"
        )

# Protected Route
@app.get("/secured")
def secure_data(user = Depends(verify_token)):
    return {
        "message": "Secure data accessed",
        "user" : user
    }
