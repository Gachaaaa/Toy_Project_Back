from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from model import pgsql_user
from schema.user import UserLogin, UserToken
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

SECRET_KEY = "your-secret"  # 반드시 실제 배포 시 강한 키로 설정
ALGORITHM = "HS256"

class UserCreate(BaseModel):
    login_id: str
    password: str
    phone_number: str
    name: str
    email: str

@router.post("/signup")
def signup_user(user: UserCreate):
    created_user = pgsql_user.insert_user(user)
    if not created_user:
        raise HTTPException(status_code=400, detail="User creation failed")
    return {"message": "User created successfully", "user": created_user}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = pgsql_user.verify_user_login(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "user_id": user["user_id"],
        "login_id": user["login_id"]
    }
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
