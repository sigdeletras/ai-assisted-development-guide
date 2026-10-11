# Incidencia: validar puntos de interés

## Situación y comportamiento actual

La función `build_feature` genera una entidad GeoJSON de tipo `Point`. El código actual acepta nombres vacíos y coordenadas fuera del rango geográfico válido. Además, una clave `name` incluida en `properties` puede sobrescribir el argumento `name`.

La prueba de `tests/test_geojson.py` que documenta la sobrescritura de `name` caracteriza el comportamiento actual: no significa que ese comportamiento sea deseable ni que deba conservarse tras resolver la incidencia.

## Cambio solicitado

Añadir validación sin reescribir el módulo ni cambiar la estructura de la entidad para entradas válidas. No incluye una refactorización general.

## Criterios de aceptación

- El nombre debe contener texto no vacío después de eliminar espacios en los extremos.
- La longitud debe estar entre -180 y 180, ambos incluidos.
- La latitud debe estar entre -90 y 90, ambos incluidos.
- Las coordenadas no pueden ser `NaN` ni infinito.
- Una propiedad adicional llamada `name` no debe sobrescribir el nombre principal recibido como argumento.
- Las entradas válidas deben conservar el formato GeoJSON actual y las propiedades adicionales.
- Los casos normales, límites y entradas inválidas deben estar cubiertos por pruebas automatizadas en `tests/test_regression.py`.

## Decisiones pendientes

- Excepción que debe producirse para cada entrada inválida. La decisión debe quedar documentada en las pruebas.
