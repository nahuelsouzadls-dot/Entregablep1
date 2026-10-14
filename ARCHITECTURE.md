# ARCHITECTURE.md — Estructura y Diseño de Clases (Nivel P1)

## 1. Diseño Orientado a Objetos Académico
El diseño replica fielmente el diagrama de clases del laboratorio universitario, priorizando claridad y simplicidad conceptual:

```text
Sistema
 ├── opciones: list (instancias de ServicioAPI o PlanMensual)
 ├── criterios: list (instancias de Criterio)
 ├── casos: list (instancias de CasoUso)
 └── evaluaciones: list (instancias de Evaluacion)

Criterio:
 - codigo: int
 - nombre: str
 - peso: int

OpcionIA (Abstracta):
 - codigo: int
 - nombre: str
 - puntajes: dict {cod_criterio: int}
 └── Métodos: costo_estimado() [abstracto]

ServicioAPI(OpcionIA):
 - costo_por_1000: float
 - consultas_estimadas: int
 └── costo_estimado() -> (consultas_estimadas / 1000) * costo_por_1000

PlanMensual(OpcionIA):
 - usuarios: int
 - costo_por_usuario: float
 └── costo_estimado() -> usuarios * costo_por_usuario

CasoUso:
 - codigo: int
 - nombre: str
 - presupuesto: float
 - puntaje_minimo: float

Evaluacion:
 - codigo: int
 - opcion: OpcionIA
 - caso: CasoUso
 - fecha: datetime
 - estado: str
 └── Métodos: puntaje_total(), costo_total(), recalcular_estado()
```
