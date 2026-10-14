# Laboratorio Programación 1 (2026) — Universidad de Montevideo

Sistema de consola para comparar opciones de Inteligencia Artificial según criterios ponderados, para distintos casos de uso con presupuesto y puntaje mínimo.

## Requisitos
- Python 3.10 o superior.
- No usa librerías externas.

## Cómo ejecutar
Desde la carpeta raíz del proyecto:

```bash
python3 main.py
```

## Estructura del proyecto

```text
├── main.py                 # Menú interactivo por consola
├── README.md
├── AGENTS.md
├── ARCHITECTURE.md         # Diseño de clases
├── TESTING_GUIDE.md        # Pruebas manuales paso a paso
├── entities/
│   ├── Sistema.py          # Guarda y administra todos los datos
│   ├── OpcionIA.py         # OpcionIA (abstracta), ServicioAPI y PlanMensual
│   ├── Criterio.py
│   ├── CasoUso.py
│   └── Evaluacion.py
└── exceptions/
    └── ErrorLaboratorio.py # Excepción propia del sistema
```

## Funcionalidades

### Menú principal
1. **Registro de datos**: abre un submenú para registrar y listar criterios, opciones de IA y casos de uso.
2. **Comparar opciones para un caso de uso**: evalúa todas las opciones registradas para el caso elegido.
3. **Listar evaluaciones de un caso de uso**.
4. **Ver ranking de un caso de uso**: ordena por puntaje (de mayor a menor); si hay empate, va primero la más barata.
5. **Actualizar presupuesto de un caso de uso**: recalcula los estados sin cambiar la fecha de las evaluaciones.
0. **Salir**.

### Cálculos
- **Servicio API**: costo mensual = (consultas estimadas / 1000) × costo por 1000 consultas.
- **Plan Mensual**: costo mensual = usuarios × costo por usuario.
- **Puntaje ponderado**: suma de (puntaje × peso) dividida entre la suma de los pesos.

### Estados de una evaluación
- **Fuera de presupuesto**: el costo mensual supera el presupuesto del caso.
- **Puntaje insuficiente**: el puntaje ponderado es menor al puntaje mínimo del caso.
- **Recomendada**: cumple con el presupuesto y con el puntaje mínimo.

### Reglas y validaciones
- El peso de un criterio debe ser un entero mayor a 0.
- Los puntajes de las opciones van de 0 a 10.
- No se pueden agregar criterios una vez que hay opciones de IA registradas.
- Para registrar una opción de IA debe existir al menos un criterio.
- No se permiten nombres repetidos de criterios, opciones o casos de uso.
- Los datos se guardan solo en memoria mientras el programa está abierto.

## Pruebas
El flujo de verificación manual está en [TESTING_GUIDE.md](TESTING_GUIDE.md).
