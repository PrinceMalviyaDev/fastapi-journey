# Examples:
#  /users?name=mohit
#  /products?price=1000

# the things written after the question mark are handled using query parameters, they are key value pairs

# in ecommerce websites we apply filters through query params, in social media we search a useror id using query params


from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name: str = None):  # (optional parameter) handling no params in URl
    return {"Name" : name};

@app.get("/products")
def get_products(limit: int = 10):  # default parameter value
    return {"limit" : limit}

@app.get("/items")
def get_items(name: str = None, price: int = 0): # Multiple parameters
    return {
        "Name" : name,
        "Price" : price
    }