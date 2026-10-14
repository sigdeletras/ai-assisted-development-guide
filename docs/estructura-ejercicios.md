# Diseño de ejercicios

Convención para vincular la guía conceptual con la práctica. No todos los apartados necesitan un ejercicio.

## Principios

- La guía explica el concepto, cuándo aplicarlo y sus límites.
- El laboratorio contiene los pasos, el proyecto y las pruebas.
- Evita duplicar instrucciones operativas.
- Asigna el nivel por la competencia que se practica, no por la herramienta.
- Si no existe un laboratorio adecuado, registra la necesidad como pendiente; no inventes enlaces ni estados.

Consulta el [itinerario de aprendizaje](itinerario-aprendizaje.md) para los objetivos de cada nivel.

## Plantilla

Añade este bloque al final de un apartado conceptual cuando la práctica aporte valor:

```markdown
### Ejercicio

- **Nivel:** 1–5.
- **Objetivo:** habilidad que se practica.
- **Conocimientos previos:** requisitos necesarios o «ninguno».
- **Laboratorio:** [Nombre del ejercicio](../laboratorio/NN-nombre/README.md).
- **Tarea:** resumen breve; los pasos están en el laboratorio.
- **Criterio de éxito:** resultado observable.
- **Verificación:** pruebas o comprobaciones necesarias.
```

Enlaza directamente al README del ejercicio. El criterio de éxito puede incluir la verificación si la práctica es sencilla.

## Estructura de un laboratorio

- `laboratorio/NN-nombre/README.md`: objetivo, pasos, criterios y referencias del ejercicio.
- `laboratorio/NN-nombre/project/`: código, configuración, pruebas y README del proyecto, cuando corresponda.

El README del proyecto describe el software; no contiene instrucciones del ejercicio. Si no hace falta código propio, no crees una carpeta `project/`.

Consulta las reglas de [aislamiento del espacio de trabajo](../laboratorio/README.md#aislamiento-del-espacio-de-trabajo).

## Revisión

Antes de publicar un ejercicio, comprueba que:

- el objetivo y el nivel son coherentes;
- la tarea es concreta y practicable;
- el proyecto y el enlace existen;
- el criterio de éxito es observable;
- la verificación es proporcional al riesgo;
- no se duplican pasos del laboratorio;
- no se requieren secretos, datos confidenciales ni permisos innecesarios;
- el contenido está implementado y validado, o se identifica explícitamente como pendiente.

Este patrón es una pauta editorial, no una obligación de añadir ejercicios a todos los apartados.
