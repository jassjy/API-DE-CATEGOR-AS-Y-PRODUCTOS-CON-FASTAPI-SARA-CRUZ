# Registro de defectos

## DEF-001 — Se permitía crear productos con categoría inexistente

| Campo | Detalle |
|---|---|
| Estado | Cerrado después de corrección y retest |
| Severidad | Alta |
| Prioridad | Alta |
| Componente | `POST /products/` y `PATCH /products/{id}` |
| Caso relacionado | CP024 |
| Fecha | 17 de septiembre de 2026 |

**Descripción:** La API aceptaba cualquier texto en el campo `category`, aunque el alcance de pruebas exige que el producto pertenezca a una categoría existente.

**Pasos para reproducir:**

1. Ejecutar `POST /products/` con `{"name":"Mouse","category":"NoExiste","price":10,"stock":1}`.
2. Observar que la respuesta original era HTTP 201.
3. Verificar que el producto se agregaba a `products_db`.

**Resultado esperado:** HTTP 422 con el mensaje `Category does not exist`; el producto no debe crearse.

**Resultado obtenido antes de la corrección:** HTTP 201; el producto se creaba con una categoría inexistente.

**Corrección aplicada:** Se agregó una validación en `create_product` y `update_product` que compara la categoría recibida con `categories_db`. También se alinearon los datos iniciales para que `Laptops` y `Cameras` sean categorías válidas.

**Retest:** Se ejecutó `pytest -v tests/test_products.py -k cp024` después de la corrección. Resultado: `1 passed`.

**Regresión:** Se ejecutó `pytest -v` sobre productos y categorías. Resultado: `26 passed`, sin regresiones detectadas.

## Convención de clasificación

- **Severidad:** impacto técnico o funcional del hallazgo.
- **Prioridad:** urgencia para resolverlo.
- Un hallazgo puede tener severidad y prioridad diferentes; no se consideran sinónimos.
