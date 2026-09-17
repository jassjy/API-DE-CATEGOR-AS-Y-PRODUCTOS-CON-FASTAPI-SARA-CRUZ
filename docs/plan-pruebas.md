# Plan de pruebas — TechStore Products & Categories API

## 1. Identificación

| Campo | Valor |
|---|---|
| Proyecto | Products & Categories API |
| Versión auditada | 1.0.0 |
| Fecha | 17 de septiembre de 2026 |
| Responsable | Sara Jasmin Cruz Calderón / 3407180 |
| Ambiente | Python 3.12.3, FastAPI 0.141.1, Pydantic 2.13.5 |
| Persistencia | Listas en memoria, aisladas por fixture |

## 2. Objetivo

Verificar, con evidencia reproducible, que los endpoints de categorías y productos cumplen RF01–RF12 y RN01–RN08 del contrato del módulo IV. La auditoría cubre respuestas exitosas, validaciones, fronteras, recursos inexistentes, actualización, eliminación y asociación de productos con categorías.

## 3. Alcance funcional

| Recurso | Operaciones incluidas |
|---|---|
| Categorías | `POST /categories`, `GET /categories`, `GET /categories/{id}` |
| Productos | `POST /products`, `GET /products`, `GET /products/{id}`, `PUT /products/{id}`, `DELETE /products/{id}` |

Se verifican códigos 200, 201, 204, 404, 409 y 422, estructura JSON y reglas de negocio. Quedan fuera autenticación, autorización, UI, rendimiento, carga, seguridad especializada, persistencia real, migraciones y despliegue.

## 4. Estrategia

Se aplican pruebas funcionales positivas, negativas y de frontera. Los casos diseñados se identifican como CP-CAT-01 a CP-CAT-07 y CP-PROD-01 a CP-PROD-18. La selección completa está automatizada con pytest y `TestClient`; cada caso parte de datos aislados mediante el fixture `reset_db`.

## 5. Riesgos priorizados

| Riesgo | Probabilidad | Impacto | Prioridad | Mitigación |
|---|---|---|---|---|
| Aceptar categoría duplicada ignorando mayúsculas | Media | Alto | Alta | CP-CAT-07 |
| Aceptar nombres menores al mínimo | Alta | Medio | Alta | CP-CAT-05, CP-PROD-09 |
| Devolver código incorrecto para recurso inexistente | Media | Alto | Alta | CP-CAT-04, CP-PROD-04, 06, 08 |
| Aceptar precio cero o negativo | Alta | Alto | Alta | CP-PROD-11, 12, 13, 17 |
| Aceptar stock negativo o rechazar stock cero | Media | Alto | Alta | CP-PROD-14, 15 |
| Asociar producto a categoría inexistente | Media | Alto | Alta | CP-PROD-16, 18 |
| Perder datos durante actualización | Media | Medio | Media | CP-PROD-05 |

## 6. Ambiente, herramientas y datos

La ejecución se realiza desde la raíz con `python3 -m pip install -r requirements.txt` y `pytest -v`. Datos base: categorías Periféricos (1) y Audio (2); productos Mouse inalámbrico (120000, stock 5, categoría 1) y Monitor (850000, stock 0, categoría 1). Fronteras: nombre de 3 caracteres, precio 0, precio negativo, precio 0.01, stock 0, stock -1 e ID 99999.

## 7. Criterios de entrada

La aplicación debe importar, `TestClient` debe inicializarse, las dependencias deben estar instaladas, los endpoints del alcance deben existir y los datos de prueba deben estar definidos.

## 8. Suspensión y reanudación

Se suspende si la aplicación no importa, el cliente no inicia o un fallo bloquea los casos críticos. Se reanuda corrigiendo la causa, restaurando el ambiente, repitiendo el caso bloqueado y ejecutando la regresión completa.

## 9. Criterios de salida

Se considera cumplido el umbral cuando existe cobertura documental del 100 % de RF01–RF12 y RN01–RN08, se ejecuta el 100 % de los casos críticos y al menos el 90 % del total, no hay defectos críticos abiertos, hay mínimo 15 pruebas automatizadas y al menos el 90 % de aprobación de los casos ejecutados. Todo defecto debe estar vinculado a caso y requisito.

