from typing import List
from ..schemas.product import ProductCreate

class ProductService:
    @staticmethod
    def list_products() -> List[dict]:
        return []

    @staticmethod
    def create_product(data: ProductCreate) -> dict:
        return {**data.dict(), "id": 0}
