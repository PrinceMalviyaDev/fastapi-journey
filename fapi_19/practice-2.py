# pip install python-jose "passlib[bcrypt]" python-multipart

from fastapi import FastAPI, Depends, HTTPException
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext

app = FastAPI()

# JWT Config
SECRET_KEY = "mysecret"
ACCESS_TOKEN_EXPIRY_MINUTES = 30
ALGORITHM = "HS256"

# Password Hashing Setup
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# OAuth Setup
oauth2_schema = OAuth2PasswordBearer(tokenUrl = "login")

# Dummy User DB
fake_user_db = {
    "admin" : {
        "username" : "admin",
        "password" : pwd_context.hash("1234")
    }
}

# Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes = 30)
    to_encode.update({"exp": expiry})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return token

# Login API(OAuth2 Form)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code = 400,
            detail = "Invalid Username or Password"
        )

    access_token = create_token({"sub": form_data.username})

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

# Verify Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = ["ALGORITHM"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code = 401,
                detail = "Invalid Token"
            )
        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

# Protected Route
@app.get("protected")
def protected_route(username:str = Depends(verify_token)):
    return {
        "message" : "You have accessed a protected resource",
        "data" : username
    }