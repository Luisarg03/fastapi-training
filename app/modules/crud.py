from sqlalchemy.orm import Session
from . import models


def get_data_data_science(db: Session):
    return db.query(models.DataScienceSalary).order_by(models.DataScienceSalary.row_id)


def get_data_pokemon(db: Session):
    return db.query(models.PokemonDataMaster).order_by(models.PokemonDataMaster.row_id)
