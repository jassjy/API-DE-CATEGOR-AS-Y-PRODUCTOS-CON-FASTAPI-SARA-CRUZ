# Casos de prueba

Los casos se ejecutan contra un ambiente aislado y se identifican con el mismo código usado en los nombres o comentarios de `tests/`.

## Casos positivos

### CP001 — Listar productos
- **Requisito:** RF01. **Prioridad:** Alta.
- **Precondición:** Datos iniciales cargados.
- **Pasos:** Enviar `GET /products/` y revisar la respuesta.
- **Resultado esperado:** HTTP 200, lista JSON con los productos.

### CP002 — Filtrar productos
- **Requisito:** RF01. **Prioridad:** Media.
- **Datos:** `GET /products/?category=Laptops`.
- **Resultado esperado:** HTTP 200; cada elemento pertenece a Laptops.

### CP003 — Consultar producto existente
- **Requisito:** RF02. **Prioridad:** Alta.
- **Datos:** `GET /products/1`.
- **Resultado esperado:** HTTP 200 y objeto con `id=1`.

### CP005 — Crear producto válido
- **Requisito:** RF03, RN03, RN07. **Prioridad:** Crítica.
- **Datos:** `{"name":"Mouse QA","category":"Accesorios","price":120000,"stock":5}`.
- **Resultado esperado:** HTTP 201, ID generado y `available=true`.

### CP010 — Actualizar producto
- **Requisito:** RF04. **Prioridad:** Alta.
- **Datos:** `PATCH /products/1` con `{"price":99.99}`.
- **Resultado esperado:** HTTP 200; precio actualizado y demás campos conservados.

### CP011 — Recalcular disponibilidad
- **Requisito:** RN07. **Prioridad:** Alta.
- **Datos:** `PATCH /products/1` con `{"stock":0}`.
- **Resultado esperado:** HTTP 200 y `available=false`.

### CP012 — Eliminar producto existente
- **Requisito:** RF05. **Prioridad:** Alta.
- **Pasos:** Crear un producto, enviar DELETE por su ID y consultarlo nuevamente.
- **Resultado esperado:** DELETE HTTP 204; consulta posterior HTTP 404.

### CP014 — Listar categorías
- **Requisito:** RF06. **Prioridad:** Alta.
- **Resultado esperado:** HTTP 200 y lista JSON.

### CP018 — Crear categoría válida
- **Requisito:** RF08, RN04. **Prioridad:** Alta.
- **Datos:** `{"name":"Tablets","description":"Dispositivos táctiles","active":true}`.
- **Resultado esperado:** HTTP 201 y categoría creada.

## Casos negativos

### CP004 — Consultar producto inexistente
- **Requisito:** RN05. **Prioridad:** Crítica.
- **Datos:** `GET /products/999`.
- **Resultado esperado:** HTTP 404; no se devuelve producto válido.

### CP006 — Rechazar precio cero
- **Requisito:** RN02. **Prioridad:** Alta.
- **Datos:** Producto válido con `price=0`.
- **Resultado esperado:** HTTP 422 y no se crea el producto.

### CP007 — Rechazar precio negativo y stock negativo
- **Requisito:** RN02, RN03. **Prioridad:** Crítica.
- **Datos:** `price=-1` o `stock=-1`.
- **Resultado esperado:** HTTP 422.

### CP008 — Rechazar nombre de producto ausente
- **Requisito:** RN01. **Prioridad:** Alta.
- **Datos:** Producto sin `name`.
- **Resultado esperado:** HTTP 422.

### CP009 — Rechazar nombre de producto demasiado corto
- **Requisito:** RN01. **Prioridad:** Media.
- **Datos:** `name="A"`.
- **Resultado esperado:** HTTP 422.

### CP013 — No eliminar producto inexistente
- **Requisito:** RF05, RN05. **Prioridad:** Alta.
- **Datos:** `DELETE /products/999`.
- **Resultado esperado:** HTTP 404.

### CP017 — Consultar categoría inexistente
- **Requisito:** RF07, RN05. **Prioridad:** Alta.
- **Datos:** `GET /categories/999`.
- **Resultado esperado:** HTTP 404.

### CP019 — Rechazar categoría con nombre corto
- **Requisito:** RN04, RN06. **Prioridad:** Alta.
- **Datos:** `POST /categories` con `{"name":"AB"}`.
- **Resultado esperado:** HTTP 422.

### CP021 — No actualizar categoría inexistente
- **Requisito:** RF09, RN05. **Prioridad:** Media.
- **Datos:** `PATCH /categories/999`.
- **Resultado esperado:** HTTP 404.

### CP023 — No eliminar categoría inexistente
- **Requisito:** RF10, RN05. **Prioridad:** Media.
- **Datos:** `DELETE /categories/999`.
- **Resultado esperado:** HTTP 404.

### CP024 — Rechazar categoría inexistente en producto
- **Requisito:** RN04, RN06. **Prioridad:** Crítica.
- **Datos:** Producto con `category="NoExiste"`.
- **Resultado esperado:** HTTP 422 y el producto no se crea.

### CP026 — Buscar categorías por nombre
- **Requisito:** RF06. **Prioridad:** Media.
- **Datos:** `GET /categories?search=comp`.
- **Resultado esperado:** HTTP 200 y la categoría Computadores.

### CP027 — Búsqueda sin coincidencias
- **Requisito:** RF06. **Prioridad:** Baja.
- **Datos:** `GET /categories?search=zzz`.
- **Resultado esperado:** HTTP 200 y lista vacía.

### CP028 — Consultar listado de productos
- **Requisito:** RF01. **Prioridad:** Alta.
- **Datos:** `GET /products/`.
- **Resultado esperado:** HTTP 200 y lista JSON.

### CP029 — Filtrar categorías activas
- **Requisito:** RF06. **Prioridad:** Media.
- **Datos:** `GET /categories?active=true`.
- **Resultado esperado:** HTTP 200 y únicamente categorías activas.

## Casos de frontera

### CP005-F — Crear producto con stock igual a cero
- **Requisito:** RN03, RN07. **Prioridad:** Alta.
- **Datos:** Producto válido con `stock=0`.
- **Resultado esperado:** HTTP 201 y `available=false`.

### CP006-F — Crear producto con precio mínimo válido
- **Requisito:** RN02. **Prioridad:** Alta.
- **Datos:** Producto válido con `price=0.01`.
- **Resultado esperado:** HTTP 201.

### CP007-F — Rechazar stock menor al límite
- **Requisito:** RN03. **Prioridad:** Alta.
- **Datos:** Producto válido con `stock=-1`.
- **Resultado esperado:** HTTP 422.

La suite automatizada cubre los casos críticos y representativos; los restantes quedan especificados para ejecución manual o ampliación futura.
