# Laboratorio de desarrollo asistido por IA

Este laboratorio acompaña a la guía conceptual con ejercicios pequeños y verificables. Usa Python como punto de partida y un dominio geográfico sencillo —puntos de interés y GeoJSON— para practicar técnicas que se pueden trasladar a otros lenguajes y proyectos.

## Recorrido

1. **[01 · Primer contacto](01-primer-contacto/README.md)**: practicar chat, autocompletado y cambios pequeños sobre un script existente.
2. **[02 · Proyecto nuevo](02-proyecto-nuevo/README.md)**: convertir requisitos en un proyecto estructurado, con pruebas y una API REST.
3. **[03 · Proyecto existente](03-proyecto-existente/README.md)**: analizar un repositorio, establecer una línea base y decidir qué necesita para trabajar con IA.
4. **[04 · Configuración del entorno de IA](04-configuracion-entorno-ia/README.md)**: crear y validar instrucciones, rules y skills, y evaluar agentes, hooks y permisos según las necesidades del proyecto.
5. **[05 · Desarrollo de una funcionalidad con IA](05-desarrollo-funcionalidad-ia/README.md)**: especificar una funcionalidad, revisar y confirmar el plan de la IA, implementar por incrementos y verificar el resultado.

Los laboratorios 03, 04 y 05 forman una secuencia recomendada: diagnosticar el proyecto, preparar el entorno y aplicar ese contexto al desarrollo de una funcionalidad. Pueden consultarse por separado si ya se dispone de los resultados de las fases anteriores.

El laboratorio 03 se centra en el diagnóstico y la preparación. El laboratorio 04 parte de ese diagnóstico y se centra en implementar y validar la configuración seleccionada. El laboratorio 05 practica la delegación controlada del desarrollo, con confirmación del plan antes de editar código y revisión humana del resultado. No es obligatorio crear todos los tipos de archivo ni habilitar todas las capacidades.

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
