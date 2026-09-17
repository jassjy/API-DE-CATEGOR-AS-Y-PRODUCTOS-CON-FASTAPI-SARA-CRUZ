VALID_PRODUCT = {"name": "Teclado mecánico", "price": 250000, "stock": 10, "category_id": 1}


# CP-PROD-01 — Crear producto válido (RF05)
def test_cp_prod_01_create_product(client):
    response = client.post("/products", json=VALID_PRODUCT)
    assert response.status_code == 201
    assert response.json()["category_id"] == 1


# CP-PROD-02 — Listar productos (RF06)
def test_cp_prod_02_list_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# CP-PROD-03 — Consultar producto existente (RF07)
def test_cp_prod_03_get_existing_product(client):
    assert client.get("/products/1").status_code == 200


# CP-PROD-04 — Consultar producto inexistente (RF08)
def test_cp_prod_04_get_missing_product(client):
    assert client.get("/products/99999").status_code == 404


# CP-PROD-05 — Actualizar producto válido (RF09)
def test_cp_prod_05_update_product(client):
    payload = {**VALID_PRODUCT, "name": "Teclado actualizado"}
    response = client.put("/products/1", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Teclado actualizado"


# CP-PROD-06 — Actualizar producto inexistente (RF10)
def test_cp_prod_06_update_missing_product(client):
    assert client.put("/products/99999", json=VALID_PRODUCT).status_code == 404


# CP-PROD-07 — Eliminar producto existente (RF11)
def test_cp_prod_07_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 204
    assert client.get("/products/1").status_code == 404


# CP-PROD-08 — Eliminar producto inexistente (RF12)
def test_cp_prod_08_delete_missing_product(client):
    assert client.delete("/products/99999").status_code == 404


# CP-PROD-09 — Nombre menor a 3 caracteres (RN03)
def test_cp_prod_09_name_too_short(client):
    assert client.post("/products", json={**VALID_PRODUCT, "name": "AB"}).status_code == 422


# CP-PROD-10 — Nombre exactamente de 3 caracteres (RN03)
def test_cp_prod_10_name_minimum(client):
    assert client.post("/products", json={**VALID_PRODUCT, "name": "ABC"}).status_code == 201


# CP-PROD-11 — Precio igual a 0 (RN04)
def test_cp_prod_11_price_zero(client):
    assert client.post("/products", json={**VALID_PRODUCT, "price": 0}).status_code == 422


# CP-PROD-12 — Precio negativo (RN04)
def test_cp_prod_12_price_negative(client):
    assert client.post("/products", json={**VALID_PRODUCT, "price": -1000}).status_code == 422


# CP-PROD-13 — Precio mínimo positivo (RN04)
def test_cp_prod_13_price_minimum_positive(client):
    assert client.post("/products", json={**VALID_PRODUCT, "price": 0.01}).status_code == 201


# CP-PROD-14 — Stock igual a 0 (RN05/RN07)
def test_cp_prod_14_zero_stock_is_accepted(client):
    assert client.post("/products", json={**VALID_PRODUCT, "stock": 0}).status_code == 201


# CP-PROD-15 — Stock negativo (RN05)
def test_cp_prod_15_negative_stock(client):
    assert client.post("/products", json={**VALID_PRODUCT, "stock": -1}).status_code == 422


# CP-PROD-16 — Categoría inexistente al crear (RN06)
def test_cp_prod_16_missing_category_on_create(client):
    assert client.post("/products", json={**VALID_PRODUCT, "category_id": 99999}).status_code == 404


# CP-PROD-17 — Precio inválido al actualizar (RN08)
def test_cp_prod_17_invalid_price_on_update(client):
    assert client.put("/products/1", json={**VALID_PRODUCT, "price": 0}).status_code == 422


# CP-PROD-18 — Categoría inexistente al actualizar (RN08/RN06)
def test_cp_prod_18_missing_category_on_update(client):
    assert client.put("/products/1", json={**VALID_PRODUCT, "category_id": 99999}).status_code == 404
