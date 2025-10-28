from typing import List
from ..schemas.alert import AlertCreate

class AlertService:
    @staticmethod
    def list_alerts() -> List[dict]:
        return []

    @staticmethod
    def create_alert(data: AlertCreate) -> dict:
        return {**data.dict(), "id": 0}
