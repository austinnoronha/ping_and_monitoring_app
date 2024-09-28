"""Pytest - Ping API."""

import json
import os

import pytest
from fastapi.testclient import TestClient

from app.lib.config import APP_PATH
from app.main import app

client = TestClient(app)

FILE_PATH = f"{APP_PATH}/datastore/stored_requests.json"


@pytest.fixture(autouse=True)
def clear_json_file():
    """Fixture to clear the JSON file before each test."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump({}, file)


def test_store_ping_request():
    """Test for successfully storing a new API ping request."""
    payload = {
        "url": "https://api.example.com/data",
        "request_type": "POST",
        "payload": '{"name":"value"}',
    }
    response = client.post("/ping/store", json=payload)
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()["message"] == "Request stored successfully"
    assert len(response.json()["data"]) == 1  # Should return the request hash


def test_duplicate_request():
    """Test for storing duplicate ping requests."""
    payload = {
        "url": "https://api.example.com/data",
        "request_type": "POST",
        "payload": '{"name":"value"}',
    }

    # Store first request
    response = client.post("/ping/store", json=payload)
    assert response.status_code == 201

    # Try storing the same request again
    response = client.post("/ping/store", json=payload)
    assert response.status_code == 200  # Should not throw an error, but return status 200


def test_store_ping_request_with_get():
    """Test storing a GET request."""
    payload = {
        "url": "https://api.example.com/health",
        "request_type": "GET",
        "payload": None,  # No payload for GET request
    }
    response = client.post("/ping/store", json=payload)
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()["message"] == "Request stored successfully"
    assert len(response.json()["data"]) == 1


def test_store_ping_request_invalid_method():
    """Test with an invalid request type."""
    payload = {
        "url": "https://api.example.com/invalid",
        "request_type": "INVALID",
        "payload": "{}",
    }
    response = client.post("/ping/store", json=payload)
    assert response.status_code == 400  # Should return an error due to invalid request type
