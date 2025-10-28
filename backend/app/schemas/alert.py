from pydantic import BaseModel
from typing import Optional

class AlertBase(BaseModel):
    name: str
    message: Optional[str] = None
    active: bool = True

class AlertCreate(AlertBase):
    pass

class AlertRead(AlertBase):
    id: int

    class Config:
        from_attributes = True
