# Incidencia: validar puntos de interés

## Situación y comportamiento actual

La función `build_feature` genera una entidad GeoJSON de tipo `Point`. El código actual acepta nombres vacíos y coordenadas fuera del rango geográfico válido. Además, una clave `name` incluida en `properties` puede sobrescribir el argumento `name`.

Antes de modificar la implementación, ejecuta las pruebas existentes y registra la salida real. La prueba de `test_geojson.py` que documenta la sobrescritura de `name` caracteriza el comportamiento actual: no significa que ese comportamiento sea deseable ni que deba conservarse tras resolver la incidencia. No afirmes que la línea base pasa hasta haber ejecutado las pruebas.

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

1. Registra `git status --short --branch` y ejecuta las pruebas existentes. Guarda comandos, salidas y limitaciones como línea base.
2. Pide al asistente que explique la función y sus riesgos, sin modificar archivos. Contrasta la explicación con el código.
3. Añade en `tests/test_regression.py` pruebas que expresen los criterios deseados. Incluye casos normales, límites, entradas inválidas y la prioridad del argumento `name`.
4. Mantén diferenciados los dos tipos de prueba: las de caracterización describen el comportamiento previo; las de regresión verifican el comportamiento requerido. Si una prueba existente codifica el defecto, actualízala cuando el requisito nuevo lo contradiga, dejando clara la razón.
5. Solicita un plan pequeño que indique archivos afectados, cambios previstos y pruebas; revísalo y confírmalo antes de permitir ediciones de implementación.
6. Implementa solo lo necesario para resolver esta incidencia. No amplíes el alcance con una refactorización general.
7. Ejecuta las pruebas pertinentes y el conjunto completo; registra la salida real y revisa `git diff` y el estado de Git.
8. En el cierre, relaciona cada criterio de aceptación con la prueba o evidencia que lo verifica e indica explícitamente las comprobaciones no ejecutadas.

Decide explícitamente qué excepción debe producirse para cada entrada inválida y documenta esa decisión en las pruebas. No amplíes el alcance con una refactorización general.
