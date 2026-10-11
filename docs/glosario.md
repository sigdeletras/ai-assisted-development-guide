# Glosario de desarrollo asistido por IA

Este glosario reúne los conceptos básicos necesarios para comprender el desarrollo de software asistido por inteligencia artificial, la configuración de asistentes y agentes, y las metodologías de ingeniería relacionadas.

Se prioriza la terminología inglesa utilizada en la documentación técnica. Las traducciones al español se incluyen cuando ayudan a comprender el concepto.

Las denominaciones y los mecanismos concretos pueden variar entre herramientas y proveedores. Cuando no exista una equivalencia directa, debe consultarse la documentación oficial correspondiente.

## 1. Fundamentos de inteligencia artificial

| Término | Definición |
| --- | --- |
| **Artificial Intelligence (AI)** — Inteligencia artificial (IA) | Campo de la informática que desarrolla sistemas capaces de realizar tareas asociadas a capacidades como el razonamiento, la percepción, la generación de contenido o la toma de decisiones. |
| **Large Language Model (LLM)** — Modelo de lenguaje grande | Modelo de IA entrenado para procesar y generar lenguaje. Los asistentes de programación utilizan LLM para comprender peticiones, analizar código y proponer soluciones. |
| **Generative AI** — IA generativa | Sistemas de IA capaces de generar contenido nuevo, como texto, código, imágenes o datos estructurados. |
| **Prompt** — Instrucción o petición | Entrada proporcionada al modelo para solicitar una respuesta o una acción. Su precisión y el contexto disponible influyen en el resultado. |
| **Token** | Unidad de texto o información que el modelo procesa. No equivale necesariamente a una palabra ni a un carácter. Los tokens influyen en los límites de contexto y en determinados costes de uso. |
| **Context** — Contexto | Información disponible para el modelo durante una interacción: instrucciones, mensajes, fragmentos de código, documentación y resultados de herramientas, entre otros elementos. |
| **Context Window** — Ventana de contexto | Cantidad máxima de tokens que un modelo puede procesar dentro de una interacción según los límites aplicables. No debe confundirse con la memoria persistente del proyecto. |
| **Hallucination** — Alucinación | Respuesta incorrecta, inventada o no respaldada por evidencias que el modelo presenta como plausible. En programación puede manifestarse en API inexistentes, dependencias incorrectas o explicaciones falsas. |
| **Context Engineering** — Ingeniería del contexto | Diseño y gestión de la información, las instrucciones y los recursos que recibe el modelo para mejorar la calidad, la pertinencia y la fiabilidad de sus resultados. |
| **Reasoning Effort** — Esfuerzo de razonamiento | Parámetro disponible en algunos modelos o herramientas que permite ajustar los recursos dedicados al razonamiento. Puede afectar a la profundidad del análisis, la latencia y el consumo de tokens; los valores y sus efectos dependen del modelo y del proveedor. |

## 2. Asistentes, agentes y herramientas

| Término | Definición |
| --- | --- |
| **AI Coding Assistant** — Asistente de programación con IA | Herramienta que ayuda a comprender, escribir, modificar, documentar o probar código. Puede funcionar mediante chat, autocompletado o edición integrada en el entorno de desarrollo. |
| **Agent** — Agente | Sistema que utiliza un modelo para perseguir un objetivo mediante un ciclo de interpretación, planificación, uso de herramientas y evaluación de resultados. Su autonomía depende de las capacidades y permisos disponibles. |
| **Subagent** — Subagente | Agente delegado para realizar una tarea específica dentro de un trabajo más amplio. Puede disponer de instrucciones, contexto y herramientas delimitados. |
| **Multi-Agent System** — Sistema multiagente | Sistema en el que varios agentes colaboran o se reparten tareas para alcanzar un objetivo. La coordinación puede ser centralizada o distribuida y requiere gestionar dependencias, intercambio de resultados, contexto, conflictos y validación. |
| **Agentic Coding** — Programación agéntica | Forma de desarrollo en la que un agente puede realizar varios pasos de trabajo, utilizar herramientas y modificar código para alcanzar un objetivo, dentro de los límites establecidos. |
| **IDE (Integrated Development Environment)** — Entorno de desarrollo integrado | Aplicación que reúne herramientas para editar, ejecutar y depurar código. Algunos IDE incorporan asistentes y agentes de IA. |
| **CLI (Command-Line Interface)** — Interfaz de línea de comandos | Interfaz que permite interactuar con una herramienta mediante comandos de texto. Algunos agentes de programación pueden ejecutarse desde una CLI. |
| **Git Worktree** — Árbol de trabajo de Git | Mecanismo de Git para mantener varios directorios de trabajo vinculados al mismo repositorio, normalmente asociados a ramas o revisiones distintas. Permite trabajar en tareas paralelas sin tener que cambiar continuamente de rama en un único directorio. |
| **Tool Calling** — Llamada a herramientas | Capacidad del modelo para solicitar la ejecución de una herramienta disponible, como consultar archivos, ejecutar pruebas o llamar a una API. La ejecución efectiva depende del sistema que la controla. |
| **Human-in-the-Loop (HITL)** — Intervención humana | Enfoque en el que una persona supervisa, valida o autoriza decisiones y acciones relevantes del sistema de IA. |

