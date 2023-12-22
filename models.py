from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.orm.base import Mapped

metadata = MetaData()


t_data_sciences_salaries = Table(
    'data_sciences_salaries', metadata,
    Column('work_year', Integer),
    Column('experience_level', String),
    Column('employment_type', String),
    Column('job_title', String),
    Column('salary', Integer),
    Column('salary_currency', String),
    Column('salary_in_usd', Integer),
    Column('employee_residence', String),
    Column('remote_ratio', Integer),
    Column('company_location', String),
    Column('company_size', String)
)
