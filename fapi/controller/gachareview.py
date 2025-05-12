from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from model import pgsql_gachareview
from schema.user import UserToken
from utils.auth import get_current_user  # JWT 인증함수

router = APIRouter(
    prefix="/gachareview",
    tags=["gachareview"],
    responses={404: {"description": "Not found"}},
)

class GachaReviewCreate(BaseModel):
    gacha_id: int
    review: str

@router.post("/")
def post_review(
    review: GachaReviewCreate,
    current_user: UserToken = Depends(get_current_user)  # ✅ 로그인 유저만 가능
):
    result = pgsql_gachareview.insert_review(
        gacha_id=review.gacha_id,
        user_id=current_user.user_id,
        review_text=review.review
    )
    if not result:
        raise HTTPException(status_code=400, detail="리뷰 등록 실패")
    return {"message": "리뷰 등록 완료", "review": result}
