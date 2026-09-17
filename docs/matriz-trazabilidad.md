# Matriz de trazabilidad

| ID | Descripción | Casos relacionados | Cobertura |
|---|---|---|---|
| RF01 | Crear categoría válida | CP-CAT-01 | Cubierto |
| RF02 | Listar categorías | CP-CAT-02 | Cubierto |
| RF03 | Consultar categoría existente | CP-CAT-03 | Cubierto |
| RF04 | 404 para categoría inexistente | CP-CAT-04 | Cubierto |
| RF05 | Crear producto con categoría existente | CP-PROD-01, CP-PROD-10, CP-PROD-13, CP-PROD-14 | Cubierto |
| RF06 | Listar productos | CP-PROD-02 | Cubierto |
| RF07 | Consultar producto existente | CP-PROD-03 | Cubierto |
| RF08 | 404 para producto inexistente | CP-PROD-04 | Cubierto |
| RF09 | Actualizar producto válido | CP-PROD-05 | Cubierto |
| RF10 | 404 al actualizar inexistente | CP-PROD-06 | Cubierto |
| RF11 | Eliminar producto existente | CP-PROD-07 | Cubierto |
| RF12 | 404 al eliminar inexistente | CP-PROD-08 | Cubierto |
| RN01 | Nombre de categoría obligatorio, 3–60 | CP-CAT-05, CP-CAT-06 | Cubierto |
| RN02 | Nombre de categoría no repetido case-insensitive | CP-CAT-07 | Cubierto |
| RN03 | Nombre de producto obligatorio, 3–80 | CP-PROD-09, CP-PROD-10 | Cubierto |
| RN04 | Precio estrictamente mayor que 0 | CP-PROD-11, CP-PROD-12, CP-PROD-13, CP-PROD-17 | Cubierto |
| RN05 | Stock mayor o igual que 0 | CP-PROD-14, CP-PROD-15 | Cubierto |
| RN06 | `category_id` debe existir | CP-PROD-16, CP-PROD-18 | Cubierto |
| RN07 | Stock 0 debe aceptarse | CP-PROD-14 | Cubierto |
| RN08 | PUT conserva las validaciones de creación | CP-PROD-05, CP-PROD-17, CP-PROD-18 | Cubierto |

**Cobertura documental:** 20/20 elementos del contrato relacionados con al menos un caso: 100 %. Cada caso está automatizado en `tests/test_categories.py` o `tests/test_products.py`.
