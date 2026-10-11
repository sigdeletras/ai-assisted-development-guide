# Mapa de contenidos de la guía

Este mapa organiza la guía en cinco módulos temáticos consultables. No define un curso obligatorio ni implica que todos los contenidos estén desarrollados: distingue los documentos existentes de las propuestas pendientes y utiliza el laboratorio como espacio común de práctica.

## Cómo utilizar el mapa

- **Documentación existente:** enlaza a contenidos que ya están en el repositorio.
- **Propuesta pendiente:** indica un tema que conviene desarrollar o revisar; no equivale a contenido publicado.
- **Laboratorio:** enlaza a escenarios existentes que pueden servir como punto de partida. La correspondencia no significa que el escenario cubra ya todos los conceptos del módulo.

La guía debe explicar conceptos, criterios de decisión, límites y riesgos. Las instrucciones operativas y el código de práctica corresponden al [laboratorio](../laboratorio/README.md). Para diseñar ejercicios, aplica la convención de [Diseño de ejercicios de la guía](estructura-ejercicios.md).

## Módulo 1. Fundamentos del desarrollo asistido

**Objetivo:** aprender un flujo de trabajo fiable antes de configurar mecanismos avanzados.

### Contenidos

- Cómo encajar el asistente en el ciclo de desarrollo: comprender, planificar, implementar, verificar y revisar.
- Cómo formular tareas concretas y aportar contexto relevante.
- Diferencias prácticas entre chat, autocompletado y modos de agente.
- Descomposición de tareas, criterios de aceptación e iteración basada en evidencias.
- Revisión del diff, pruebas y responsabilidad del desarrollador.

**Documentación existente**
- [Primeros pasos con asistentes de programación](primeros-pasos.md).
- [Referencias de herramientas](referencias-herramientas.md), para consultar documentación oficial de cada producto.

**Propuesta pendiente**
- Añadir una explicación comparativa de los modos de interacción, sin convertirla en un catálogo de marcas.
- Incorporar un ejercicio sobre cómo mejorar una petición ambigua y definir criterios de aceptación.

**Laboratorio relacionado**
- [01 · Primer contacto](../laboratorio/01-primer-contacto/README.md).
- [02 · Proyecto nuevo](../laboratorio/02-proyecto-nuevo/README.md).
- [03 · Proyecto existente](../laboratorio/03-proyecto-existente/README.md).

## Módulo 2. Contexto e instrucciones del entorno

**Objetivo:** hacer que el asistente trabaje de acuerdo con las convenciones y restricciones del proyecto, sin acumular configuración innecesaria.

### Contenidos

- Contexto: qué información aportar, cómo acotarla y cómo evitar contexto irrelevante o sensible.
- Archivos de instrucciones del repositorio, por ejemplo `AGENTS.md`, `CLAUDE.md` y los mecanismos equivalentes de cada producto.
- Reglas de proyecto y configuración del editor o herramienta, incluidos archivos como `settings.json` cuando corresponda.
- Diferencias entre instrucciones, reglas, skills y configuración.
- Diseño de instrucciones pequeñas, comprobables y mantenibles.
- Precedencia, alcance y posibles conflictos entre instrucciones locales, de usuario y de organización, según la herramienta.

**Documentación existente**
- [Referencias de herramientas](referencias-herramientas.md), con enlaces a documentación oficial de los productos.
- [Diseño de ejercicios de la guía](estructura-ejercicios.md), para enlazar la práctica con el laboratorio.

**Propuesta pendiente**
- Crear un apartado agnóstico sobre instrucciones persistentes y reglas.
- Añadir una tabla comparativa de los mecanismos específicos por producto, respaldada por documentación oficial vigente.
- Añadir criterios para decidir cuándo un archivo de instrucciones aporta valor y cómo comprobar que se aplica.

**Laboratorio relacionado**
- [03 · Proyecto existente](../laboratorio/03-proyecto-existente/README.md), como escenario potencial para introducir instrucciones de proyecto. La práctica específica queda pendiente de documentar.

## Módulo 3. Agentes, herramientas y automatización

**Objetivo:** comprender qué puede delegarse a un agente, qué herramientas puede utilizar y cómo limitar sus acciones.

### Contenidos

- Diferencias entre chat, modo de agente, agentes especializados y subagentes.
- Planificación, ejecución por etapas, delegación y revisión de resultados.
- Herramientas y permisos: lectura, edición de archivos, terminal, red y servicios externos.
- Skills: instrucciones reutilizables y criterios para decidir cuándo crearlas.
- Hooks: automatización de acciones asociadas a eventos y sus riesgos.
- MCP: conexión con herramientas y fuentes de datos externas, permisos y límites de confianza.
- Configuración de agentes y diferencias de implementación entre proveedores.

**Documentación existente**
- [Referencias de herramientas](referencias-herramientas.md), como punto de entrada a las fuentes oficiales de cada producto.

**Propuesta pendiente**
- Desarrollar los conceptos de agentes, skills, hooks y MCP por separado, evitando tratarlos como mecanismos equivalentes.
- Explicar el ciclo de una tarea delegada y los puntos de control humano.
- Incorporar ejemplos mínimos y seguros, además de criterios para habilitar o denegar herramientas.

**Laboratorio relacionado**
- [03 · Proyecto existente](../laboratorio/03-proyecto-existente/README.md), como base potencial para practicar exploración y cambios controlados. Los ejercicios específicos de agentes, skills, hooks y MCP están pendientes.

