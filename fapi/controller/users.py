from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model import pgsql_user
from schema.user import UserLogin

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not founc"}},
)

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
def login_user(user: UserLogin):
    login_result = pgsql_user.verify_user_login(user.login_id, user.password)
    if not login_result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user": login_result}
