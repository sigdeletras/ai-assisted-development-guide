# Itinerario de aprendizaje

Este itinerario organiza la guía por competencias. No sustituye al [mapa de contenidos](mapa-contenidos.md), que permite consultar temas concretos, ni obliga a recorrer todos los niveles en orden: puedes acudir directamente a una referencia cuando la necesites.

## Cómo utilizar el itinerario

1. Identifica qué necesitas hacer, no solo qué herramienta quieres aprender.
2. Empieza en el nivel cuyo objetivo se aproxime a tu experiencia.
3. Realiza la práctica asociada y comprueba sus criterios de salida.
4. Avanza cuando puedas explicar las decisiones tomadas y aportar evidencias de verificación.
5. Consulta el [mapa de contenidos](mapa-contenidos.md) y el [glosario](glosario.md) cuando necesites profundizar en un concepto.

Los niveles describen competencias acumulativas, pero no son certificaciones ni requisitos para consultar el resto de la documentación.

## Niveles

### Nivel 1 · Iniciación práctica

**Objetivo:** utilizar un asistente para completar una tarea pequeña y verificable sin delegar la responsabilidad de revisión.

**Aprenderás a:**
- formular un objetivo y criterios de aceptación sencillos;
- proporcionar contexto relevante y autorizado;
- solicitar explicaciones o un plan breve antes de un cambio no trivial;
- revisar el diff y ejecutar las comprobaciones disponibles;
- reconocer cuándo no puedes validar una propuesta.

**Práctica principal:** [Laboratorio 01 · Primer contacto](../laboratorio/01-primer-contacto/README.md).

**Criterio de salida:** puedes explicar qué cambió, por qué era necesario, qué archivos se modificaron y qué pruebas o comprobaciones ejecutaste.

### Nivel 2 · Desarrollo estructurado

**Objetivo:** aplicar IA en proyectos con alcance, estructura y verificación explícitos.

**Aprenderás a:**
- transformar requisitos en tareas pequeñas;
- reconocer la estructura de un proyecto y sus dependencias;
- establecer una línea base antes de modificar un repositorio existente;
- utilizar Git para revisar cambios y mantenerlos acotados;
- incorporar pruebas y criterios de aceptación.

**Prácticas principales:**
- [Laboratorio 02 · Proyecto nuevo](../laboratorio/02-proyecto-nuevo/README.md).
- [Laboratorio 03 · Proyecto existente](../laboratorio/03-proyecto-existente/README.md).

**Criterio de salida:** puedes iniciar o analizar un proyecto, identificar cómo se ejecuta y prueba, y producir un cambio acotado que pueda revisarse y reproducirse.

### Nivel 3 · Configuración del entorno

**Objetivo:** configurar el entorno de trabajo según las necesidades del proyecto, sin habilitar mecanismos por defecto.

**Aprenderás a:**
- distinguir instrucciones persistentes, reglas por ámbito y configuración de la herramienta;
- decidir cuándo conviene usar skills, hooks, agentes o MCP;
- aplicar permisos mínimos y mantener la supervisión humana;
- evitar duplicidades entre archivos de instrucciones;
- comprobar que una configuración se carga y tiene el efecto esperado.

**Práctica principal:** [Laboratorio 04 · Configuración del entorno de IA](../laboratorio/04-configuracion-entorno-ia/README.md).

**Criterio de salida:** puedes justificar cada mecanismo configurado, verificar su funcionamiento y explicar sus límites. No necesitas crear todos los tipos de archivo ni activar todas las capacidades.

### Nivel 4 · Ingeniería asistida

**Objetivo:** integrar la IA en un flujo de ingeniería trazable desde la especificación hasta la verificación.

**Aprenderás a:**
- definir una funcionalidad y sus criterios de aceptación antes de implementarla;
- revisar y confirmar un plan de trabajo;
- dividir la implementación en incrementos comprobables;
- relacionar requisitos, historias de usuario, casos de uso, tareas y pruebas;
- registrar decisiones de arquitectura (ADR) y mantener la documentación del ciclo de vida;
- evaluar el cambio mediante pruebas, revisión humana y evidencias.

**Práctica principal:** [Laboratorio 05 · Desarrollo de una funcionalidad con IA](../laboratorio/05-desarrollo-funcionalidad-ia/README.md).

**Criterio de salida:** puedes relacionar el objetivo y sus criterios de aceptación con las decisiones, los cambios realizados y las pruebas ejecutadas.

**Estado de la guía:** el laboratorio 05 cubre el flujo de especificación, planificación, implementación incremental y verificación. Las prácticas específicas de historias de usuario, casos de uso, ADR y documentación completa del ciclo de vida siguen siendo ampliaciones pendientes del [roadmap](../ROADMAP.md).

### Nivel 5 · Gobierno y escalado

**Objetivo:** evaluar y gobernar el uso de asistentes y agentes en un equipo o en proyectos con requisitos de seguridad y calidad.

**Aprenderás a:**
- valorar riesgos de privacidad, exposición de secretos y permisos;
- definir límites de autonomía y controles de revisión;
- comparar calidad, utilidad, coste y tiempo de un flujo asistido;
- establecer criterios de adopción, evaluación y mejora continua;
- documentar decisiones, limitaciones e incidencias;
- distinguir capacidades anunciadas de resultados verificados en el entorno real.

**Prácticas previstas:** evaluación de calidad, coste y utilidad; controles de seguridad y automatización; registro de resultados y decisiones.

**Criterio de salida:** puedes justificar una decisión de adopción con criterios verificables, riesgos identificados, controles proporcionados y limitaciones documentadas.

**Estado de la guía:** este nivel es una orientación de desarrollo futuro. Sus prácticas de evaluación y gobierno deben completarse según las propuestas del [roadmap](../ROADMAP.md).

## Vista resumida

| Nivel | Competencia | Laboratorios principales | Estado |
| --- | --- | --- | --- |
| 1 | Tareas pequeñas y verificables | 01 | Disponible |
| 2 | Proyectos, requisitos, Git y pruebas | 02 y 03 | Disponible; el laboratorio 03 sigue sujeto a validación según el roadmap |
| 3 | Configuración consciente del entorno | 04 | Disponible |
| 4 | Flujo de ingeniería trazable | 05 | Parcial; falta ampliar documentación del ciclo de vida |
| 5 | Gobierno, evaluación y escalado | Ampliaciones futuras | Pendiente de desarrollar |

## Rutas según experiencia

- **Primera experiencia con asistentes:** empieza por el nivel 1 y continúa al nivel 2.
- **Desarrollador con experiencia:** revisa los criterios de salida de los niveles 1 y 2; si ya los cumples, utiliza los laboratorios como referencia y avanza al nivel 3 o 4 según tu necesidad.
- **Responsable técnico o de equipo:** consulta los niveles 3 y 5, manteniendo como base los controles de revisión y calidad del nivel 2.
- **Necesidad puntual:** utiliza el [mapa de contenidos](mapa-contenidos.md) sin recorrer el itinerario completo.

## Recursos transversales

- [Mapa de contenidos](mapa-contenidos.md): índice temático de conceptos y prácticas.
- [Glosario](glosario.md): definiciones breves.
- [Herramientas de desarrollo asistido por IA](herramientas-desarrollo-ia.md): categorías y ejemplos representativos.
- [Referencias de herramientas](referencias-herramientas.md): documentación oficial y equivalencias.
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md): riesgos y medidas de control.
- [Roadmap](../ROADMAP.md): ampliaciones pendientes; no equivale a contenido ya implementado.
