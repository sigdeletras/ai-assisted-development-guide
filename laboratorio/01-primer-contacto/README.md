# 01 · Primer contacto

## Objetivo

Practicar chat, autocompletado y edición puntual en un script Python pequeño, aprendiendo a dar contexto y a verificar el resultado sin delegar todo el ejercicio al asistente.

## Punto de partida

El proyecto está en [`project/`](project/README.md). Su módulo `src/pois.py` contiene una función para construir una entidad GeoJSON de tipo `Point`. No utiliza librerías externas.

Antes de empezar, copia `project/` a un directorio fuera del repositorio de la guía y abre esa copia como espacio de trabajo del asistente. No abras esta carpeta ni la raíz de la guía en el asistente. El README de este ejercicio contiene las tareas sugeridas con IA; el README dentro de la copia describe el proyecto. Proporciona las instrucciones del ejercicio explícitamente al asistente cuando las necesite. Sigue el [procedimiento común de copia independiente](../README.md#copia-independiente-obligatoria).

## Ejercicios

### A. Comprender antes de cambiar

Pide al asistente que explique:

- qué argumentos recibe la función;
- en qué orden se guardan las coordenadas en GeoJSON;
- qué validaciones realiza y qué entradas podrían quedar sin cubrir (por ejemplo, un nombre que no sea texto);
- qué comportamiento verifican las pruebas existentes.

Pídele que no modifique archivos en esta primera interacción. Contrasta la explicación con el código y la especificación de [RFC 7946](https://www.rfc-editor.org/rfc/rfc7946).

### B. Autocompletado

Escribe tú una pequeña función o prueba y utiliza el autocompletado para completarla. Revisa el resultado línea a línea; acepta solo lo que entiendas y puedas justificar.

### C. Encargar una tarea acotada

Solicita una función `crear_coleccion(puntos)` que agrupe varios puntos en una `FeatureCollection` ([RFC 7946, sección 3.3](https://www.rfc-editor.org/rfc/rfc7946#section-3.3)). Antes de aceptar el cambio, acuerda estos criterios:

- devuelve `{"type": "FeatureCollection", "features": [...]}` con los puntos en el orden recibido;
- una lista vacía produce una colección válida sin entidades;
- no modifica las entidades recibidas;
- rechaza elementos que no sean entidades `Feature`; decide qué excepción se produce y documéntalo en las pruebas;
- reutiliza `crear_punto` en las pruebas en lugar de duplicar la construcción de entidades;
- no cambia el comportamiento de `crear_punto`;
- añade pruebas para casos normales, lista vacía y entradas inválidas.

### D. Verificación

Instala pytest si aún no está disponible y ejecuta desde `project/`:

```bash
python -m pip install pytest
python -m pytest
```

Revisa los cambios con `git diff -- .` desde `project/`. Si una prueba falla, pide al asistente que explique el fallo antes de aceptar una corrección.

## Criterios de finalización

- Puedes explicar el código y el orden de las coordenadas.
- Las pruebas cubren casos normales, límites y entradas inválidas.
- El cambio es pequeño y el diff no contiene modificaciones ajenas a la tarea.
- Has ejecutado las pruebas localmente.

## Preguntas de reflexión

- ¿Qué contexto hizo mejorar la respuesta?
- ¿Qué error detectaste al revisar el código?
- ¿Habría sido mejor usar chat, autocompletado o un agente para cada tarea?
