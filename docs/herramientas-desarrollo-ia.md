# Herramientas de desarrollo asistido por IA

*Este índice ofrece una selección breve de herramientas representativas para orientarse en el ecosistema de desarrollo asistido por IA. No es un ranking ni un catálogo exhaustivo: los productos, sus capacidades y sus modelos comerciales cambian con rapidez.*


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

## Herramientas de desarrollo asistido por IA por entorno

Las herramientas se organizan según el entorno de uso: **escritorio**, **cliente de terminal**, **IDE** y **web**. Algunas están disponibles en más de uno; en esos casos se indican las modalidades pertinentes. Las funciones y condiciones pueden variar según la modalidad, el plan y la configuración.

### Selección principal: resumen por entorno

| Herramienta | Escritorio | Cliente CLI | IDE | Web |
| --- | :---: | :---: | :---: | :---: |
| Visual Studio Code | — | — | ✓ | — |
| Claude Code | — | ✓ | — | — |
| OpenAI Codex | ✓ | ✓ | ✓ | ✓ |
| Google Antigravity | ✓ | ✓ | ✓ | — |
| Gemini CLI* | — | ✓ | — | — |
| Cursor | — | — | ✓ | — |
| GitHub Copilot | ✓ | — | ✓ | ✓ |
| OpenCode | ✓ | ✓ | ✓ | ✓ |

✓ Modalidad documentada en esta guía. — No incluida en esta selección. La tabla resume el tipo de cliente, no la disponibilidad por sistema operativo, plan o cuenta.
* La disponibilidad de Gemini CLI depende del tipo de cuenta; consulta el [anuncio oficial](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli) y la alternativa [Antigravity CLI](https://antigravity.google/cli).

La selección principal se apoya también en los datos de uso de la [encuesta Stack Overflow 2026 sobre agentes de programación](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent): entre las herramientas de la tabla, indica Claude Code 66 %, GitHub Copilot 59 %, OpenAI Codex 30 %, Cursor 26 %, Google Antigravity 16 % y OpenCode 14 % (n = 12.255). Son respuestas de participantes de la encuesta, no una medida de cuota de mercado ni un ranking universal.


## IDE

### Editores y entornos de desarrollo

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Visual Studio Code** | Editor de código multiplataforma, extensible mediante un amplio ecosistema de extensiones e integraciones. | [Documentación](https://code.visualstudio.com/docs) · [Inicio rápido](https://code.visualstudio.com/docs/getstarted/getting-started) |
| **Cursor** | Editor basado en VS Code con asistencia y agentes integrados en el flujo de edición. | [Documentación](https://cursor.com/docs) · [Inicio rápido](https://cursor.com/docs/get-started/quickstart) |
| **Google Antigravity IDE** | IDE de Google con integración de agentes; se ofrece junto con Antigravity 2.0, una aplicación de escritorio independiente centrada en agentes. | [Documentación y anuncio de Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2) |

### Extensiones para IDE

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **GitHub Copilot para IDE** | Extensión de asistencia de código y chat integrada en VS Code y otros IDE compatibles. | [Documentación de GitHub Copilot](https://docs.github.com/en/copilot) |
| **OpenAI Codex para IDE** | Extensión de Codex para VS Code, Cursor, Windsurf y otros IDE compatibles. | [Documentación](https://developers.openai.com/codex/ide) |
| **OpenCode para IDE** | Integración con VS Code, Cursor, Windsurf y VSCodium; ofrece acceso al agente en un panel y comparte el contexto del editor. | [Documentación de la integración IDE](https://opencode.ai/docs/ide/) |

## Cliente de terminal (CLI)

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **Claude Code** | Agente de programación para explorar repositorios, modificar código y ejecutar herramientas desde terminal y otras interfaces compatibles. | [Documentación](https://code.claude.com/docs/en/overview) · [Inicio rápido](https://code.claude.com/docs/en/quickstart) |
| **OpenAI Codex CLI** | Cliente de línea de comandos para trabajar con Codex desde la terminal. | [Documentación](https://developers.openai.com/codex/cli) · [Repositorio](https://github.com/openai/codex) |
| **Google Antigravity CLI** | Cliente de terminal ligero para invocar, supervisar e interactuar con los agentes de Antigravity; comparte el agente y la configuración con Antigravity 2.0. | [Documentación oficial](https://antigravity.google/blog/introducing-google-antigravity-cli) · [Instalación](https://antigravity.google/cli) |
| **Gemini CLI*** | Agente de terminal de código abierto del ecosistema Google. Para usuarios gratuitos y de Google One fue sustituido por Antigravity CLI en junio de 2026; sigue disponible para determinados clientes empresariales y mediante claves API de pago. | [Documentación](https://geminicli.com/) · [Anuncio de transición](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli) |
| **OpenCode CLI/TUI** | Cliente de terminal de código abierto con interfaz interactiva y soporte para distintos proveedores y modelos. | [CLI](https://opencode.ai/docs/cli/) · [Interfaz TUI](https://opencode.ai/docs/tui/) |


## Escritorio

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **GitHub Copilot app** | Aplicación de escritorio para sesiones con agentes sobre carpetas locales o repositorios conectados, revisión de cambios y creación de pull requests. Es distinta de la extensión de Copilot para IDE y del coding agent de GitHub. | [Documentación](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app) · [Inicio rápido](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app) |
| **OpenAI Codex en la app de escritorio de ChatGPT** | Modalidad de Codex para trabajar con proyectos y archivos locales y para iniciar tareas en la nube. | [Guía de la app](https://developers.openai.com/codex/app) |
| **Google Antigravity 2.0** | Aplicación de escritorio independiente, centrada en el uso de agentes y distinta de Antigravity IDE. | [Anuncio oficial](https://antigravity.google/blog/introducing-google-antigravity-2) · [Descarga](https://antigravity.google/download) |
| **OpenCode Desktop** | Aplicación de escritorio para usar el agente de programación OpenCode. | [Documentación](https://opencode.ai/docs/) · [Descargas e instalación](https://opencode.ai/download) |

## Web

| Herramienta | Enfoque | Documentación oficial |
| --- | --- | --- |
| **OpenAI Codex web** | Acceso a Codex desde el navegador para tareas de desarrollo. | [Codex web](https://chatgpt.com/codex) · [Documentación](https://developers.openai.com/learn/codex) |
| **OpenCode Web** | Interfaz de navegador para sesiones de OpenCode, servida por un proceso local de OpenCode; no es un servicio cloud alojado por OpenCode. | [Documentación de OpenCode Web](https://opencode.ai/docs/web/) |
| **GitHub Copilot coding agent** | Agente que ejecuta tareas delegadas en el entorno de GitHub y propone cambios para revisión mediante el flujo de trabajo del repositorio. | [Documentación de GitHub Copilot](https://docs.github.com/en/copilot) · [Buenas prácticas](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks) |

## Otras herramientas

Estas herramientas quedan en segundo plano para que el recorrido inicial sea manejable. Es una decisión editorial, no un ranking de popularidad.

| Herramienta | Entornos con modalidad documentada | Referencias |
| --- | --- | --- |
| **Kiro** | CLI, IDE, web y móvil (iOS, acceso anticipado) | [Documentación](https://kiro.dev/docs/) |
| **Devin** | Escritorio/IDE, CLI y web | [Documentación](https://docs.devin.ai/) |
| **Aider** | CLI | [Documentación](https://aider.chat/docs/) |
| **Cline** | Escritorio, CLI, IDE y web | [Documentación](https://docs.cline.bot/cline-overview) |


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
