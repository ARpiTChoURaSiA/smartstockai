from fastapi import APIRouter
from typing import List
from ..schemas.order import OrderCreate, OrderRead

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/", response_model=List[OrderRead])
def list_orders():
    return []

@router.post("/", response_model=OrderRead)
def create_order(payload: OrderCreate):
    return {**payload.dict(), "id": 0, "created_at": "1970-01-01T00:00:00"}
