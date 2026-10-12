# Laboratorio de desarrollo asistido por IA

Este laboratorio acompaña a la guía conceptual con ejercicios pequeños y verificables. Usa Python como punto de partida y un dominio geográfico sencillo —puntos de interés y GeoJSON— para practicar técnicas que se pueden trasladar a otros lenguajes y proyectos.

Consulta el [itinerario de aprendizaje](../docs/itinerario-aprendizaje.md) para conocer las competencias y los criterios de salida asociados a los laboratorios.

## Proyectos y ejercicios

| Laboratorio | Nivel principal | Objetivo | Referencia |
| --- | --- | --- | --- |
| 01 · Primer contacto | 1 | Practicar chat, autocompletado y cambios pequeños sobre un script existente. | [Abrir ejercicio](01-primer-contacto/README.md) |
| 02 · Proyecto nuevo | 2 | Convertir requisitos en un proyecto estructurado, con pruebas y una API REST. | [Abrir ejercicio](02-proyecto-nuevo/README.md) |
| 03 · Proyecto existente | 2 | Analizar un repositorio, establecer una línea base y decidir qué necesita para trabajar con IA. | [Abrir ejercicio](03-proyecto-existente/README.md) |
| 04 · Configuración del entorno de IA | 3 | Crear y validar instrucciones, rules y skills, y evaluar agentes, hooks y permisos según las necesidades del proyecto. | [Abrir ejercicio](04-configuracion-entorno-ia/README.md) |
| 05 · Desarrollo de una funcionalidad con IA | 4 | Especificar una funcionalidad, revisar y confirmar el plan de la IA, implementar por incrementos y verificar el resultado. | [Abrir ejercicio](05-desarrollo-funcionalidad-ia/README.md) |

Los laboratorios 03, 04 y 05 forman una secuencia recomendada: diagnosticar el proyecto, preparar el entorno y aplicar ese contexto al desarrollo de una funcionalidad. Pueden consultarse por separado si ya se dispone de los resultados de las fases anteriores.

El laboratorio 03 se centra en el diagnóstico y la preparación. El laboratorio 04 parte de ese diagnóstico y se centra en implementar y validar la configuración seleccionada. El laboratorio 05 practica la delegación controlada del desarrollo, con confirmación del plan antes de editar código y revisión humana del resultado. No es obligatorio crear todos los tipos de archivo ni habilitar todas las capacidades.

Los ejercicios describen resultados esperados, no una solución que haya que copiar literalmente. Usa el asistente autorizado por tu organización y compara sus propuestas con los criterios de aceptación.

## Ejercicio y proyecto: dos espacios separados

Cada laboratorio distingue dos espacios con responsabilidades diferentes:

| Espacio | Ubicación | Contenido | Quién lo modifica |
| --- | --- | --- | --- |
| **Ejercicio** | `laboratorio/NN-nombre/README.md` | Objetivos, instrucciones, criterios de evaluación y referencias. | Personas que mantienen la guía. |
| **Proyecto** | `laboratorio/NN-nombre/project/` cuando existe | Código, configuración, README propio, pruebas, dependencias y artefactos generados. | La persona que realiza el ejercicio y el asistente. |

```text
laboratorio/03-proyecto-existente/
├── README.md          ← instrucciones del ejercicio (no es el README del proyecto)
└── project/           ← espacio de trabajo del asistente
    ├── README.md      ← README propio del proyecto
    ├── pyproject.toml
    ├── docs/
    ├── src/
    └── tests/
```

La presencia de `project/` depende del ejercicio:

- El laboratorio 01 incluye un proyecto pequeño para practicar cambios acotados.
- El laboratorio 02 propone crear un proyecto nuevo a partir de requisitos.
- El laboratorio 03 incluye un proyecto existente para practicar el diagnóstico.
- Los laboratorios 04 y 05 incluyen proyectos de referencia para que puedan realizarse de forma independiente; también permiten continuar con una copia propia del proyecto del laboratorio 03.

Comprueba siempre la estructura real enlazada desde cada ejercicio y sigue sus instrucciones. No presupongas que todos los laboratorios contienen la misma estructura de carpetas.

## Aislamiento del espacio de trabajo

Si el asistente trabaja desde la raíz de la guía, puede confundir el README del ejercicio con el del proyecto, cargar instrucciones que no pertenecen al proyecto o modificar la propia guía. Antes de empezar cada laboratorio:

1. Lee las instrucciones del laboratorio en el repositorio de la guía.
2. Identifica el directorio o repositorio que contiene el proyecto de trabajo.
3. Abre ese directorio como espacio de trabajo del asistente; no uses la raíz de la guía como carpeta de trabajo.
4. Mantén las instrucciones del laboratorio como contexto de referencia: proporciónalas explícitamente al asistente cuando las necesite, en lugar de dejar que las busque en la guía.
5. Ejecuta pruebas, instalaciones y cambios exclusivamente en el proyecto de trabajo.
6. Revisa con Git los archivos modificados y los artefactos generados.

Si un laboratorio exige modificar la propia guía, trátalo como una tarea diferente y explícita.

### Copia independiente (recomendada)

Cuando el ejercicio incluya una carpeta `project/`, sigue las instrucciones de su README. Si vas a reutilizar el proyecto en varios laboratorios, copia el proyecto fuera de la guía y crea un repositorio propio:

```bash
cp -r laboratorio/03-proyecto-existente/project ~/labs/poi-app
cd ~/labs/poi-app
git init
git add .
git commit -m "Estado inicial del proyecto de práctica"
```

Así, la línea base, el diff y el estado de Git corresponden solo al proyecto, y la guía no recibe cambios accidentales. Utiliza la misma copia en los laboratorios 03, 04 y 05 cuando quieras seguir la secuencia recomendada.

### Trabajo dentro de la guía

Para ejercicios breves, como el laboratorio 01, puedes abrir directamente su carpeta `project/` como espacio de trabajo si existe. Limita entonces las órdenes de Git a ese directorio (`git status --short -- .`, `git diff -- .`) y no confirmes los cambios del ejercicio en el repositorio de la guía.

## Requisitos iniciales

- Python 3.11 o posterior.
- Git.
- Un editor o asistente de programación aprobado para el proyecto.
- Para ejecutar las pruebas del primer ejercicio: `python -m pip install pytest`.

El primer ejercicio no necesita servicios externos ni dependencias de geografía: utiliza coordenadas y la estructura GeoJSON directamente. FastAPI y otras dependencias se introducirán cuando aporten valor.

La guía define el objetivo de aprendizaje y enlaza al ejercicio pertinente. La plantilla editorial y el flujo para crear o revisar esos ejercicios están descritos en [Diseño de ejercicios de la guía](../docs/estructura-ejercicios.md).

## Método de trabajo

Para cada tarea:

1. Comprueba que el asistente trabaja en el proyecto, no en la raíz de la guía.
2. Comprende el objetivo y las restricciones.
3. Pide al asistente un plan si el cambio no es trivial.
4. Trabaja en una modificación pequeña.
5. Revisa el diff y comprueba que entiendes el código.
6. Ejecuta las pruebas y registra cualquier limitación.

No introduzcas datos reales de clientes, credenciales ni información confidencial. No consideres correcto un cambio solo porque el asistente indique que ha terminado.
