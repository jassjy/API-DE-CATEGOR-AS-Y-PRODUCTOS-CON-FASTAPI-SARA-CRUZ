import pytest
from fastapi.testclient import TestClient

from app import main as main_module
from app.main import app


INITIAL_PRODUCTS = [
    {"id": 1, "name": "Product 1", "category": "Laptops", "price": 10.99, "stock": 100, "available": True},
    {"id": 2, "name": "Product 2", "category": "Cameras", "price": 15.99, "stock": 50, "available": True},
    {"id": 3, "name": "Product 3", "category": "Laptops", "price": 20.99, "stock": 0, "available": False},
    {"id": 4, "name": "Product 4", "category": "Cameras", "price": 25.99, "stock": 30, "available": True},
    {"id": 5, "name": "Product 5", "category": "Laptops", "price": 30.99, "stock": 20, "available": True},
]

INITIAL_CATEGORIES = [
    {"id": 1, "name": "Computadores", "description": "Equipos de cómputo", "active": True},
    {"id": 2, "name": "Accesorios", "description": "Periféricos y accesorios", "active": False},
]


@pytest.fixture(autouse=True)
def reset_db(monkeypatch):
    """Restaura AMBAS bases antes de CADA test para evitar contaminación."""
    monkeypatch.setattr(main_module, "products_db", [p.copy() for p in INITIAL_PRODUCTS])
    monkeypatch.setattr(main_module, "categories_db", [c.copy() for c in INITIAL_CATEGORIES])


@pytest.fixture
def client():
    return TestClient(app)