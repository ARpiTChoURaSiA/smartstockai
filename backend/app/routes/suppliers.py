from fastapi import APIRouter
from typing import List
from ..schemas.supplier import SupplierCreate, SupplierRead

router = APIRouter(prefix="/suppliers", tags=["suppliers"])

@router.get("/", response_model=List[SupplierRead])
def list_suppliers():
    return []

@router.post("/", response_model=SupplierRead)
def create_supplier(payload: SupplierCreate):
    return {**payload.dict(), "id": 0}
