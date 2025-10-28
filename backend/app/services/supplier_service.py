from typing import List
from ..schemas.supplier import SupplierCreate

class SupplierService:
    @staticmethod
    def list_suppliers() -> List[dict]:
        return []

    @staticmethod
    def create_supplier(data: SupplierCreate) -> dict:
        return {**data.dict(), "id": 0}
