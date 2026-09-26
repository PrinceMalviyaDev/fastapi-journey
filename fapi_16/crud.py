from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    completed = Column(Boolean, default = False)

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
    todo = ToDo(title = title, completed = False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo Created",
        "data": todo
    }

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(ToDo).all()
    return {
        "total": len(todos),
        "data": todos
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code = 404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title:str, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code = 404, detail= "Todo not found")
    
    todo.title = title

    db.commit()
    db.refresh(todo)

    return {
        "message": "Todo updated",
        "data": todo
    }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code = 404, detail= "Todo not found")

    db.delete(todo)
    db.commit()
    
    return {
        "message" : "Todo Deleted"
    }
