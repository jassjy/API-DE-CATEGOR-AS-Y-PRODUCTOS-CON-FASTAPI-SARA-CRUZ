# Informe de ejecución de pruebas

## 1. Identificación y ambiente

| Campo | Valor |
|---|---|
| Proyecto | TechStore Products & Categories API |
|---|---|
| Versión | 1.0.0 |
| Commit auditado | `f47851a` |
| Fecha | 17 de septiembre de 2026 |
| Ambiente | Linux, Python 3.12.3, FastAPI 0.141.1, pytest 9.1.1 |
| Comando | `pytest -v` |
| Persistencia | Memoria; reset por caso |

## 2. Resultado de la ejecución

La ejecución final recolectó 25 casos y todos aprobaron.

| Métrica | Resultado |
|---|---:|
| Casos diseñados | 25 |
| Casos ejecutados | 25 |
| PASSED | 25 |
| FAILED | 0 |
| BLOCKED | 0 |
| NOT EXECUTED | 0 |
| Porcentaje de aprobación | 100 % (25/25 × 100) |
| Cobertura de ejecución | 100 % (25/25 × 100) |
| Automatización | 25 casos |
| Defectos críticos abiertos | 0 |
| Defectos altos abiertos | 0 |

La salida completa queda conservada en `pytest-final.txt`. El único warning observado fue una advertencia de deprecación de `starlette.testclient` en una dependencia; no produjo fallos ni afecta el contrato funcional.

## 3. Retest y regresión

El defecto DEF-001 se corrigió alineando el modelo a `category_id`, agregando la validación de categoría existente y cambiando la actualización a `PUT`. El retest específico correspondió a CP-PROD-16, CP-PROD-17 y CP-PROD-18, todos PASSED. La regresión completa posterior fue `25 passed, 0 failed`.

## 4. Criterios de salida

| Criterio | Resultado | Estado |
|---|---|---|
| RF01–RF12 y RN01–RN08 con trazabilidad | 20/20 cubiertos | Cumplido |
| 100 % de casos críticos ejecutados | 100 % | Cumplido |
| Al menos 90 % del total ejecutado | 100 % | Cumplido |
| Mínimo 15 casos automatizados | 25 | Cumplido |
| Aprobación mínima de 90 % | 100 % | Cumplido |
| 0 defectos críticos abiertos | 0 | Cumplido |
| Defectos trazables | DEF-001 vinculado a requisitos y casos | Cumplido |

## 5. Conclusión técnica

La versión auditada cumple el contrato funcional definido para Categories & Products API dentro del alcance declarado. Los 25 casos diseñados, incluidos positivos, negativos y de frontera, fueron reproducibles y aprobaron. El riesgo funcional detectado durante la comparación inicial con el contrato fue corregido y confirmado mediante retest y regresión. La conclusión no cubre rendimiento, seguridad especializada, persistencia real ni despliegue.
