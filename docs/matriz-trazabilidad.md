# Matriz de trazabilidad

| ID requisito | Requisito / regla | Casos relacionados |
|---|---|---|
| RF01 | Consultar listado de productos | CP002, CP028 |
| RF02 | Consultar producto por ID | CP003, CP004 |
| RF03 | Crear producto | CP005, CP006, CP007, CP008, CP009 |
| RF04 | Actualizar parcialmente producto | CP010, CP011 |
| RF05 | Eliminar producto | CP012, CP013 |
| RF06 | Consultar listado de categorías | CP014, CP029 |
| RF07 | Consultar categoría por ID | CP016, CP017 |
| RF08 | Crear categoría | CP018, CP019 |
| RF09 | Actualizar parcialmente categoría | CP020, CP021 |
| RF10 | Eliminar categoría | CP022, CP023 |
| RN01 | Nombre de producto obligatorio y válido | CP008, CP009 |
| RN02 | Precio mayor que cero | CP006, CP007 |
| RN03 | Stock mayor o igual que cero | CP005, CP007 |
| RN04 | Nombre de categoría obligatorio y válido | CP018, CP019, CP020 |
| RN05 | Recurso inexistente responde 404 | CP004, CP017, CP013, CP022, CP023 |
| RN06 | Entrada inválida responde 422 | CP006, CP007, CP009, CP015, CP019, CP020, CP024 |
| RN07 | Cálculo de `available` según stock | CP005, CP011 |

Todos los requisitos incluidos en el alcance tienen al menos un caso asociado. Los casos CP001–CP023 son únicos y se reutilizan en la documentación de casos, pruebas automatizadas y reporte de ejecución.
