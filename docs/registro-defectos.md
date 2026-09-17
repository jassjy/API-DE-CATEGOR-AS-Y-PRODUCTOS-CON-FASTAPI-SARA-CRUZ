# Registro de defectos

## DEF-001 — Modelo de producto no cumplía la asociación por `category_id`

| Campo | Detalle |
|---|---|
| Requisito relacionado | RF05, RN06, RN08 |
| Casos relacionados | CP-PROD-01, CP-PROD-16, CP-PROD-18 |
| Severidad | Alta |
| Prioridad | Alta |
| Estado | Cerrado después de corrección y retest |
| Componente | Esquemas y endpoints de productos |
| Evidencia | Inspección inicial de `app/schemas.py` y `app/main.py`; la versión original recibía `category` textual y no verificaba su existencia |

**Precondición:** API original ejecutándose con sus datos en memoria.

**Pasos para reproducir:** Enviar `POST /products` con un producto cuya categoría no exista y observar que la implementación original aceptaba texto libre. La implementación original tampoco exponía `PUT /products/{id}` como exige EP07.

**Resultado esperado:** El contrato exige `category_id`, categoría existente y respuesta 404 cuando no existe; la actualización debe usar PUT.

**Resultado obtenido inicial:** Contrato no satisfecho: se usaba `category` textual, no se garantizaba RN06 y el método era PATCH.

**Corrección aplicada:** Se actualizaron `schemas.py`, `database.py` y `main.py` para usar `category_id`, validar categoría con 404, implementar `PUT /products/{id}` y aplicar todas las validaciones de creación al actualizar.

**Retest:** CP-PROD-16, CP-PROD-17 y CP-PROD-18 aprobaron.

**Regresión:** `pytest -v` ejecutó 25 casos: 25 passed, 0 failed.

## Clasificación

No se inventaron defectos adicionales. Los fallos de la suite final fueron cero; cualquier warning de deprecación pertenece a una dependencia del ambiente y no altera el contrato funcional.
