from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import router
from app.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="1.0.0",
        description="Modular Scientific & ML API Suite"
    )

    # -----------------------------
    # CORS
    # -----------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # -----------------------------
    # Routers
    # -----------------------------
    app.include_router(router)

    # -----------------------------
    # Health Check
    # -----------------------------
    @app.get("/health")
    def health():
        return {"status": "ok"}

    # -----------------------------
    # Startup / Shutdown Events
    # -----------------------------
    @app.on_event("startup")
    async def startup_event():
        print("🚀 ML App Project starting up...")

    @app.on_event("shutdown")
    async def shutdown_event():
        print("🛑 ML App Project shutting down...")

    return app

app = create_app()