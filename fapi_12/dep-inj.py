from fastapi import FastAPI, Depends

app = FastAPI()

# def common_logic():
#     return {
#         "message" : "Common Logic executed"
#     }

# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data

def get_current_user():
    return {
        "user" : "guest"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user