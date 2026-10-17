# Herramientas de desarrollo asistido por IA

Este índice ofrece una selección breve de herramientas representativas para orientarse en el ecosistema de desarrollo asistido por IA. No es un ranking ni un catálogo exhaustivo: los productos, sus capacidades y sus modelos comerciales cambian con rapidez.

La guía prioriza los conceptos y métodos transferibles —especificar tareas, aportar contexto autorizado, revisar cambios y verificar resultados— por encima de las particularidades de un producto.

## Cómo interpretar la selección

Las categorías describen la interfaz o el flujo de trabajo principal, no límites estrictos. Una misma herramienta puede aparecer en más de una categoría o incorporar nuevas modalidades con el tiempo.

## IDE y editores con funciones de IA

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Visual Studio Code** | Editor de código multiplataforma, extensible mediante un amplio ecosistema de extensiones e integraciones. | [Documentación oficial](https://code.visualstudio.com/docs) · [Inicio rápido](https://code.visualstudio.com/docs/getstarted/getting-started) |
| **Cursor** | Editor basado en VS Code con asistencia y agentes integrados en el flujo de edición. | [Documentación](https://cursor.com/docs) · [Inicio rápido](https://cursor.com/docs/get-started/quickstart) |
| **Kiro** | Entorno de desarrollo que promueve un flujo guiado por especificaciones, requisitos y tareas. | [Documentación](https://kiro.dev/docs/) |

## Agentes de programación por terminal (CLI)

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Claude Code** | Agente de programación para explorar repositorios, modificar código y ejecutar herramientas desde terminal y otras interfaces compatibles. | [Documentación](https://code.claude.com/docs/en/overview) · [Inicio rápido](https://code.claude.com/docs/en/quickstart) |
| **OpenAI Codex** | Agente de programación disponible mediante distintas superficies, incluidas CLI, IDE, aplicación y web, según el producto y el acceso disponible. | [Recursos para desarrolladores](https://developers.openai.com/learn/codex) · [Repositorio de Codex CLI](https://github.com/openai/codex) |
| **Gemini CLI** | Agente de terminal del ecosistema Google para trabajar con código y herramientas. | [Repositorio oficial y documentación](https://github.com/google-gemini/gemini-cli) |
| **OpenCode** | Agente de programación de código abierto, compatible con distintos proveedores y modelos. | [Documentación](https://opencode.ai/docs/) |

## Extensiones y herramientas multimodelo

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Gemini Code Assist** | Asistente de programación disponible como extensión para VS Code y otros IDE; ofrece funciones de generación y completado de código y asistencia mediante chat. Las funciones y condiciones dependen de la edición y el entorno. | [Documentación](https://cloud.google.com/gemini/docs/codeassist/overview) · [IDE compatibles](https://cloud.google.com/gemini/docs/codeassist/supported-languages#supported_ides) |
| **Continue** | Extensión de código abierto para VS Code y JetBrains que integra asistencia de programación con modelos y proveedores configurables. | [Documentación](https://docs.continue.dev/) · [Extensión de VS Code](https://marketplace.visualstudio.com/items?itemName=Continue.continue) |
| **Cline** | Agente integrado en VS Code que puede trabajar con archivos, terminal y herramientas externas bajo un flujo de control configurable. | [Documentación](https://docs.cline.bot/) |
| **Aider** | Asistente de programación desde terminal con integración con Git y soporte para distintos modelos. | [Documentación](https://aider.chat/docs/) |

## Agentes integrados en plataformas de desarrollo

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **GitHub Copilot coding agent** | Modalidad de Copilot que permite delegar tareas de desarrollo en el entorno de GitHub y revisar los cambios propuestos mediante el flujo de trabajo del repositorio. | [Documentación de GitHub Copilot](https://docs.github.com/en/copilot) · [Trabajar con tareas](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks) |

## Criterios para elegir

Antes de adoptar una herramienta en un proyecto, comprueba:

- **Entorno de trabajo:** IDE, terminal, plataforma web o combinación de interfaces.
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
