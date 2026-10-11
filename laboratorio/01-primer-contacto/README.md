# 01 · Primer contacto

## Objetivo

Practicar chat, autocompletado y edición puntual en un script Python pequeño, aprendiendo a dar contexto y a verificar el resultado sin delegar todo el ejercicio al asistente.

## Punto de partida

El módulo `src/pois.py` contiene una función para construir una entidad GeoJSON de tipo `Point`. No utiliza librerías externas.

## Ejercicios

### A. Comprender antes de cambiar

Pide al asistente que explique:

- qué argumentos recibe la función;
- en qué orden se guardan las coordenadas en GeoJSON;
- qué casos no valida todavía;
- qué pruebas convendría añadir.

Pídele que no modifique archivos en esta primera interacción. Contrasta la explicación con el código y la especificación de [RFC 7946](https://www.rfc-editor.org/rfc/rfc7946).

### B. Autocompletado

Escribe tú una pequeña función o prueba y utiliza el autocompletado para completarla. Revisa el resultado línea a línea; acepta solo lo que entiendas y puedas justificar.

### C. Encargar una tarea acotada

Solicita implementar validación de longitud y latitud. Antes de aceptar el cambio, acuerda estos criterios:

- longitud entre -180 y 180, ambos incluidos;
- latitud entre -90 y 90, ambos incluidos;
- rechazar valores fuera de rango y coordenadas no finitas;
- mantener el orden GeoJSON `[longitud, latitud]`;
- añadir pruebas para valores válidos y casos límite.

### D. Verificación

Instala pytest si aún no está disponible y ejecuta desde esta carpeta:

```bash
python -m pip install pytest
python -m pytest
```

Revisa los cambios con `git diff`. Si una prueba falla, pide al asistente que explique el fallo antes de aceptar una corrección.

## Criterios de finalización

- Puedes explicar el código y el orden de las coordenadas.
- Las pruebas cubren casos normales, límites y entradas inválidas.
- El cambio es pequeño y el diff no contiene modificaciones ajenas a la tarea.
- Has ejecutado las pruebas localmente.

## Preguntas de reflexión

- ¿Qué contexto hizo mejorar la respuesta?
- ¿Qué error detectaste al revisar el código?
- ¿Habría sido mejor usar chat, autocompletado o un agente para cada tarea?
