# =====================================================
# TESTS DE CATEGORÍAS (CA01 - CA12 + RETO OPCIONAL)
# Los fixtures reset_db y client vienen de conftest.py
# =====================================================


# CA01 - Listar categorías
def test_list_categories(client):
    response = client.get("/categories")
    assert response.status_code == 200
    assert len(response.json()) == 2


# CA02 - Consultar existente
def test_get_existing_category(client):
    response = client.get("/categories/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Computadores"


# CA03 - Consultar inexistente
def test_get_non_existing_category(client):
    response = client.get("/categories/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Category with id 999 not found"}


# CA04 - ID inválido
def test_get_invalid_id(client):
    response = client.get("/categories/abc")
    assert response.status_code == 422


# CA05 - Crear válida
def test_create_valid_category(client):
    payload = {"name": "Tablets", "description": "Dispositivos táctiles", "active": True}
    response = client.post("/categories", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 3
    assert data["name"] == "Tablets"


# CA06 - Nombre demasiado corto
def test_create_category_name_too_short(client):
    response = client.post("/categories", json={"name": "AB"})
    assert response.status_code == 422


# CA07 - Falta nombre
def test_create_category_missing_name(client):
    response = client.post("/categories", json={"description": "Sin nombre"})
    assert response.status_code == 422


# CA08 - Actualizar existente
def test_update_existing_category(client):
    response = client.patch("/categories/1", json={"name": "PCs"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "PCs"
    assert data["description"] == "Equipos de cómputo"


# CA09 - Actualizar inexistente
def test_update_non_existing_category(client):
    response = client.patch("/categories/999", json={"name": "X"})
    assert response.status_code == 404


# CA10 - Eliminar existente
def test_delete_existing_category(client):
    response = client.delete("/categories/1")
    assert response.status_code == 204
    assert client.get("/categories/1").status_code == 404


# CA11 - Eliminar inexistente
def test_delete_non_existing_category(client):
    response = client.delete("/categories/999")
    assert response.status_code == 404


# CA12 - Filtrar activas
def test_filter_active_categories(client):
    response = client.get("/categories?active=true")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert all(c["active"] is True for c in data)


# RETO OPCIONAL 1 - Búsqueda por nombre
def test_search_categories(client):
    response = client.get("/categories?search=comp")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Computadores"


# RETO OPCIONAL 2 - Búsqueda sin resultados
def test_search_categories_no_match(client):
    response = client.get("/categories?search=zzz")
    assert response.status_code == 200
    assert response.json() == []