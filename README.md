# MODULO 3

python -m venv .venv

.venv\Scripts\Activate.ps1 

python -m pip install fastapi

python -m pip install "uvicorn[standard]"

python -m pip install pytest httpx

python -m pip freeze > requirements.txt

python -m pip install -r requirements.txt



API REST desarrollada con **FastAPI** que administra dos recursos:

- **Productos** (`/products`)
- **Categorías** (`/categories`)

Los datos se almacenan **temporalmente en memoria** (`products_db` y `categories_db`), por lo que se reinician cada vez que se detiene el servidor.

---

##  Tecnologías

- Python 3.10+
- FastAPI
- Pydantic v2
- Uvicorn
- pytest + TestClient
- httpx

---

## Estructura del proyecto

```
mi-proyecto/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── schemas.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_categories.py
│   └── test_products.py
│
├── requirements.txt
└── README.md
```

---



##  Ejecutar la API

Desde la raíz del proyecto:

```bash
uvicorn app.main:app --reload
```

La API quedará disponible en:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:**       http://127.0.0.1:8000/redoc
- **Raíz:**        http://127.0.0.1:8000/
- **Health:**      http://127.0.0.1:8000/health


Para detener el servidor: `Ctrl + C`.

---

##  Ejecutar las pruebas

En otra terminal (con el entorno virtual activado):

```bash
pytest -v
```

---

##  Endpoints

### Productos

| Método | Endpoint                        | Descripción                              | Código OK |
|--------|---------------------------------|------------------------------------------|-----------|
| GET    | `/products/`                    | Listar productos                         | 200       |
| GET    | `/products/?category=Laptops`   | Filtrar por categoría                    | 200       |
| GET    | `/products/?available=true`     | Filtrar por disponibilidad               | 200       |
| GET    | `/products/?search=Product 1`   | Buscar por nombre o categoría            | 200       |
| GET    | `/products/{product_id}`        | Consultar producto por ID                | 200       |
| POST   | `/products/`                    | Crear producto                           | 201       |
| PATCH  | `/products/{product_id}`        | Actualización parcial                    | 200       |
| DELETE | `/products/{product_id}`        | Eliminar producto                        | 204       |

### Categorías

| Método | Endpoint                        | Descripción                              | Código OK |
|--------|---------------------------------|------------------------------------------|-----------|
| GET    | `/categories`                   | Listar categorías                        | 200       |
| GET    | `/categories?active=true`       | Filtrar categorías activas               | 200       |
| GET    | `/categories?search=comp`       | Buscar por nombre (case-insensitive)     | 200       |
| GET    | `/categories/{category_id}`     | Consultar categoría por ID               | 200       |
| POST   | `/categories`                   | Crear categoría                          | 201       |
| PATCH  | `/categories/{category_id}`     | Actualización parcial                    | 200       |
| DELETE | `/categories/{category_id}`     | Eliminar categoría                       | 204       |

### Otros

| Método | Endpoint   | Descripción           |
|--------|------------|-----------------------|
| GET    | `/`        | Mensaje de bienvenida |
| GET    | `/health`  | Estado del servicio   |

---

##  Modelos de datos

### Producto

```json
{
  "id": 1,
  "name": "Product 1",
  "category": "Laptops",
  "price": 10.99,
  "stock": 100,
  "available": true
}
```

**Validaciones:**
- `name`: obligatorio, 2–100 caracteres.
- `category`: obligatorio, 2–100 caracteres.
- `price`: obligatorio, mayor que 0.
- `stock`: obligatorio, mayor o igual que 0.
- `available`: opcional. Si no se envía, se calcula como `stock > 0`.
- `id`: generado automáticamente por la API.

### Categoría

```json
{
  "id": 1,
  "name": "Computadores",
  "description": "Equipos de cómputo",
  "active": true
}
```

**Validaciones:**
- `name`: obligatorio, 3–50 caracteres.
- `description`: opcional, máximo 200 caracteres.
- `active`: opcional, booleano, `true` por defecto.
- `id`: generado automáticamente por la API.

---

##  Códigos HTTP usados

| Código | Significado                                |
|--------|--------------------------------------------|
| 200    | OK — consulta o actualización exitosa      |
| 201    | Created — recurso creado                   |
| 204    | No Content — recurso eliminado             |
| 404    | Not Found — recurso inexistente            |
| 422    | Unprocessable Entity — datos inválidos     |

---

##  Casos de prueba cubiertos

### Categorías (CA01 – CA12 + Reto opcional)

| ID   | Escenario                | Esperado                     |
|------|--------------------------|------------------------------|
| CA01 | Listar categorías        | 200 y lista JSON             |
| CA02 | Consultar existente      | 200                          |
| CA03 | Consultar inexistente    | 404                          |
| CA04 | ID inválido              | 422                          |
| CA05 | Crear válida             | 201                          |
| CA06 | Nombre demasiado corto   | 422                          |
| CA07 | Falta nombre             | 422                          |
| CA08 | Actualizar existente     | 200                          |
| CA09 | Actualizar inexistente   | 404                          |
| CA10 | Eliminar existente       | 204                          |
| CA11 | Eliminar inexistente     | 404                          |
| CA12 | Filtrar activas          | 200 y solo `active=true`     |
| Extra 1 | Búsqueda con match    | 200 + resultado              |
| Extra 2 | Búsqueda sin match    | 200 + lista vacía            |

### Productos

| Escenario                                    | Esperado |
|----------------------------------------------|----------|
| Health check                                 | 200      |
| Listar productos                             | 200      |
| Consultar producto existente / inexistente   | 200 / 404|
| Crear producto válido                        | 201      |
| Actualizar producto                          | 200      |
| Recalcular `available` al cambiar `stock`    | 200      |
| Eliminar producto existente                  | 204      |
| Filtros por categoría, disponibilidad y search | 200    |

---

##  Aislamiento de pruebas

El archivo `tests/conftest.py` define dos fixtures:

- `reset_db` (**autouse**): restaura `products_db` y `categories_db` antes de **cada** test, evitando que una prueba contamine a otra.
- `client`: instancia reutilizable de `TestClient(app)`.

Gracias a esto, los tests pueden ejecutarse **en cualquier orden** y siempre pasan.