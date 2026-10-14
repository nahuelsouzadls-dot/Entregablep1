# TESTING_GUIDE.md — Verificación Manual y Pruebas de Consola

Sigue este flujo paso a paso en consola para validar que el comportamiento cumpla exactamente con los criterios de evaluación de Programación 1:

### Paso 1: Registrar Criterios
1. Registrar Criterio: "Calidad de Respuesta", Peso: 5.
2. Registrar Criterio: "Facilidad de Integración", Peso: 3.
3. Registrar Criterio: "Disponibilidad", Peso: 2.
- *Verificación:* Intentar registrar con peso 0 o negativo (debe rebotar y volver a pedir).

### Paso 2: Registrar Opciones de IA
1. Registrar "OpenAI API" (Servicio API):
   - Costo por 1000: 20 USD.
   - Consultas estimadas: 5000.
   - Costo mensual esperado: (5000 / 1000) * 20 = 100 USD.
   - Puntajes: Calidad: 9, Integración: 8, Disponibilidad: 9.
   - Puntaje ponderado: (9*5 + 8*3 + 9*2) / 10 = 8.70.
2. *Verificación de regla de corte:* Intentar volver al menú de Criterios y agregar uno nuevo (debe arrojar error porque ya existe una opción registrada).
3. Registrar "Claude Team" (Plan Mensual):
   - Usuarios: 4.
   - Costo por usuario: 30 USD.
   - Costo mensual esperado: 4 * 30 = 120 USD.
   - Puntajes: Calidad: 9, Integración: 9, Disponibilidad: 8.
   - Puntaje ponderado: (9*5 + 9*3 + 8*2) / 10 = 8.80.

### Paso 3: Registrar Caso de Uso
1. Registrar Caso: "Soporte Técnico".
   - Presupuesto mensual: 110 USD.
   - Puntaje mínimo: 8.5.

### Paso 4: Comparar Opciones para el Caso
1. Ejecutar opción 2 del menú principal (Comparar opciones para el caso "Soporte Técnico").
- *Resultados esperados:*
  - **OpenAI API:** Costo 100 <= 110 y Puntaje 8.70 >= 8.5 -> **Recomendada**.
  - **Claude Team:** Costo 120 > 110 -> **Fuera de presupuesto**.

### Paso 5: Probar Actualizaciones Dinámicas
1. Actualizar Presupuesto del Caso "Soporte Técnico" a 150 USD.
   - Listar evaluaciones: Claude Team debe pasar inmediatamente a **Recomendada** sin cambiar la fecha original de su evaluación.
2. Ver Ranking del caso:
   - Posición 1: Claude Team (Puntaje: 8.80, Costo: 120 USD).
   - Posición 2: OpenAI API (Puntaje: 8.70, Costo: 100 USD).
