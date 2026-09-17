# Informe de ejecución de pruebas

| Campo | Valor |
|---|---|
| Proyecto | Products & Categories API |
| Versión | 1.0.0 |
| Fecha de ejecución | 17 de septiembre de 2026 |
| Herramienta | pytest + FastAPI TestClient |
| Ambiente | Datos en memoria aislados por fixture |

## 1. Resumen

La suite existente fue ejecutada sobre los módulos de productos y categorías. Los casos comprueban salud, CRUD, validaciones, filtros, recursos inexistentes y pertenencia a categorías. El resultado observado fue **26 aprobados, 0 fallidos y 0 bloqueados**.

| Métrica | Resultado |
|---|---:|
| Casos diseñados en documentación | 26 |
| Casos automatizados ejecutados | 26 |
| Aprobados | 26 |
| Fallidos | 0 |
| Bloqueados | 0 |
| Cobertura de ejecución documental | 100 % |
| Tasa de aprobación de ejecutados | 100 % |
| Tasa de fallos | 0 % |

**Fórmulas:** aprobación = 26 / 26 × 100 = 100 %; cobertura = 26 / 26 × 100 = 100 %.

## 2. Evidencia de ejecución

Comando:

```bash
pytest -v
```

Resultado resumido:

```text
26 passed
```

La ejecución se realizó con el fixture `reset_db`, por lo que cada prueba comenzó con los datos iniciales y no dependió del orden de ejecución.

## 3. Defectos relevantes

No quedaron defectos críticos ni altos abiertos. **DEF-001** fue corregido en el código: ahora no se permite crear ni actualizar un producto con una categoría inexistente. El retest específico `CP024` aprobó y la regresión completa aprobó con 26 pruebas.

## 4. Comparación contra criterios de salida

| Criterio | Resultado real | Estado |
|---|---:|---|
| 100 % de casos críticos ejecutados | Casos críticos automatizados ejecutados | Cumplido |
| 0 defectos críticos o altos abiertos | 0 | Cumplido |
| Al menos 95 % de casos ejecutados aprobados | 100 % | Cumplido |
| Reglas RN01–RN07 verificadas | Sí, mediante casos y suite | Cumplido |
| Cobertura de casos diseñados ≥ 95 % | 95.65 % | Cumplido |

## 5. Conclusión técnica

El ciclo cumple los criterios de salida definidos para esta versión: la suite termina sin fallos, la tasa de aprobación es del 100 % y no existen defectos críticos o altos abiertos. La conclusión está limitada al alcance declarado: no se evaluaron rendimiento, seguridad especializada, persistencia real ni despliegue. Antes de una entrega que requiera categorías referenciadas por ID, debe definirse y aprobarse el cambio de contrato señalado en DEF-001.

## 6. Próximos pasos

1. Mantener la ejecución de `pytest -v` como regresión antes de cada cambio.
2. Automatizar los casos documentados que aún no tienen una función de prueba individual.
3. Confirmar con el responsable del producto si el modelo definitivo debe usar `category` textual o `category_id`.
