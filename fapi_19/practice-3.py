from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext

app = FastAPI()

# JWT Configuration
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30

# Password Hashing Setup
pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# OAuth2 Setup
oauth2_schema = OAuth2PasswordBearer(tokenUrl = "login")

# Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Fake User DB
fake_user_db = {
    "admin" : {
        "username" : "admin",
        "password" : pwd_context.hash("1234")
    }
}

# Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRY_MINUTES)
    to_encode.update({
        "exp": expiry
    })

    token = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return token

# Login API (OAuth2 Form)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or verify_password(form_data.password, user["password"]):
        raise HTTPException (
            status_code = 400,
            detail = "Invalid Username or Password"
        )

    token = create_token({"sub": user})

    return {
        "access_token" : token,
        "token_type" : "bearer"
    }

# Verify Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        username = payload.username
        if username is None:
            raise HTTPException (
                status_code = 401,
                detail = "Invalid Token"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid Token"
        )

# Protected Route
@app.get("/protected")
def protected(username: str = Depends(verify_token)):
    return {
        "message" : "Protected route accessed"
    }