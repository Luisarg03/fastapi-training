from fastapi import APIRouter, Depends
from modules import crud, schemas
from modules.conf import cursor_confs, get_db
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate

CursorPage = cursor_confs()
router = APIRouter()


@router.get("/getdata/datascience/", response_model=CursorPage[schemas.DataScienceSalary])
def read_data_science(db: Session = Depends(get_db)) -> CursorPage[schemas.DataScienceSalary]:
    query = crud.get_data_data_science(db)
    return paginate(query)
