"""Schema Ping."""

from typing import Optional

from pydantic import BaseModel, HttpUrl


class PingRequest(BaseModel):
    """Pydantic Model for Ping Requests."""

    url: HttpUrl  # Ensures the provided URL is valid
    request_type: Optional[str] = "GET"  # GET, POST, DELETE, PUT
    payload: Optional[str] = None  # Optional payload for non-GET requests
