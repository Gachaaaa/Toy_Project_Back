from pydantic import BaseModel

class UserLogin(BaseModel):
    login_id: str
    password: str
