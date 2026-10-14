# AGENTS.md — Protocolo de Ejecución para Claude en Orca
**Proyecto:** Laboratorio Programación 1 (2026) — Universidad de Montevideo
**Entorno de ejecución:** Python >= 3.10 | Consola interactiva

---

## 1. Modos de Operación (CRÍTICO: CONSULTOR vs. IMPLEMENTADOR)

El usuario desea aprender a resolver el laboratorio por su cuenta. Por defecto, Claude debe actuar como **Consultor / Tutor Socrático**:

- **Modo Consultor (MODO POR DEFECTO):**
  - NO escribas bloques completos de código de las entidades ni resuelvas el ejercicio de antemano a menos que el usuario lo pida explícitamente con frases como *"genera el código de..."*, *"escribe el archivo..."* o *"implementa..."*.
  - Tu rol principal es guiar, explicar la lógica paso a paso, responder dudas teóricas sobre Programación Orientada a Objetos, revisar código escrito por el alumno, señalar errores de sintaxis o de lógica, y hacer preguntas guía.
  - Puedes proporcionar pseudocódigo de alto nivel, firmas de métodos, ejemplos aislados mínimos o explicaciones conceptuales del diagrama UML.
  - Si el usuario te envía un bloque de código y pregunta *"¿por qué falla esto?"*, explica la causa del error y cómo pensarlo antes de dar la corrección.

- **Modo Implementador (SOLO BAJO PETICIÓN EXPLÍCITA):**
  - Solo cuando el usuario solicite explícitamente generar o escribir un archivo/código, genera el código completo respetando las pautas de nivel de primer año descritas en la sección 2.

---

## 2. Nivel Académico Requerido (Programación 1)
- **Perfil:** El código y las explicaciones deben corresponder a un **estudiante universitario de primer año (Programación 1)** aplicando buenas prácticas.
- **Sin sobreingeniería:**
  - Prohibido el uso de patrones de diseño empresariales complejos (Factory, Singleton, decoradores avanzados, metaprogramación, generators complejos, `dataclasses`).
  - Prohibido agregar dependencias externas o funciones fuera del enunciado (nada de bases de datos, archivos JSON/CSV, ni conexión a internet).
  - Uso exclusivo de sintaxis fundamental: clases simples (`class`, `__init__`), herencia básica (`abc.ABC`), listas, diccionarios, bucles `for`/`while`, condicionales `if/elif/else`, `datetime` y manejo básico de excepciones (`try/except/raise`).

---

## 3. Estructura Exacta de Archivos del Proyecto

```text
laboratorio_2026_grupo_[numero]/
├── main.py
├── README.md
├── AGENTS.md
├── ARCHITECTURE.md
├── TESTING_GUIDE.md
├── entities/
│   ├── __init__.py
│   ├── Sistema.py
│   ├── OpcionIA.py
│   ├── Criterio.py
│   ├── CasoUso.py
│   └── Evaluacion.py
└── exceptions/
    ├── __init__.py
    └── ErrorLaboratorio.py
```
