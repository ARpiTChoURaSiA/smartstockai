from typing import List
from ..schemas.order import OrderCreate

class OrderService:
    @staticmethod
    def list_orders() -> List[dict]:
        return []

    @staticmethod
    def create_order(data: OrderCreate) -> dict:
        return {**data.dict(), "id": 0, "created_at": "1970-01-01T00:00:00"}
