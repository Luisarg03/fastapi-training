from fastapi import FastAPI, Depends, Query
from fastapi_pagination import add_pagination
from fastapi_pagination.cursor import CursorPage
from fastapi_pagination.ext.sqlalchemy import paginate

from sqlalchemy.orm import Session
from modules.database import SessionLocal
from modules import crud, schemas


CursorPage = CursorPage.with_custom_options(
    size=Query(5),
)

app = FastAPI()
add_pagination(app)


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


@app.get("/getdata/datascience/", response_model=CursorPage[schemas.DataScienceSalary])
def read_data_science(db: Session = Depends(get_db)) -> CursorPage[schemas.DataScienceSalary]:
    query = crud.get_data_data_science(db)
    return paginate(query)


@app.get("/getdata/pokemon/", response_model=CursorPage[schemas.PokemonDataMaster])
def read_pokemon(db: Session = Depends(get_db)) -> CursorPage[schemas.PokemonDataMaster]:
    query = crud.get_data_pokemon(db)
    return paginate(query)
