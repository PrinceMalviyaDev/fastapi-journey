from fastapi import FastAPI, Depends, HTTPException, Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

# Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes = 30)
    to_encode.update({
        "exp": expiry
    })
    token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return token

# Login API
@app.post("/login")
def login(user_name:str, password:str):
    if user_name != "admin" or password != "1234":
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Username or Password"
        )
    token = create_token({
        "sub": user_name
    })

    return {
        "access_token" : token
    }

# Token Verify
def verify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid or exspired Token"
        )

@app.get("/secured")
def secured(user = Depends(verify_token)):
    return {
        "message" : "secured data accesssed",
        "user" : user
    }