## 3. Configuración y gobierno del entorno de IA

| Término | Definición |
| --- | --- |
| **Instructions** — Instrucciones | Indicaciones que orientan el comportamiento del asistente o agente, como las convenciones del proyecto, los objetivos, las restricciones y los criterios de calidad. |
| **Rules** — Reglas | Instrucciones que se aplican bajo un alcance o unas condiciones determinadas, por ejemplo, a ciertos directorios, lenguajes o tipos de archivo. Su activación depende de la herramienta. |
| **AGENTS.md** | Archivo de instrucciones para agentes de programación que permite documentar convenciones, comandos, arquitectura y restricciones de un proyecto. Su lectura y su alcance dependen de la herramienta y de su implementación. |
| **CLAUDE.md** | Archivo utilizado por Claude Code para proporcionar instrucciones persistentes. Es un mecanismo específico de ese producto, no un nombre genérico para todos los asistentes. |
| **Settings** — Ajustes o configuración | Parámetros que controlan el funcionamiento de una herramienta, incluidos los modelos seleccionados, los permisos, las integraciones y las preferencias de ejecución. |
| **Skill** — Capacidad o procedimiento reutilizable | Conjunto organizado de instrucciones y, cuando corresponda, recursos auxiliares que describe cómo realizar una tarea recurrente. Puede activarse según la petición y las reglas de la herramienta. |
| **Hook** — Gancho o disparador de evento | Mecanismo que ejecuta una acción cuando ocurre un evento definido en el ciclo de trabajo de una herramienta. Puede utilizarse para realizar comprobaciones o aplicar controles. |
| **MCP (Model Context Protocol)** | Protocolo que permite conectar aplicaciones de IA con herramientas y fuentes de información mediante una interfaz común. No implica por sí mismo que cualquier conexión sea segura ni que el acceso esté autorizado. |
| **Harness** — Entorno de ejecución y control | Conjunto de componentes que rodean al modelo y permiten gestionar su ejecución, contexto, herramientas, permisos, estado y resultados. El significado concreto depende del ámbito y del uso del término. |
| **Harness Engineering** — Ingeniería del entorno de control | Diseño y mejora de la infraestructura, las restricciones, las comprobaciones y los mecanismos de evaluación que permiten que los agentes trabajen de forma controlada y verificable. |
| **Permission Model** — Modelo de permisos | Conjunto de reglas que determina qué archivos, comandos, herramientas, servicios o acciones puede utilizar un asistente o agente. |
| **Sandbox** — Entorno aislado | Entorno de ejecución con restricciones destinadas a limitar el acceso a recursos del sistema. Su nivel de aislamiento depende de la implementación. |

## 4. Especificación y diseño del software

