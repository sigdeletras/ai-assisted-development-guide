# Referencias de herramientas

Consulta esta página para acceder a la documentación oficial y a guías de acceso e inicio rápido de las herramientas. La metodología de trabajo y los criterios de decisión se desarrollan en [Primeros pasos](primeros-pasos.md) y en el [mapa de contenidos](mapa-contenidos.md).

## Acceso rápido

### Selección principal

| Entorno | Herramienta / modalidad | Documentación o acceso |
| --- | --- | --- |
| Escritorio | GitHub Copilot app | [Documentación](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app) · [Inicio rápido](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app) |
| Escritorio | OpenAI Codex en la app de ChatGPT | [Guía de la app](https://developers.openai.com/codex/app) |
| Escritorio | Google Antigravity 2.0 | [Anuncio oficial](https://antigravity.google/blog/introducing-google-antigravity-2) · [Descarga](https://antigravity.google/download) |
| Escritorio | OpenCode Desktop | [Documentación](https://opencode.ai/docs/) · [Descargas e instalación](https://opencode.ai/download) |
| Cliente de terminal (CLI) | Claude Code | [Documentación](https://code.claude.com/docs/en/overview) · [Quickstart](https://code.claude.com/docs/en/quickstart) |
| Cliente de terminal (CLI) | OpenAI Codex CLI | [Documentación](https://developers.openai.com/codex/cli) |
| Cliente de terminal (CLI) | Google Antigravity CLI | [Documentación](https://antigravity.google/blog/introducing-google-antigravity-cli) · [Instalación](https://antigravity.google/cli) |
| Cliente de terminal (CLI) | Gemini CLI* | [Documentación](https://geminicli.com/) · [Transición a Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli) |
| Cliente de terminal (CLI) | OpenCode CLI/TUI | [CLI](https://opencode.ai/docs/cli/) · [TUI](https://opencode.ai/docs/tui/) |
| IDE — editor / entorno | Visual Studio Code | [Documentación](https://code.visualstudio.com/docs) |
| IDE — editor / entorno | Cursor | [Documentación](https://cursor.com/docs) · [Quickstart](https://cursor.com/docs/get-started/quickstart) |
| IDE — editor / entorno | Google Antigravity IDE | [Documentación y anuncio de Antigravity 2.0](https://antigravity.google/blog/introducing-google-antigravity-2) |
| IDE — extensión | GitHub Copilot | [Documentación de Copilot](https://docs.github.com/en/copilot) |
| IDE — extensión | OpenAI Codex | [Documentación](https://developers.openai.com/codex/ide) |
| IDE — extensión | OpenCode | [Integración IDE](https://opencode.ai/docs/ide/) |
| Web | OpenAI Codex web | [Codex web](https://chatgpt.com/codex) |
| Web | GitHub Copilot coding agent | [Documentación de Copilot](https://docs.github.com/en/copilot) · [Buenas prácticas](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks) |
| Web | OpenCode Web | [Documentación](https://opencode.ai/docs/web/) |

La clasificación describe el entorno principal de cada modalidad; no implica que todas las herramientas ofrezcan las mismas funciones ni que estén disponibles con todos los planes. Comprueba la documentación y las políticas aplicables a tu organización.

* Para usuarios gratuitos y de Google One, Gemini CLI fue sustituido por [Antigravity CLI](https://antigravity.google/cli) en junio de 2026. Gemini CLI continúa disponible para determinados clientes empresariales y mediante claves API de pago; consulta el [anuncio oficial](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli).

Como referencia de uso declarado, Stack Overflow publicó en 2026 la [encuesta sobre agentes de programación](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) (n = 12.255 respuestas): Claude Code 66 %, GitHub Copilot 59 %, OpenAI Codex 30 %, Cursor 26 %, Google Antigravity 16 % y OpenCode 14 %. Son resultados de esa encuesta, no cuotas de mercado ni una medida universal de popularidad.

### Otras herramientas

Kiro, Devin, Aider y Cline quedan como referencias complementarias para mantener manejable la selección principal. Es una decisión editorial, no un ranking de popularidad.

| Herramienta | Entornos | Referencias |
| --- | --- | --- |
| Kiro | IDE, CLI, web y móvil (iOS, acceso anticipado) | [Documentación](https://kiro.dev/docs/) |
| Devin | Escritorio/IDE, CLI y web | [Documentación](https://docs.devin.ai/) |
| Aider | CLI | [Documentación](https://aider.chat/docs/) |
| Cline | Escritorio, CLI, IDE y web | [Documentación](https://docs.cline.bot/cline-overview) |

## Equivalencias orientativas

La tabla relaciona mecanismos parecidos entre productos; no implica que sean idénticos ni que tengan el mismo alcance. Para el criterio de uso de las instrucciones generales, consulta [Instrucciones persistentes del proyecto](instrucciones-persistentes.md).

| Concepto común | GitHub Copilot | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- | --- |
| Instrucciones persistentes del proyecto | `.github/copilot-instructions.md`; `AGENTS.md` (prevalece el más cercano) | `CLAUDE.md`; `AGENTS.md` si no hay `CLAUDE.md` (desde v2.1.277) | `.cursor/rules/*.mdc` o `AGENTS.md` | `AGENTS.md` |
| Instrucciones específicas por ruta | `.github/instructions/*.instructions.md` en entornos compatibles | Reglas en `.claude/rules/` con ámbito configurable | Reglas `.cursor/rules/*.mdc` con patrones de aplicación | `AGENTS.md` anidados por directorio |
| Flujos reutilizables (*skills*) | Directorios con `SKILL.md`; ubicación según cliente | `.claude/skills/<nombre>/SKILL.md` | Skills con `SKILL.md`; ubicación según modalidad | `.agents/skills/<nombre>/SKILL.md` |
| Automatización por eventos (*hooks*) | Disponible en CLI y determinados entornos/plugins | Hooks configurados en los ajustes de Claude Code | Hooks según configuración de agente y plugins | Disponible en determinados entornos |
| Herramientas externas (MCP) | Servidores MCP, según cliente | Servidores MCP configurables por ámbito | Servidores MCP desde configuración o archivos de proyecto | Servidores MCP desde configuración o plugins |

## Dónde ampliar información

### GitHub Copilot app

La app de escritorio ofrece sesiones con agentes para carpetas locales o repositorios conectados. No es lo mismo que la extensión de GitHub Copilot para el IDE ni que el coding agent que trabaja en GitHub.

- **Visión general:** [GitHub Copilot app](https://docs.github.com/en/copilot/concepts/copilot-surfaces/github-copilot-app).
- **Instalación y primera sesión:** [Getting started with the GitHub Copilot app](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app).
- Para cuentas Business o Enterprise, comprueba las políticas de Copilot de la organización y qué funciones están habilitadas antes de usarla.

### Claude Code

- **Documentación:** [Claude Code overview](https://code.claude.com/docs/en/overview).
- **Inicio rápido:** [Claude Code quickstart](https://code.claude.com/docs/en/quickstart).
- **Buenas prácticas:** [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices). Describe flujos de exploración, planificación, implementación y verificación, así como el uso de instrucciones persistentes.
- **Privacidad y seguridad:** [Data usage](https://code.claude.com/docs/en/data-usage) y [Security](https://code.claude.com/docs/en/security).
- **Instrucciones del proyecto:** [CLAUDE.md y AGENTS.md](https://code.claude.com/docs/en/memory). Explica qué archivos carga, en qué orden y cómo comprobarlo con `/context`.

### Cursor

- **Documentación:** [Cursor Docs](https://cursor.com/docs).
- **Inicio rápido:** [Cursor Quickstart](https://cursor.com/docs/get-started/quickstart).
- **Primer proyecto:** [Your first project](https://prod.cursor.com/help/getting-started/first-project).
- **Privacidad y datos:** [Data Use & Privacy Overview](https://cursor.com/es/data-use) y [Privacy and data](https://prod.cursor.com/help/security-and-privacy/privacy). Revisa el estado de Privacy Mode, el modelo seleccionado y las excepciones indicadas por el proveedor.

### OpenCode

OpenCode es un agente de código abierto disponible como app de escritorio, cliente de terminal, integración para IDE e interfaz web. OpenCode Web se sirve desde un proceso local; si se cambia su configuración para permitir conexiones desde la red, hay que proteger el acceso.

- **Documentación e instalación:** [OpenCode Docs](https://opencode.ai/docs/) · [descargas](https://opencode.ai/download).
- **Escritorio:** aplicación OpenCode Desktop; consulta la documentación y las opciones oficiales de descarga.
- **Terminal:** [CLI](https://opencode.ai/docs/cli/) y [TUI](https://opencode.ai/docs/tui/).
- **IDE:** [integración con VS Code y editores compatibles](https://opencode.ai/docs/ide/).
- **Web:** [OpenCode Web](https://opencode.ai/docs/web/), interfaz de navegador para un servidor local de OpenCode.

### OpenAI Codex

Codex agrupa varias superficies de trabajo. No confundas el producto de escritorio ChatGPT con una aplicación independiente llamada Codex; selecciona Codex dentro de ChatGPT para tareas de desarrollo. Las funciones y el acceso pueden variar según el entorno, el plan y la configuración.

- **Acceso con un plan de ChatGPT:** [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan).
- **Recursos para desarrolladores:** [Codex — OpenAI Developers](https://developers.openai.com/learn/codex).
- **Escritorio:** [Codex en la app de escritorio de ChatGPT](https://developers.openai.com/codex/app). Permite trabajar con proyectos y archivos locales; también se pueden iniciar tareas en la nube.
- **Terminal / cliente CLI:** [Codex CLI](https://developers.openai.com/codex/cli) · [Repositorio oficial](https://github.com/openai/codex).
- **IDE:** [Extensión Codex para IDE](https://developers.openai.com/codex/ide).
- **Web:** [Codex web](https://chatgpt.com/codex).
- **Privacidad y datos:** [Controles de datos de la plataforma API](https://developers.openai.com/api/docs/guides/your-data) y [controles de datos de ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq). No asumas que las condiciones de la API, ChatGPT y los distintos clientes de Codex son idénticas.

### Otras herramientas

Para ampliar la selección principal, consulta las referencias oficiales:

- **Kiro:** IDE, CLI, web y acceso anticipado para iOS — [documentación](https://kiro.dev/docs/).
- **Devin:** escritorio/IDE, CLI y agente web — [documentación](https://docs.devin.ai/) · [historia de Windsurf](https://cognition.com/blog/windsurf).
- **Aider:** cliente de terminal — [documentación](https://aider.chat/docs/).
- **Cline:** escritorio, CLI, IDE y web — [descripción general](https://docs.cline.bot/cline-overview).

### AGENTS.md

- **Especificación y guía:** [agents.md](https://agents.md/) y [repositorio del formato](https://github.com/agentsmd/agents.md). Recoge los temas recomendados, la prioridad de los archivos anidados y la lista de herramientas compatibles.
- **GitHub Copilot:** [Añadir instrucciones al repositorio](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions), incluido el uso de `AGENTS.md`.
- Criterios de uso en esta guía: [Instrucciones persistentes del proyecto](instrucciones-persistentes.md).

## Criterios para usar estas referencias

- Prioriza la documentación oficial para instalación, configuración, permisos, privacidad y capacidades.
- Distingue las características generales de los asistentes de las funciones específicas de cada producto.
- Comprueba qué datos se procesan, qué permisos recibe la herramienta y qué políticas de retención o privacidad se aplican.
- No confundas la exclusión del entrenamiento con la retención cero de datos (ZDR).
- No deduzcas las condiciones de privacidad a partir de que un plan sea gratuito o de pago; verifica el producto, plan, función y modelo concretos.
- No compartas credenciales, datos de clientes ni información confidencial sin autorización explícita y sin verificar las condiciones aplicables.
- Para un criterio transversal, consulta [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md).

## Relación con el resto de la guía

- [Primeros pasos con asistentes de programación](primeros-pasos.md): metodología inicial y orientación para practicar.
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md): criterios de clasificación, tratamiento de datos, retención y permisos.
- [Laboratorio práctico](../laboratorio/README.md): proyectos y ejercicios para aplicar los métodos de la guía.

Los ejercicios se describen junto a los conceptos y prácticas que enseñan. Este documento se limita a reunir referencias de producto; no define ejercicios independientes.