## Módulo 4. Ingeniería del software y seguridad

**Objetivo:** integrar la asistencia de IA en un proceso de ingeniería verificable y reducir los riesgos técnicos y de seguridad.

Este módulo reúne dos bloques relacionados, pero conviene mantenerlos diferenciados al desarrollar la documentación.

### 4A. Calidad y flujo de ingeniería

- Git, commits pequeños, ramas y worktrees cuando aporten aislamiento.
- Pruebas unitarias, de integración y de caracterización.
- Linters, tipado, análisis estático y CI.
- Refactorización segura y preservación del comportamiento.
- Harness engineering: preparar el repositorio, las herramientas y los bucles de verificación para que el agente pueda trabajar con límites claros.
- Spec-Driven Development: explicitar requisitos, restricciones y criterios verificables antes de implementar.
- Documentación técnica y decisiones de arquitectura.

**Documentación existente**
- [Primeros pasos](primeros-pasos.md), para el flujo básico de revisión y pruebas.
- [Laboratorio](../laboratorio/README.md), con escenarios de proyecto nuevo y proyecto existente.

**Propuesta pendiente**
- Desarrollar harness engineering y Spec-Driven Development como enfoques complementarios, explicando cuándo ayudan y qué coste introducen.
- Añadir una práctica que conecte requisitos, pruebas, implementación y revisión.

### 4B. Seguridad, privacidad y control de cambios

- Protección de secretos, credenciales, datos personales y código confidencial.
- Políticas de uso, retención de datos y condiciones contractuales de los proveedores.
- Permisos mínimos, sandboxing y aprobación de acciones con efectos externos.
- Riesgos de prompt injection en repositorios, documentación, issues y contenido recuperado.
- Riesgos de comandos destructivos, dependencias, exfiltración y acceso a servicios.
- Revisión humana, trazabilidad y respuesta ante incidentes.
- Diferencias entre las garantías declaradas por el proveedor y los controles aplicados en el entorno propio.

**Documentación existente**
- [Primeros pasos](primeros-pasos.md), con precauciones iniciales sobre datos, permisos y revisión.
- [Laboratorio](../laboratorio/README.md), con la regla de no utilizar secretos ni datos confidenciales reales.

**Propuesta pendiente**
- Crear una guía de seguridad práctica con una matriz de riesgos, controles y evidencias de verificación.
- Distinguir controles del proveedor, controles del editor/agente y controles del repositorio o la organización.
- Añadir escenarios de prueba seguros para revisar permisos e instrucciones potencialmente maliciosas.

## Módulo 5. Gobierno, evaluación y mejora continua

**Objetivo:** decidir cómo adoptar y mantener el desarrollo asistido por IA en un equipo u organización con criterios explícitos.

### Contenidos

- Selección de modelos y herramientas según la tarea, calidad, coste, latencia, privacidad y capacidades.
- Evaluación mediante tareas representativas y resultados verificables, no solo impresiones subjetivas.
- Métricas útiles: calidad, defectos, tiempo de revisión, retrabajo, coste y mantenimiento.
- Políticas de uso, responsabilidades, niveles de autorización y requisitos contractuales.
- Gestión de versiones de modelos, cambios de comportamiento y vigencia de configuraciones.
- Trazabilidad de decisiones, configuración y cambios generados.
- Formación del equipo y revisión periódica de las prácticas adoptadas.

**Documentación existente**
- [Criterios de la guía](../README.md#criterios-de-la-guía), como principios editoriales generales.
- [Referencias de herramientas](referencias-herramientas.md), para consultar información oficial específica de producto.

**Propuesta pendiente**
- Definir una plantilla para evaluar herramientas y modelos con tareas representativas del equipo.
- Añadir una lista de comprobación para adopción organizativa: seguridad, privacidad, permisos, costes, calidad y supervisión.
- Documentar cómo revisar periódicamente las recomendaciones y registrar su fecha y fuentes.

**Laboratorio relacionado**
- Los tres proyectos del [laboratorio](../laboratorio/README.md) pueden utilizarse como conjunto de tareas comparables para una evaluación inicial. Antes de publicar una metodología de evaluación, habrá que definir protocolo, métricas y criterios de comparación.

## Ejes transversales

Estos criterios deben aparecer en los módulos pertinentes, no limitarse a una única sección:

- **Seguridad y responsabilidad:** datos permitidos, permisos, revisión humana y límites de autonomía.
- **Calidad y verificación:** criterios de aceptación, pruebas, revisión del diff y evidencia reproducible.
- **Independencia de proveedor:** explicar primero el principio general y después las variantes específicas, con enlaces oficiales.
- **Mantenimiento:** indicar qué información cambia con frecuencia y requiere revisión.
- **Práctica:** enlazar al laboratorio solo cuando exista un escenario real que permita completar y verificar el ejercicio.

## Referencias de producto y fuentes

Las páginas específicas de cada herramienta deben mantenerse agrupadas en [Referencias de herramientas](referencias-herramientas.md), no repartidas como listas duplicadas por los módulos. Cuando se desarrolle un concepto, enlaza directamente a la fuente oficial pertinente y comprueba su vigencia.

Este mapa es una propuesta de organización editorial incorporada como documento de planificación. No implica que los contenidos marcados como pendientes estén desarrollados, ni que los ejercicios potenciales estén ya implementados o validados.
