from fastapi import APIRouter
from typing import List
from ..schemas.alert import AlertCreate, AlertRead

router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/", response_model=List[AlertRead])
def list_alerts():
    return []

@router.post("/", response_model=AlertRead)
def create_alert(payload: AlertCreate):
    return {**payload.dict(), "id": 0}
