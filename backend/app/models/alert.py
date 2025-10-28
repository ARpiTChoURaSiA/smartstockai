from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    message = Column(String, nullable=True)
    active = Column(Boolean, default=True)
