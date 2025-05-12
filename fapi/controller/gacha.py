from fastapi import APIRouter, HTTPException
from model import pgsql_gacha

router = APIRouter(
    prefix="/gacha",
    tags=["gacha"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_all_gacha():
    try:
        gachas = pgsql_gacha.get_all_gacha()
        return {"count": len(gachas), "gacha": gachas}
    except Exception as e:
        print("가챠 조회 오류:", e)
        raise HTTPException(status_code=500, detail="가챠 정보를 불러오는 중 오류가 발생했습니다.")
