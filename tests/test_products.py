# =====================================================
# TESTS DE PRODUCTOS
# Los fixtures reset_db y client vienen de conftest.py
# =====================================================


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 5


def test_get_existing_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data


def test_get_non_existing_product(client):
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Product with id 999 not found"}


def test_create_product(client):
    payload = {
        "name": "New Product",
        "category": "Laptops",
        "price": 49.99,
        "stock": 10,
    }
    response = client.post("/products/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "New Product"
    assert data["available"] is True
    assert "id" in data


def test_update_product(client):
    response = client.patch("/products/1", json={"price": 99.99})
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 99.99
    assert data["id"] == 1


def test_update_product_stock_recalculates_available(client):
    response = client.patch("/products/1", json={"stock": 0})
    assert response.status_code == 200
    data = response.json()
    assert data["stock"] == 0
    assert data["available"] is False


def test_delete_product(client):
    # Creamos uno primero para no romper otros tests
    created = client.post(
        "/products/",
        json={"name": "To Delete", "category": "Cameras", "price": 1.0, "stock": 1},
    ).json()
    product_id = created["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 204
    assert client.get(f"/products/{product_id}").status_code == 404


def test_filters(client):
    # Filtrar por categoría
    response = client.get("/products/?category=Laptops")
    assert response.status_code == 200
    assert all(p["category"] == "Laptops" for p in response.json())

    # Filtrar por available
    response = client.get("/products/?available=true")
    assert response.status_code == 200
    assert all(p["available"] is True for p in response.json())

    # Buscar por nombre
    response = client.get("/products/?search=Product 1")
    assert response.status_code == 200
    assert any("Product 1" in p["name"] for p in response.json())