| Término | Definición |
| --- | --- |
| **Requirement** — Requisito | Necesidad, condición o capacidad que debe satisfacer el sistema. Puede ser funcional o no funcional. |
| **User Story** — Historia de usuario | Descripción breve de una necesidad desde la perspectiva de una persona usuaria o de un actor del sistema. Suele acompañarse de criterios de aceptación. |
| **Use Case** — Caso de uso | Descripción de cómo un actor interactúa con el sistema para alcanzar un objetivo, incluyendo las condiciones y los posibles flujos de interacción relevantes. |
| **Acceptance Criteria** — Criterios de aceptación | Condiciones observables y verificables que permiten determinar si una funcionalidad satisface los requisitos acordados. |
| **Specification** — Especificación | Descripción estructurada del comportamiento esperado, las restricciones y las condiciones que debe cumplir una solución. |
| **SDD (Spec-Driven Development)** — Desarrollo guiado por especificaciones | Enfoque que utiliza especificaciones explícitas como referencia para planificar, implementar y validar cambios de software. La especificación puede evolucionar durante el desarrollo. |
| **Plan** — Plan de implementación | Secuencia propuesta de pasos, archivos afectados, decisiones técnicas y comprobaciones necesarias para realizar un cambio. Debe revisarse antes de autorizar tareas de cierta complejidad. |
| **ADR (Architecture Decision Record)** — Registro de decisión arquitectónica | Documento breve que registra una decisión arquitectónica relevante, el contexto que la motiva, las alternativas consideradas y sus consecuencias. |
| **Scope** — Alcance | Límites de una tarea o proyecto: qué se incluye, qué queda fuera y qué restricciones deben respetarse. |
| **Assumption** — Supuesto | Condición que se considera cierta provisionalmente, pero que necesita confirmación cuando puede afectar al diseño o al resultado. |

## 5. Seguridad, privacidad y fiabilidad

| Término | Definición |
| --- | --- |
| **Prompt Injection** — Inyección de instrucciones | Ataque que intenta manipular el comportamiento del modelo mediante instrucciones maliciosas incluidas en una petición, un archivo, una página web u otro contenido que procesa. |
| **Least Privilege** — Mínimo privilegio | Principio de seguridad según el cual una herramienta o agente debe recibir únicamente los permisos necesarios para realizar su tarea. |
| **Secret** — Secreto | Información sensible utilizada para autenticar o autorizar el acceso a sistemas, como contraseñas, claves API y tokens de acceso. No debe incluirse en prompts ni en archivos versionados. |
| **Data Retention** — Retención de datos | Periodo y condiciones durante los cuales un proveedor conserva datos procesados por un servicio. Depende del producto, el plan, la función y las condiciones aplicables. |
| **ZDR (Zero Data Retention)** — Retención cero de datos | Compromiso o modalidad según la cual determinados datos no se conservan después de su procesamiento, dentro del alcance y las excepciones acordados. Debe verificarse para el servicio concreto. |
| **Human Review** — Revisión humana | Inspección y validación por una persona de los cambios, las decisiones o los resultados generados por la IA antes de aceptarlos o utilizarlos. |
| **Verification** — Verificación | Comprobación mediante evidencias de que un cambio cumple los criterios definidos. Puede incluir pruebas, análisis estático, revisión del código y comprobaciones manuales. |

## 6. Principios de uso

- Comprender un concepto no implica que todas las herramientas lo implementen de la misma forma.
- Un archivo de instrucciones, una skill, un hook y un agente cumplen funciones distintas; no deben tratarse como mecanismos intercambiables.
- La IA puede proponer código, planes y pruebas, pero sus resultados deben verificarse.
- Los permisos deben limitarse a las necesidades reales de la tarea.
- La información que se comparte con una herramienta debe estar autorizada según su clasificación, las políticas de la organización y las condiciones del proveedor.
- Las configuraciones y equivalencias entre productos deben comprobarse en la documentación oficial vigente.

## Referencias dentro de la guía

- [Primeros pasos con asistentes de programación](primeros-pasos.md)
- [Referencias de herramientas y documentación](referencias-herramientas.md)
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md)
- [Mapa de contenidos](mapa-contenidos.md)
- [Laboratorio 04: configuración del entorno de IA](../laboratorio/04-configuracion-entorno-ia/README.md)
- [Laboratorio 05: desarrollo de una funcionalidad con IA](../laboratorio/05-desarrollo-funcionalidad-ia/README.md)
