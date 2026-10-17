# Herramientas de desarrollo asistido por IA

Este índice ofrece una selección breve de herramientas representativas para orientarse en el ecosistema de desarrollo asistido por IA. No es un ranking ni un catálogo exhaustivo: los productos, sus capacidades y sus modelos comerciales cambian con rapidez.

La guía prioriza los conceptos y métodos transferibles —especificar tareas, aportar contexto autorizado, revisar cambios y verificar resultados— por encima de las particularidades de un producto.

## Cómo interpretar la selección

Las herramientas se organizan según el entorno de uso: **escritorio**, **cliente de terminal**, **IDE** y **web**. Algunas están disponibles en más de uno; en esos casos se indican las modalidades pertinentes. Las funciones y condiciones pueden variar según la modalidad, el plan y la configuración.

## Escritorio

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **GitHub Copilot app** | Aplicación de escritorio para sesiones con agentes sobre carpetas locales o repositorios conectados, revisión de cambios y creación de pull requests. Es distinta de la extensión de Copilot para IDE y del coding agent de GitHub. | [Documentación](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app) · [Inicio rápido](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app) |
| **OpenAI Codex en la app de escritorio de ChatGPT** | Modalidad de Codex para trabajar con proyectos y archivos locales y para iniciar tareas en la nube. | [Guía de la app](https://developers.openai.com/codex/app) |
| **Cline Desktop** | Aplicación de escritorio de código abierto con sesiones paralelas, tareas programadas y selección de modelos. | [Página de Cline Desktop](https://cline.bot/desktop) · [Descripción general](https://docs.cline.bot/cline-overview) |

## Cliente de terminal (CLI)

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Claude Code** | Agente de programación para explorar repositorios, modificar código y ejecutar herramientas desde terminal y otras interfaces compatibles. | [Documentación](https://code.claude.com/docs/en/overview) · [Inicio rápido](https://code.claude.com/docs/en/quickstart) |
| **OpenAI Codex CLI** | Cliente de línea de comandos para trabajar con Codex desde la terminal. | [Documentación](https://developers.openai.com/codex/cli) · [Repositorio](https://github.com/openai/codex) |
| **Gemini CLI** | Agente de terminal del ecosistema Google para trabajar con código y herramientas. | [Repositorio oficial y documentación](https://github.com/google-gemini/gemini-cli) |
| **OpenCode** | Agente de programación de código abierto, compatible con distintos proveedores y modelos. | [Documentación](https://opencode.ai/docs/) |
| **Aider** | Asistente de programación desde terminal con integración con Git y soporte para distintos modelos. | [Documentación](https://aider.chat/docs/) |
| **Cline CLI** | Agente de terminal con modo interactivo y ejecución sin interfaz para automatizaciones y CI/CD. | [Documentación CLI](https://docs.cline.bot/usage/cli-overview) |

## IDE

### Editores y entornos de desarrollo

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Visual Studio Code** | Editor de código multiplataforma, extensible mediante un amplio ecosistema de extensiones e integraciones. | [Documentación](https://code.visualstudio.com/docs) · [Inicio rápido](https://code.visualstudio.com/docs/getstarted/getting-started) |
| **Cursor** | Editor basado en VS Code con asistencia y agentes integrados en el flujo de edición. | [Documentación](https://cursor.com/docs) · [Inicio rápido](https://cursor.com/docs/get-started/quickstart) |
| **Kiro** | Entorno de desarrollo que promueve un flujo guiado por especificaciones, requisitos y tareas. | [Documentación](https://kiro.dev/docs/) |

### Extensiones para IDE

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **GitHub Copilot para IDE** | Extensión de asistencia de código y chat integrada en VS Code y otros IDE compatibles. | [Documentación de GitHub Copilot](https://docs.github.com/en/copilot) |
| **OpenAI Codex para IDE** | Extensión de Codex para VS Code, Cursor, Windsurf y otros IDE compatibles. | [Documentación](https://developers.openai.com/codex/ide) |
| **Gemini Code Assist** | Asistente de programación para VS Code y otros IDE; ofrece generación y completado de código y asistencia mediante chat. Funciones y condiciones dependen de la edición y el entorno. | [Documentación](https://cloud.google.com/gemini/docs/codeassist/overview) · [IDE compatibles](https://cloud.google.com/gemini/docs/codeassist/supported-languages#supported_ides) |
| **Continue** | Extensión de código abierto para VS Code y JetBrains que integra asistencia de programación con modelos y proveedores configurables. | [Documentación](https://docs.continue.dev/) · [Extensión de VS Code](https://marketplace.visualstudio.com/items?itemName=Continue.continue) |
| **Cline para IDE** | Agente disponible como extensión de VS Code y plugin de JetBrains; también funciona en Cursor, Windsurf, Antigravity y Zed. Neovim es compatible mediante ACP. | [Descripción general y editores compatibles](https://docs.cline.bot/cline-overview) · [Plugin JetBrains](https://plugins.jetbrains.com/plugin/27189-cline) · [ACP para Neovim](https://docs.cline.bot/usage/acp) |

## Web

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **OpenAI Codex web** | Acceso a Codex desde el navegador para tareas de desarrollo. | [Codex web](https://chatgpt.com/codex) · [Documentación](https://developers.openai.com/learn/codex) |
| **GitHub Copilot coding agent** | Agente que ejecuta tareas delegadas en el entorno de GitHub y propone cambios para revisión mediante el flujo de trabajo del repositorio. | [Documentación de GitHub Copilot](https://docs.github.com/en/copilot) · [Buenas prácticas](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks) |
| **Cline Kanban** | Interfaz web de tablero para ejecutar varios agentes en paralelo, con worktrees por tarea y dependencias entre tareas. | [Repositorio oficial](https://github.com/cline/kanban) |

## Criterios para elegir

Antes de adoptar una herramienta en un proyecto, comprueba:

- **Entorno de trabajo:** escritorio, cliente de terminal, IDE, web o combinación de interfaces.
- **Modelos y proveedor:** modelos disponibles, posibilidad de elegir proveedor y condiciones de acceso.
- **Control de ejecución:** permisos para leer y modificar archivos, ejecutar comandos, acceder a la red y utilizar herramientas.
- **Privacidad y contratación:** tratamiento de prompts y código, retención de datos, uso para entrenamiento, ubicación y condiciones contractuales.
- **Integración con el proyecto:** Git, pruebas, CI, instrucciones del repositorio, MCP y otras herramientas necesarias.
- **Coste y límites:** suscripción, consumo, cuotas, límites de contexto y costes de modelos o servicios externos.
- **Verificación:** facilidad para inspeccionar diffs, ejecutar pruebas y revisar los resultados antes de integrarlos.

No deduzcas las condiciones de privacidad, seguridad o autonomía solo por el nombre del producto o por el tipo de plan. Comprueba la documentación y las condiciones aplicables a la versión, modalidad y organización concretas.

## Mantenimiento de este índice

- La selección es ilustrativa, no exhaustiva ni una recomendación comercial.
- Se priorizan herramientas que representan enfoques distintos; no es necesario añadir cada producto nuevo que aparezca.
- Revisa los enlaces y el estado de los productos cuando se actualice esta guía y, como referencia, cada seis meses.
- Si un producto cambia de nombre, se discontinúa o deja de ser representativo, actualiza o elimina la entrada en lugar de mantenerla por inercia.
- Para instalación, configuración detallada, privacidad y seguridad, consulta siempre la documentación oficial enlazada.

## Relación con la guía

- [Referencias de herramientas y documentación](referencias-herramientas.md): puntos de entrada y referencias detalladas de los productos cubiertos por la guía.
- [Primeros pasos con asistentes de programación](primeros-pasos.md): método inicial de trabajo.
- [Glosario](glosario.md): conceptos comunes de asistentes, agentes y configuración.
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md): evaluación de riesgos, permisos y tratamiento de datos.
- [Mapa de contenidos](mapa-contenidos.md): índice temático de la guía.
