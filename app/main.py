from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from modules.database import SessionLocal
from modules import crud, models, schemas

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data/", response_model=list[schemas.DataScienceSalary])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_data(db, skip=skip, limit=limit)
    return users
