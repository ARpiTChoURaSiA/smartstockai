# routes package
from fastapi import APIRouter

router = APIRouter()

# Individual route modules register their routers on import
try:
    from . import products, suppliers, orders, alerts, dashboard  # noqa: F401
except Exception:
    pass
