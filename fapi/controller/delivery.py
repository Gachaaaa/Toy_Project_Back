from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from model import pgsql_delivery
from schema.user import UserToken
from utils.auth import get_current_user

router = APIRouter(
    prefix="/delivery",
    tags=["delivery"],
    responses={404: {"description": "Not found"}},
)

class DeliveryRequest(BaseModel):
    item_id: int
    address: str

@router.post("/")
def request_delivery(
    delivery: DeliveryRequest,
    current_user: UserToken = Depends(get_current_user)
):
    result = pgsql_delivery.create_delivery(
        user_id=current_user.user_id,
        item_id=delivery.item_id,
        address=delivery.address
    )
    if not result:
        raise HTTPException(status_code=400, detail="배송 요청 실패")
    return {"message": "배송 요청 완료", "delivery": result}
