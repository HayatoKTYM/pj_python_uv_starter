"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.routes import health, items

app = FastAPI(
    title="Python UV Starter API",
    description="A starter template for Python projects using uv and FastAPI",
    version="0.1.0",
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(items.router, prefix="/api/v1", tags=["items"])


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to Python UV Starter API"}
