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

@router.get("/gacha/{gacha_id}")
def get_reviews_by_gacha(gacha_id: int):
    try:
        reviews = pgsql_gachareview.get_reviews_by_gacha_id(gacha_id)
        if not reviews:
            return {
                "count": 0,
                "gacha_id": gacha_id,
                "reviews": [],
                "message": "등록된 리뷰가 없습니다."
            }
        return {
            "count": len(reviews),
            "gacha_id": gacha_id,
            "reviews": reviews
        }
    except Exception as e:
        print("리뷰 조회 오류:", e)
        raise HTTPException(status_code=500, detail="리뷰 조회 중 오류 발생")