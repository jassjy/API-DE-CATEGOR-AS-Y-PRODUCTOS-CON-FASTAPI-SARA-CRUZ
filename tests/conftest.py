import pytest
from fastapi.testclient import TestClient

from app import main as main_module
from app.main import app

INITIAL_CATEGORIES = [
    {"id": 1, "name": "Periféricos"},
    {"id": 2, "name": "Audio"},
]
INITIAL_PRODUCTS = [
    {"id": 1, "name": "Mouse inalámbrico", "price": 120000.0, "stock": 5, "category_id": 1},
    {"id": 2, "name": "Monitor", "price": 850000.0, "stock": 0, "category_id": 1},
]


@pytest.fixture(autouse=True)
def reset_db(monkeypatch):
    monkeypatch.setattr(main_module, "categories_db", [item.copy() for item in INITIAL_CATEGORIES])
    monkeypatch.setattr(main_module, "products_db", [item.copy() for item in INITIAL_PRODUCTS])


@pytest.fixture
def client():
    return TestClient(app)
