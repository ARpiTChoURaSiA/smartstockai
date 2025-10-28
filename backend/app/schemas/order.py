from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
