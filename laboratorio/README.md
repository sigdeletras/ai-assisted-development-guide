# Laboratorio de desarrollo asistido por IA

Cinco ejercicios para practicar desarrollo asistido con un proyecto geográfico sencillo en Python. Los métodos se pueden trasladar a otros lenguajes.

Consulta el [itinerario de aprendizaje](../docs/itinerario-aprendizaje.md) para ver las competencias de cada nivel.

## Ejercicios

| Laboratorio | Nivel | Objetivo |
| --- | --- | --- |
| [01 · Primer contacto](01-primer-contacto/README.md) | 1 | Practicar chat, autocompletado y cambios pequeños. |
| [02 · Proyecto nuevo](02-proyecto-nuevo/README.md) | 2 | Convertir requisitos en un proyecto con pruebas y API REST. |
| [03 · Proyecto existente](03-proyecto-existente/README.md) | 2 | Analizar el repositorio y establecer una línea base. |
| [04 · Configuración del entorno](04-configuracion-entorno-ia/README.md) | 3 | Configurar y validar instrucciones, reglas, skills y permisos. |
| [05 · Desarrollar una funcionalidad](05-desarrollo-funcionalidad-ia/README.md) | 4 | Planificar, implementar por incrementos y verificar. |

La secuencia recomendada es 03 → 04 → 05. Los laboratorios 01 y 02 son prácticas independientes; los demás también pueden realizarse por separado si ya se dispone del diagnóstico o configuración necesarios.

## Ejercicio y proyecto son espacios distintos

- **README del ejercicio:** instrucciones, tareas, criterios y referencias. Se mantiene en este repositorio.
- **Proyecto de trabajo:** código, pruebas y configuración que se modifican durante la práctica.

Abre como espacio de trabajo únicamente el proyecto, no la raíz de esta guía. Así se evita que el asistente confunda instrucciones, modifique documentación por error o ejecute comandos en el repositorio equivocado.

## Copia independiente obligatoria

Antes de utilizar un asistente, copia el proyecto fuera del repositorio de la guía. Por ejemplo:

```bash
mkdir -p ~/labs
cp -r laboratorio/03-proyecto-existente/project ~/labs/poi-app
cd ~/labs/poi-app
git init
git add .
git commit -m "Estado inicial del proyecto de práctica"
```

Si la copia ya contiene Git, revisa su estado e historial; no la reinicialices ni sobrescribas cambios existentes. Para el laboratorio 02, crea un directorio nuevo.

Usa la misma copia en los laboratorios 03–05 si quieres mantener la secuencia. Si un laboratorio ofrece otro proyecto de referencia, copia ese proyecto. Proporciona al asistente las instrucciones del ejercicio explícitamente cuando las necesite; no abras la guía como espacio de trabajo.

## Requisitos

- Python 3.11 o posterior.
- Git.
- Un editor o asistente aprobado para el proyecto.
- Para las pruebas del laboratorio 01: `python -m pip install pytest`.

No se necesitan servicios externos para el primer ejercicio. Las dependencias adicionales se incorporan cuando el proyecto las requiere.

## Método de trabajo

1. Define el objetivo y las restricciones.
2. Pide un plan para cambios no triviales.
3. Haz un cambio pequeño cada vez.
4. Revisa el diff y entiende las modificaciones.
5. Ejecuta las pruebas y registra lo que no hayas podido verificar.

No uses credenciales, datos de clientes ni información confidencial sin autorización. El asistente no sustituye la revisión ni la responsabilidad del desarrollador.

Más información: [Diseño de ejercicios](../docs/estructura-ejercicios.md) · [Seguridad y privacidad](../docs/seguridad-privacidad-ia.md).
