from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary")
def summary():
    return {"products": 0, "orders": 0, "alerts": 0}
