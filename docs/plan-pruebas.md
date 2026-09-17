# Plan de Pruebas

## 1. Información general

| Campo | Valor |
|---|---|
| Proyecto | Products & Categories API |
| Versión | 1.0.0 |
| Tecnologías | Python 3.x, FastAPI, Pydantic, pytest, TestClient |
| Persistencia | Estructuras en memoria para ambiente de pruebas |
| Responsable | Sara Jasmin Cruz Calderon / 3407180|
| Fecha | 17 de septiembre de 2026 |

## 2. Objetivo

Verificar que la API de productos y categorías cumpla los comportamientos funcionales definidos, incluyendo respuestas exitosas, validaciones de entrada, consulta y manejo de recursos inexistentes, actualización parcial, eliminación, filtros y endpoints de salud.

## 3. Alcance

### Incluido

- `GET /` y `GET /health`.
- Consulta, creación, actualización parcial (`PATCH`) y eliminación de productos.
- Consulta, creación, actualización parcial (`PATCH`) y eliminación de categorías.
- Filtros de productos por `category`, `available` y `search`.
- Filtros de categorías por `active` y `search`.
- Códigos HTTP, estructura JSON y mensajes de error.
- Validaciones Pydantic: nombre, precio mayor que cero, stock no negativo y tipos de datos.
- Casos positivos, negativos y de frontera.

### Fuera de alcance

- Autenticación, autorización y gestión de usuarios.
- Pruebas de rendimiento, concurrencia y carga.
- Seguridad especializada, inyección y análisis de dependencias.
- Interfaz gráfica.
- Persistencia real en una base de datos y migraciones.
- Despliegue en producción, observabilidad y recuperación ante fallos de infraestructura.

## 4. Requisitos y reglas verificables

| ID | Descripción |
|---|---|
| RF01 | Consultar el listado de productos |
| RF02 | Consultar un producto por ID |
| RF03 | Crear un producto |
| RF04 | Actualizar parcialmente un producto |
| RF05 | Eliminar un producto |
| RF06 | Consultar el listado de categorías |
| RF07 | Consultar una categoría por ID |
| RF08 | Crear una categoría |
| RF09 | Actualizar parcialmente una categoría |
| RF10 | Eliminar una categoría |
| RN01 | El nombre del producto es obligatorio y debe tener entre 2 y 100 caracteres |
| RN02 | El precio del producto debe ser mayor que cero |
| RN03 | El stock del producto no puede ser negativo |
| RN04 | El nombre de la categoría es obligatorio y debe tener entre 3 y 50 caracteres |
| RN05 | Un recurso inexistente debe responder HTTP 404 |
| RN06 | Una entrada con tipos o formato inválido debe responder HTTP 422 |
| RN07 | Al crear o cambiar stock, `available` se calcula como `stock > 0` cuando no se envía explícitamente |

## 5. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Prioridad |
|---|---|---|---|---|
| R01 | Aceptar un precio cero o negativo | Media | Alto | Alta |
| R02 | Aceptar stock negativo | Media | Alto | Alta |
| R03 | Crear un producto sin nombre o con nombre inválido | Media | Alto | Alta |
| R04 | Devolver 200 para un producto o categoría inexistente | Alta | Alto | Crítica |
| R05 | No recalcular `available` después de cambiar el stock | Media | Medio | Alta |
| R06 | Eliminar un recurso inexistente sin informar el error | Media | Alto | Alta |
| R07 | Romper la información existente al actualizar parcialmente | Media | Medio | Media |
| R08 | Devolver datos incorrectos al aplicar filtros | Media | Medio | Media |

Se priorizan R01, R02 y R04 porque afectan directamente la integridad de los datos y los contratos HTTP básicos de la API.

## 6. Estrategia

Se aplicarán pruebas funcionales para verificar cada endpoint; pruebas positivas con datos válidos; pruebas negativas con datos ausentes, inválidos o recursos inexistentes; pruebas de frontera para precio, stock y longitudes mínimas; y pruebas automatizadas repetibles mediante pytest y `TestClient`. Se usará aislamiento por caso mediante el fixture `reset_db`, que restaura los datos iniciales antes de cada prueba.

## 7. Ambiente

- Sistema operativo: Linux/Windows compatible.
- Python: 3.x.
- Framework: FastAPI 0.141.1.
- Validación: Pydantic 2.13.5.
- Servidor opcional: Uvicorn 0.52.4.
- Pruebas: pytest 9.1.1 y FastAPI TestClient.
- Base de datos: listas en memoria (`app/database.py`); no usar datos de producción.

Comandos de ejecución:

```bash
pip install -r requirements.txt
pytest -v
```

## 8. Datos de prueba

| Escenario | Datos | Resultado esperado |
|---|---|---|
| Producto válido | `name=Mouse`, `category=Accesorios`, `price=120000`, `stock=5` | HTTP 201 |
| Precio frontera válido | `price=0.01` | HTTP 201 |
| Precio inválido | `price=0` o `price=-1` | HTTP 422 |
| Stock frontera válido | `stock=0` | HTTP 201 y `available=false` |
| Stock inválido | `stock=-1` | HTTP 422 |
| Nombre ausente | Sin `name` | HTTP 422 |
| Categoría válida | `name=Tablets` | HTTP 201 |
| Categoría inválida | `name=AB` | HTTP 422 |
| ID inexistente | `999` | HTTP 404 |

## 9. Criterios de entrada

- La aplicación puede importarse y `TestClient` puede inicializarse.
- Los endpoints del alcance están implementados.
- Las dependencias de `requirements.txt` están instaladas.
- Los datos de prueba están definidos.
- Los requisitos y reglas verificables están disponibles.

## 10. Criterios de suspensión y reanudación

Se suspenderá el ciclo si la aplicación no puede importarse, el cliente HTTP no puede inicializarse o un fallo bloquea la ejecución de los casos críticos. Se reanudará después de corregir la causa, restaurar el ambiente y ejecutar nuevamente el caso bloqueado y la regresión completa.

## 11. Criterios de salida

- 100 % de los casos críticos ejecutados.
- 0 defectos críticos o altos abiertos.
- Al menos 95 % de los casos ejecutados aprobados.
- Reglas RN01–RN07 verificadas.
- La suite automatizada termina sin errores de configuración.
