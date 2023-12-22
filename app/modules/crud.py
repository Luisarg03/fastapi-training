from sqlalchemy.orm import Session
from . import models, schemas


def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.t_data_sciences_salaries).offset(skip).limit(limit).all()
