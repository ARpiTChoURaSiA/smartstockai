from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import config
from .database import engine, Base
from .routes import products

settings = config.settings

app = FastAPI(title=settings.app_name)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=False,  # Set to False since we're not using credentials
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(products.router)


@app.on_event("startup")
def on_startup():
    # Ensure database tables exist for development/dev-run convenience
    Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": f"{settings.app_name} API is up"}


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# include routers when available
try:
    from .routes.products import router as products_router
    from .routes.suppliers import router as suppliers_router
    from .routes.orders import router as orders_router
    from .routes.alerts import router as alerts_router
    from .routes.dashboard import router as dashboard_router

    app.include_router(products_router)
    app.include_router(suppliers_router)
    app.include_router(orders_router)
    app.include_router(alerts_router)
    app.include_router(dashboard_router)
except Exception:
    # routes may not exist yet during initial scaffolding
    pass
