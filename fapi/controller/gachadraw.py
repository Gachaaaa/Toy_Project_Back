from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from model import pgsql_gachadraw
from schema.user import UserToken
from utils.auth import get_current_user

router = APIRouter(
    prefix="/gachadraw",
    tags=["gachadraw"],
    responses={404: {"description": "Not found"}},
)

class GachaDrawRequest(BaseModel):
    gacha_id: int

@router.post("/")
def draw_gacha(
    request: GachaDrawRequest,
    current_user: UserToken = Depends(get_current_user)
):
    result = pgsql_gachadraw.draw_gacha(
        gacha_id=request.gacha_id,
        user_id=current_user.user_id
    )
    if not result:
        raise HTTPException(status_code=400, detail="아이템이 없거나 뽑기 실패")
    
    return {
        "message": "가챠 성공",
        "draw_id": result["draw_id"],
        "item": result["item"]
    }
