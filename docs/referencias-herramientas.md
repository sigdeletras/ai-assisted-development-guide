# Referencias de herramientas y documentación

Este documento reúne los puntos de entrada oficiales para aprender a utilizar asistentes de programación concretos. No sustituye la guía metodológica: las herramientas cambian, mientras que las prácticas de especificación, revisión y verificación son transferibles.

Para una visión rápida de las categorías y de una selección representativa de productos, consulta el [índice de herramientas de desarrollo asistido por IA](herramientas-desarrollo-ia.md). Para conocer las principales familias de modelos y distinguir entre modelos propietarios, pesos abiertos y código abierto para IA, consulta [LLM: familias de modelos, distribución y criterios de selección](referencias-llm.md).

Comprueba la documentación del proveedor antes de seguir instrucciones de instalación o configuración, ya que las funciones disponibles pueden depender de la versión, el plan y las políticas de la organización.

## GitHub Copilot

- **Inicio:** [Get started with GitHub Copilot](https://docs.github.com/en/copilot/get-started). Permite elegir entre los distintos entornos de uso.
- **Guía rápida:** [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/get-started/quickstart).
- **Buenas prácticas para tareas:** [Best practices for using GitHub Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks). Se centra en Copilot cloud agent y en cómo definir, planificar y revisar tareas.
- **Privacidad y datos:** [Administrar directivas y opciones de datos](https://docs.github.com/es/copilot/how-tos/manage-your-account/manage-policies) y [datos de sesión y retención](https://docs.github.com/es/copilot/concepts/security-governance-and-network-settings/session-data).

## Claude Code

- **Documentación:** [Claude Code overview](https://code.claude.com/docs/en/overview).
- **Inicio rápido:** [Claude Code quickstart](https://code.claude.com/docs/en/quickstart).
- **Buenas prácticas:** [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices). Describe flujos de exploración, planificación, implementación y verificación, así como el uso de instrucciones persistentes.
- **Privacidad y seguridad:** [Data usage](https://code.claude.com/docs/en/data-usage) y [Security](https://code.claude.com/docs/en/security).

## Cursor

- **Documentación:** [Cursor Docs](https://cursor.com/docs).
- **Inicio rápido:** [Cursor Quickstart](https://cursor.com/docs/get-started/quickstart).
- **Primer proyecto:** [Your first project](https://prod.cursor.com/help/getting-started/first-project).
- **Privacidad y datos:** [Data Use & Privacy Overview](https://cursor.com/es/data-use) y [Privacy and data](https://prod.cursor.com/help/security-and-privacy/privacy). Revisa el estado de Privacy Mode, el modelo seleccionado y las excepciones indicadas por el proveedor.

## OpenAI Codex

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
