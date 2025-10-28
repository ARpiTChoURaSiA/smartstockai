from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    sku: Optional[str] = None
    price: float
    quantity: int
    supplier_id: Optional[int] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True
