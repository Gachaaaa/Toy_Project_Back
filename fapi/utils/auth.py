# 📄 utils/auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from schema.user import UserToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

SECRET_KEY = "your-secret"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserToken:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        login_id: str = payload.get("login_id")
        if user_id is None or login_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return UserToken(user_id=user_id, login_id=login_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token decode error")
