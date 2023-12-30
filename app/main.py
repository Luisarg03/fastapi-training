from fastapi import FastAPI
from fastapi_pagination import add_pagination
from modules.routers import root, pokemon, datascience

app = FastAPI()

routers = [
    pokemon.router,
    datascience.router,
    root.router
]

for router in routers:
    app.include_router(router)

add_pagination(app)
