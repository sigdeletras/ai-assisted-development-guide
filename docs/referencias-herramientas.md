# Referencias de herramientas

Consulta esta página para acceder a la documentación oficial y al inicio rápido de cada herramienta. La metodología de trabajo y los criterios de decisión se desarrollan en [Primeros pasos](primeros-pasos.md) y en el [mapa de contenidos](mapa-contenidos.md).

## Acceso rápido

| Herramienta | Documentación | Inicio rápido |
| --- | --- | --- |
| GitHub Copilot | [Documentación de Copilot](https://docs.github.com/en/copilot) | [Primeros pasos con la app de Copilot](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app) |
| Claude Code | [Documentación de Claude Code](https://code.claude.com/docs/en/overview) | [Quickstart](https://code.claude.com/docs/en/quickstart) |
| Cursor | [Documentación de Cursor](https://cursor.com/docs) | [Quickstart](https://prod.cursor.com/docs/get-started/quickstart) |
| OpenAI Codex | [Documentación de Codex](https://developers.openai.com/learn/codex) | [Inicio rápido de Codex CLI](https://github.com/openai/codex#quickstart) |

Los productos ofrecen distintas modalidades (IDE, CLI, aplicación o agente en la nube). El inicio rápido enlazado corresponde a una modalidad concreta; comprueba que sea la adecuada para tu entorno y las políticas de tu organización.

## Equivalencias orientativas

- **Documentación:** [Claude Code overview](https://code.claude.com/docs/en/overview).
- **Inicio rápido:** [Claude Code quickstart](https://code.claude.com/docs/en/quickstart).
- **Buenas prácticas:** [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices). Describe flujos de exploración, planificación, implementación y verificación, así como el uso de instrucciones persistentes.
- **Privacidad y seguridad:** [Data usage](https://code.claude.com/docs/en/data-usage) y [Security](https://code.claude.com/docs/en/security).

| Concepto común | GitHub Copilot | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- | --- |
| Instrucciones persistentes del proyecto | `.github/copilot-instructions.md`; `AGENTS.md` en entornos compatibles | `CLAUDE.md` | `.cursor/rules/*.mdc` o `AGENTS.md` | `AGENTS.md` |
| Instrucciones específicas por ruta | `.github/instructions/*.instructions.md` en entornos compatibles | Reglas en `.claude/rules/` con ámbito configurable | Reglas `.cursor/rules/*.mdc` con patrones de aplicación | `AGENTS.md` anidados por directorio |
| Flujos reutilizables (*skills*) | Directorios con `SKILL.md`; ubicación según cliente | `.claude/skills/<nombre>/SKILL.md` | Skills con `SKILL.md`; ubicación según modalidad | `.agents/skills/<nombre>/SKILL.md` |
| Automatización por eventos (*hooks*) | Disponible en CLI y determinados entornos/plugins | Hooks configurados en los ajustes de Claude Code | Hooks según configuración de agente y plugins | Disponible en determinados entornos |
| Herramientas externas (MCP) | Servidores MCP, según cliente | Servidores MCP configurables por ámbito | Servidores MCP desde configuración o archivos de proyecto | Servidores MCP desde configuración o plugins |

- **Documentación:** [Cursor Docs](https://cursor.com/docs).
- **Inicio rápido:** [Cursor Quickstart](https://cursor.com/docs/get-started/quickstart).
- **Primer proyecto:** [Your first project](https://prod.cursor.com/help/getting-started/first-project).
- **Privacidad y datos:** [Data Use & Privacy Overview](https://cursor.com/es/data-use) y [Privacy and data](https://prod.cursor.com/help/security-and-privacy/privacy). Revisa el estado de Privacy Mode, el modelo seleccionado y las excepciones indicadas por el proveedor.

## Dónde ampliar información

Codex ofrece distintos puntos de entrada, entre ellos CLI, extensión para IDE, aplicación y versión web. Utiliza el cliente disponible y autorizado en tu entorno.

- **Acceso con un plan de ChatGPT:** [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan).
- **Recursos para desarrolladores:** [Codex — OpenAI Developers](https://developers.openai.com/learn/codex).
- **CLI:** [Repositorio oficial de Codex CLI](https://github.com/openai/codex).
- **Privacidad y datos:** [Controles de datos de la plataforma API](https://developers.openai.com/api/docs/guides/your-data) y [controles de datos de ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-faq). No asumas que las condiciones de la API, ChatGPT y los distintos clientes de Codex son idénticas.

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
