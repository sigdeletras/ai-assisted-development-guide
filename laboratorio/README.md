# Laboratorio de desarrollo asistido por IA

Este laboratorio acompaña a la guía conceptual con ejercicios pequeños y verificables. Usa Python como punto de partida y un dominio geográfico sencillo —puntos de interés y GeoJSON— para practicar técnicas que se pueden trasladar a otros lenguajes y proyectos.

## Proyectos y ejercicios

| N.º | Ejercicio | Proyecto de práctica | Aprendizajes principales |
| --- | --- | --- | --- |
| 01 | [Primer contacto](01-primer-contacto/README.md) | Script Python para construir entidades GeoJSON | Chat, autocompletado, contexto, tareas acotadas, pruebas y revisión del diff. |
| 02 | [Proyecto nuevo](02-proyecto-nuevo/README.md) | API REST de puntos de interés geográficos | Requisitos y criterios de aceptación, diseño proporcional, implementación incremental, pruebas y documentación. |
| 03 | [Proyecto existente](03-proyecto-existente/README.md) | Repositorio ya desarrollado | Exploración sin cambios, pruebas de caracterización, cambios acotados, prevención de regresiones e instrucciones de proyecto. |
| 04 | Documentación y ciclo de vida del proyecto | **Propuesta pendiente de desarrollar** | Usar IA para mantener requisitos, historias de usuario, casos de uso, ADR, tareas y documentación técnica conectados durante la evolución del proyecto. |

Los tres primeros ejercicios están disponibles. El cuarto se plantea como una ampliación para practicar el uso de IA en la planificación y documentación del ciclo de vida, sin depender de un proveedor o agente concreto; no constituye todavía un ejercicio implementado.

Los ejercicios describen resultados esperados, no una solución que haya que copiar literalmente. Usa el asistente autorizado por tu organización y compara sus propuestas con los criterios de aceptación.

## Requisitos iniciales

- Python 3.11 o posterior.
- Git.
- Un editor o asistente de programación aprobado para el proyecto.
- Para ejecutar las pruebas del primer ejercicio: `python -m pip install pytest`.

El primer ejercicio no necesita servicios externos ni dependencias de geografía: utiliza coordenadas y la estructura GeoJSON directamente. FastAPI y otras dependencias se introducirán cuando aporten valor.

La guía define el objetivo de aprendizaje y enlaza al ejercicio pertinente. La plantilla editorial y el flujo para crear o revisar esos ejercicios están descritos en [Diseño de ejercicios de la guía](../docs/estructura-ejercicios.md).

## Método de trabajo

Para cada tarea:

1. Comprende el objetivo y las restricciones.
2. Pide al asistente un plan si el cambio no es trivial.
3. Trabaja en una modificación pequeña.
4. Revisa el diff y comprueba que entiendes el código.
5. Ejecuta las pruebas y registra cualquier limitación.

No introduzcas datos reales de clientes, credenciales ni información confidencial. No consideres correcto un cambio solo porque el asistente indique que ha terminado.
