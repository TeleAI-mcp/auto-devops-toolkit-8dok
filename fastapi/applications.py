"""
FastAPI applications.
"""
from typing import Any, Dict

from fastapi import FastAPI


def get_app() -> FastAPI:
    """
    Create a FastAPI application.

    Returns:
        FastAPI: The FastAPI application.
    """
    app = FastAPI()

    @app.get("/")
    async def root() -> Dict[str, Any]:
        """Root endpoint."""
        return {"message": "Hello World"}

    return app
