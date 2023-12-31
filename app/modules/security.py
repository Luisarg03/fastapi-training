import hashlib
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .routers.conf import cursor_confs, get_db
from . import crud, schemas


SALT = "4854e434b9cab3ee2e3db738616d59251b70"
ROUNDS = 15
SECRET_KEY = "una_llave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

CursorPage = cursor_confs()
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(stored_password_hash, provided_password, salt, rounds):
    hashed_provided_password = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt.encode('utf-8'),
        rounds
    )

    return hashed_provided_password.hex() == stored_password_hash


def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_user_api(db, username)
    if not user:
        return False
    if not verify_password(user.password, password, SALT, ROUNDS):
        return False
    return user


def create_access_token(data: dict, token_expire_minutes: int):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid username")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username}, token_expire_minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {"access_token": access_token, "token_type": "bearer"}


# @router.get("/user/me")
# def read_users_me(current_user: str = Depends(get_current_user)):
#     return {"username": current_user}
