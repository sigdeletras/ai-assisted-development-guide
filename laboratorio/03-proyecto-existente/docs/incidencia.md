# Incidencia: validar puntos de interés

## Situación

La función `build_feature` genera una entidad GeoJSON de tipo `Point`, pero acepta nombres vacíos y coordenadas fuera del rango geográfico válido. Además, una clave `name` incluida en `properties` puede sobrescribir el argumento `name`.

## Cambio solicitado

Añadir validación sin reescribir el módulo ni cambiar la estructura de la entidad para entradas válidas.

## Criterios de aceptación

- El nombre debe contener texto no vacío después de eliminar espacios en los extremos.
- La longitud debe estar entre -180 y 180, ambos incluidos.
- La latitud debe estar entre -90 y 90, ambos incluidos.
- Las coordenadas no pueden ser `NaN` ni infinito.
- Una propiedad adicional llamada `name` no debe sobrescribir el nombre principal recibido como argumento.
- Las entradas válidas deben conservar el formato GeoJSON actual y las propiedades adicionales.
- Los casos normales, límites y entradas inválidas deben estar cubiertos por pruebas automatizadas.

## Secuencia recomendada

1. Ejecuta las pruebas existentes y guarda el resultado inicial.
2. Pide al asistente que explique la función y sus riesgos, sin modificar archivos.
3. Añade pruebas para cada criterio de aceptación antes de implementar.
4. Solicita un plan pequeño y revisa la propuesta.
5. Implementa solo lo necesario para resolver esta incidencia.
6. Ejecuta todas las pruebas y revisa `git diff`.

Decide explícitamente qué excepción debe producirse para cada entrada inválida y documenta esa decisión en las pruebas. No amplíes el alcance con una refactorización general.
