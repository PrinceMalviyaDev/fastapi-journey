from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title:str
    completed:bool

# POST - create a todo
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message": "ToDo added",
        "data": todo
    }

# GET all todos
@app.get("/todos")
def get_todos():
    return todos

# GET individual todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id :
            return todo
    return {
        "error" : "No matching todo."
    }

# PUT - update the todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id :
            todos[index] = updated_todo
            return {
                "message" : "successfully updated",
                "data" : updated_todo
            }
    return {
        "error" : "todo not found"
    }

# DELETE - delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {
                "message" : "record deleted successfully"
            }
    return {
        "error":"todo not found"
    }