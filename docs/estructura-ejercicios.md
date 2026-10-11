# Diseño de ejercicios de la guía

Este documento define el patrón editorial para conectar los conceptos de la guía con la práctica en el laboratorio. Debe utilizarse al diseñar o revisar apartados que enseñen una habilidad aplicable.

## Principios

- El apartado de la guía explica el concepto, cuándo aplicarlo, sus límites y las precauciones relevantes.
- El bloque de ejercicio propone una práctica breve vinculada al concepto explicado.
- El laboratorio contiene el proyecto, los pasos operativos y el código necesario para realizar la práctica. Dentro de cada laboratorio, el README describe el ejercicio y la subcarpeta `project/` contiene el proyecto de trabajo (consulta [Estructura de un laboratorio](#estructura-de-un-laboratorio)).
- Evita duplicar en la guía los pasos detallados que ya están documentados en el laboratorio.
- No todos los apartados necesitan un ejercicio. En contenidos puramente descriptivos o de referencia, no fuerces una actividad artificial.
- Si todavía no existe un escenario adecuado en el laboratorio, registra la necesidad como pendiente; no inventes un enlace ni des por creado el ejercicio.

## Plantilla estándar

Al final del apartado conceptual, añade el bloque siguiente cuando corresponda:

```markdown
### Ejercicio

- **Objetivo:** habilidad o concepto que se va a practicar.
- **Proyecto del laboratorio:** [Etapa N · Nombre del proyecto](../laboratorio/NN-nombre/README.md).
- **Tarea:** actividad concreta que hay que realizar; consulta el proyecto enlazado para seguir los pasos.
- **Criterio de éxito:** resultado observable que permite comprobar que se ha completado correctamente.
- **Verificación:** pruebas, revisión del diff u otra comprobación necesaria.
```

Adapta el enlace a la ubicación real del documento y al proyecto más adecuado. No uses siempre el mismo proyecto por defecto: selecciona el escenario según la habilidad que se quiere practicar.

### Significado de los campos

- **Objetivo:** expresa el aprendizaje, no una acción genérica como «usar la IA».
- **Proyecto del laboratorio:** apunta directamente al README del ejercicio, no solo a la portada del laboratorio.
- **Tarea:** resume qué se hará sin copiar todas las instrucciones del laboratorio.
- **Criterio de éxito:** define una condición concreta y observable.
- **Verificación:** explica cómo comprobar el resultado; puede integrarse en el criterio de éxito si el ejercicio es muy sencillo.

## Estructura de un laboratorio

Cada laboratorio separa el ejercicio del proyecto sobre el que se trabaja:

- `laboratorio/NN-nombre/README.md`: objetivos, instrucciones, criterios de evaluación y referencias del ejercicio. Es documentación de la guía.
- `laboratorio/NN-nombre/project/`: código, configuración, README propio, pruebas y dependencias del proyecto. Es el espacio de trabajo del asistente.

El README de `project/` describe el proyecto como lo haría un repositorio real: propósito, estructura, instalación y pruebas. No incluye instrucciones del ejercicio ni referencias al laboratorio. Del mismo modo, los archivos del proyecto (código, comentarios, incidencias) no deben dirigirse a quien realiza el ejercicio.

Si un laboratorio no necesita código propio, no crees `project/`; indica en el README qué proyecto se utiliza o dónde debe crearse. El procedimiento para aislar el espacio de trabajo está en el [laboratorio](../laboratorio/README.md#aislamiento-del-espacio-de-trabajo).

## Flujo para desarrollar o actualizar un apartado

1. **Definir el aprendizaje:** concreta qué debe saber hacer el lector al terminar el apartado.
2. **Desarrollar el contenido:** explica el concepto, los casos de uso, los criterios de decisión, las alternativas y las limitaciones.
3. **Elegir el escenario:** identifica qué proyecto existente del laboratorio permite practicar esa habilidad. Si ninguno encaja, define la ampliación necesaria antes de enlazarlo.
4. **Diseñar la tarea:** formula una actividad acotada y coherente con el contenido del apartado.
5. **Añadir el bloque estándar:** completa objetivo, proyecto, tarea, criterio de éxito y verificación.
6. **Preparar o actualizar el laboratorio:** documenta allí los pasos operativos, los archivos implicados, las restricciones y los criterios de aceptación necesarios para realizar el ejercicio.
7. **Comprobar la correspondencia:** verifica que el enlace existe, que el laboratorio permite practicar el concepto y que no hay instrucciones duplicadas o contradictorias.
8. **Revisar seguridad y calidad:** incluye límites de permisos, protección de datos y comprobaciones técnicas cuando proceda.
9. **Registrar lo pendiente:** si falta el escenario o no se ha podido validar el ejercicio, indícalo como pendiente de revisión; no lo presentes como completado.

## Criterios de revisión

Antes de dar por listo un apartado con ejercicio, comprueba:

- El ejercicio practica directamente el concepto explicado.
- El trabajo puede completarse en pasos pequeños y revisables.
- El criterio de éxito es observable y no depende de que el asistente afirme haber terminado.
- La verificación es proporcionada a los riesgos del cambio.
- El enlace apunta al proyecto correcto y existe en el repositorio.
- La guía no duplica los pasos operativos del laboratorio.
- Las instrucciones no requieren compartir secretos, datos confidenciales ni conceder permisos innecesarios.

Esta convención es una pauta editorial. No implica que todos los apartados tengan que incluir un ejercicio ni que los ejercicios descritos estén ya implementados o validados.
