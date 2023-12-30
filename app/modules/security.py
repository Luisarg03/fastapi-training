from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/test/")
# async def read_test(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}