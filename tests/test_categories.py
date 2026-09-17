# CP-CAT-01 — Crear categoría válida (RF01)
def test_cp_cat_01_create_valid_category(client):
    response = client.post("/categories", json={"name": "Periféricos nuevos"})
    assert response.status_code == 201
    assert response.json()["name"] == "Periféricos nuevos"


# CP-CAT-02 — Listar categorías (RF02)
def test_cp_cat_02_list_categories(client):
    response = client.get("/categories")
    assert response.status_code == 200
    assert len(response.json()) >= 2


# CP-CAT-03 — Consultar categoría existente (RF03)
def test_cp_cat_03_get_existing_category(client):
    response = client.get("/categories/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


# CP-CAT-04 — Consultar categoría inexistente (RF04)
def test_cp_cat_04_get_missing_category(client):
    assert client.get("/categories/99999").status_code == 404


# CP-CAT-05 — Nombre menor a 3 caracteres (RN01)
def test_cp_cat_05_category_name_too_short(client):
    assert client.post("/categories", json={"name": "AB"}).status_code == 422


# CP-CAT-06 — Nombre exactamente de 3 caracteres (RN01)
def test_cp_cat_06_category_name_minimum(client):
    response = client.post("/categories", json={"name": "Red"})
    assert response.status_code == 201


# CP-CAT-07 — Duplicado sin distinguir mayúsculas/minúsculas (RN02)
def test_cp_cat_07_duplicate_category_case_insensitive(client):
    response = client.post("/categories", json={"name": "audio"})
    assert response.status_code == 409
