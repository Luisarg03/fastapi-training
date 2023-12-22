from pydantic import BaseModel


# Esquema para la lectura de datos (por ejemplo, para respuestas de la API)
class DataScienceSalary(BaseModel):
    work_year: int
    experience_level: str
    employment_type: str
    job_title: str
    salary: int
    salary_currency: str
    salary_in_usd: int
    employee_residence: str
    remote_ratio: int
    company_location: str
    company_size: str

    class Config:
        orm_mode = True
