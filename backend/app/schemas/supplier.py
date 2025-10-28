from pydantic import BaseModel
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierRead(SupplierBase):
    id: int

    class Config:
        from_attributes = True
