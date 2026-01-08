from fastapi import FastAPI
from app.endpoints import gamma, beta, zeta, mittag_leffler, random_forest, hash_table

app = FastAPI(
    title="ML App Project",
        description="Consultable cockpit of ML models and special functions",
            version="1.0.0"
            )

            # Include routers from each endpoint
            app.include_router(gamma.router)
            app.include_router(beta.router)
            app.include_router(zeta.router)
            app.include_router(mittag_leffler.router)
            app.include_router(random_forest.router)
            app.include_router(hash_table.router)

            @app.get("/")
            def root():
                return {"message": "Welcome to the ML App Project cockpit!"}