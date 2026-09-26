from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()
DATABASE_URL = "sqlite:///./practice.db"

engine = create_engine(
    DATABASE_URL,
    connect_args = { "check_same_thread": False } 
)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default = False)

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db : Session = Depends(get_db)):
    return {
        "message" : "Database connected successfully"
    }