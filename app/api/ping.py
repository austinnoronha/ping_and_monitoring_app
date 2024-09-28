"""API Ping."""

import hashlib
import json
import os

from fastapi import APIRouter, HTTPException, Request, Response, status
from fastapi.templating import Jinja2Templates

from app.lib.config import APP_PATH
from app.lib.logger import (  # Adjust the import based on your project structure
    setup_logger,
)
from app.schemas.ping import PingRequest

logger = setup_logger(__name__)

router = APIRouter(prefix="/ping", tags=["ping"])

templates = Jinja2Templates(directory="app/templates")

FILE_PATH = f"{APP_PATH}/datastore/stored_requests.json"  # Store the requests in this JSON file


@router.get("/add")
def get_ping_form(request: Request):
    """Ping Form API."""
    return templates.TemplateResponse("ping/ping_form.html", {"request": request})


def generate_hash(url: str, request_type: str, payload: dict) -> str:
    """Generate a unique hash for a request based on URL, type, and payload."""
    unique_string = f"{url}{request_type}{json.dumps(payload, sort_keys=True)}"
    return hashlib.sha256(unique_string.encode()).hexdigest()


def save_request_to_file(request_data: dict) -> str:
    """Save the request to a JSON file with a unique hash as the key."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH) as file:
            stored_requests = json.load(file)
    else:
        stored_requests = {}

    # Convert HttpUrl object to string
    request_data["url"] = str(request_data["url"])

    request_hash = generate_hash(request_data["url"], request_data["request_type"], request_data["payload"])

    is_new = True
    if request_hash in stored_requests:
        is_new = False

    # Add new request
    stored_requests[request_hash] = request_data

    with open(FILE_PATH, "w") as file:
        json.dump(stored_requests, file, indent=4)

    return request_hash, is_new


@router.post("/store", status_code=status.HTTP_200_OK)
async def store_ping_request(ping_request: PingRequest, response: Response):
    """Store the API ping request in a JSON file by a scheduled task."""
    if ping_request.request_type not in ["POST", "GET", "DELETE", "UPDATE", "PUT"]:
        logger.error(
            "/ping/store error: request_type %s is not supported",
            ping_request.request_type,
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request type not supported, please add POST, GET, DELETE, UPDATE, PUT methods",
        )

    try:
        request_data = {
            "url": ping_request.url,
            "request_type": ping_request.request_type,
            "payload": ping_request.payload,
        }
        request_hash, is_new = save_request_to_file(request_data)

        if is_new:
            response.status_code = status.HTTP_201_CREATED

        logger.info("/ping/store success!")
        return {"message": "Request stored successfully", "data": [request_hash]}
    except Exception as e:
        logger.error("Exception /ping/store error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Exception raised!",
        )
