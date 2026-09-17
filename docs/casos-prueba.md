# Casos de prueba

Todos los casos se ejecutan con `TestClient` y el fixture `reset_db`. Estado `PASSED` corresponde a la ejecución final de `pytest -v`.

## Categorías

| ID | Requisito/regla | Título y prioridad | Precondición | Datos | Pasos | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|---|---|---|
| CP-CAT-01 | RF01 | Crear válida — Alta | API disponible | `{"name":"Periféricos nuevos"}` | POST `/categories` | 201 y objeto creado | 201 y objeto | PASSED |
| CP-CAT-02 | RF02 | Listar — Alta | Categorías base | — | GET `/categories` | 200 y lista | 200 y lista | PASSED |
| CP-CAT-03 | RF03 | Consultar existente — Alta | Categoría 1 existe | ID 1 | GET `/categories/1` | 200 | 200 | PASSED |
| CP-CAT-04 | RF04 | Consultar inexistente — Alta | API disponible | ID 99999 | GET `/categories/99999` | 404 | 404 | PASSED |
| CP-CAT-05 | RN01 | Nombre menor al mínimo — Alta | API disponible | `name=AB` | POST `/categories` | 422 | 422 | PASSED |
| CP-CAT-06 | RN01 | Nombre de 3 caracteres — Media | API disponible | `name=Red` | POST `/categories` | 201 | 201 | PASSED |
| CP-CAT-07 | RN02 | Duplicado case-insensitive — Alta | Audio existe | `name=audio` | POST `/categories` | 409 | 409 | PASSED |

## Productos

| ID | Requisito/regla | Título y prioridad | Precondición | Datos | Pasos | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|---|---|---|
| CP-PROD-01 | RF05 | Crear válido — Alta | Categoría 1 existe | Teclado, 250000, 10, cat. 1 | POST `/products` | 201 | 201 | PASSED |
| CP-PROD-02 | RF06 | Listar — Alta | Productos base | — | GET `/products` | 200 y lista | 200 y lista | PASSED |
| CP-PROD-03 | RF07 | Consultar existente — Alta | Producto 1 existe | ID 1 | GET `/products/1` | 200 | 200 | PASSED |
| CP-PROD-04 | RF08 | Consultar inexistente — Alta | API disponible | ID 99999 | GET `/products/99999` | 404 | 404 | PASSED |
| CP-PROD-05 | RF09/RN08 | Actualizar válido — Alta | Producto 1 y cat. 1 existen | PUT con datos válidos | PUT `/products/1` | 200 y datos actualizados | 200 | PASSED |
| CP-PROD-06 | RF10 | Actualizar inexistente — Alta | API disponible | ID 99999 y payload válido | PUT `/products/99999` | 404 | 404 | PASSED |
| CP-PROD-07 | RF11 | Eliminar existente — Alta | Producto 1 existe | ID 1 | DELETE y GET posterior | 204 y luego 404 | 204 y 404 | PASSED |
| CP-PROD-08 | RF12 | Eliminar inexistente — Alta | API disponible | ID 99999 | DELETE `/products/99999` | 404 | 404 | PASSED |
| CP-PROD-09 | RN03 | Nombre menor a 3 — Alta | API disponible | `name=AB` | POST válido restante | 422 | 422 | PASSED |
| CP-PROD-10 | RN03 | Nombre de 3 caracteres — Media | Cat. 1 existe | `name=ABC` | POST producto | 201 | 201 | PASSED |
| CP-PROD-11 | RN04 | Precio 0 — Alta | API disponible | `price=0` | POST producto | 422 | 422 | PASSED |
| CP-PROD-12 | RN04 | Precio negativo — Alta | API disponible | `price=-1000` | POST producto | 422 | 422 | PASSED |
| CP-PROD-13 | RN04 | Precio mínimo positivo — Media | Cat. 1 existe | `price=0.01` | POST producto | 201 | 201 | PASSED |
| CP-PROD-14 | RN05/RN07 | Stock 0 — Alta | Cat. 1 existe | `stock=0` | POST producto | 201 y aceptación | 201 y aceptación | PASSED |
| CP-PROD-15 | RN05 | Stock negativo — Alta | API disponible | `stock=-1` | POST producto | 422 | 422 | PASSED |
| CP-PROD-16 | RN06 | Categoría inexistente al crear — Alta | API disponible | `category_id=99999` | POST producto | 404 | 404 | PASSED |
| CP-PROD-17 | RN08/RN04 | Precio inválido al actualizar — Alta | Producto 1 existe | PUT con `price=0` | PUT `/products/1` | 422 | 422 | PASSED |
| CP-PROD-18 | RN08/RN06 | Categoría inexistente al actualizar — Alta | Producto 1 existe | PUT con cat. 99999 | PUT `/products/1` | 404 | 404 | PASSED |

**Total:** 25 casos diseñados y 25 ejecutados. **Automatización:** 25/25; incluye 8 positivos, 10 negativos, 4 de frontera y operaciones de consulta, actualización y eliminación.
