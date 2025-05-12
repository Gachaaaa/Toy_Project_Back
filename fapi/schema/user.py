from pydantic import BaseModel

class UserLogin(BaseModel):
    login_id: str
    password: str

class UserToken(BaseModel):
    user_id: int
    login_id: str