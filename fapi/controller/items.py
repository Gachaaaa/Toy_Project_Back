from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model import pgsql_item

router = APIRouter(
    prefix="/item",
    tags=["item"],
    responses={404: {"description": "Not found"}},
)

@router.get("/gacha/{gacha_id}")
def get_item_by_gacha(gacha_id: int):
    try:
        items = pgsql_item.get_items_by_gacha_id(gacha_id)
        if not items:
            return {"count": 0, "gacha_id": gacha_id, "itemss": [], "message": "등록된 아이템이 없습니다."}
        return {"count": len(items), "gacha_id": gacha_id, "items": items}
    except Exception as e:
        print("아이템 조회 오류:", e)
        raise HTTPException(status_code=500, detail="아이템템 조회 중 오류 발생")
