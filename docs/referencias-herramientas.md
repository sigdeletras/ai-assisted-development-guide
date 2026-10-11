# Referencias de herramientas y documentación

Este documento reúne los puntos de entrada oficiales para aprender a utilizar asistentes de programación concretos. No sustituye la guía metodológica: las herramientas cambian, mientras que las prácticas de especificar tareas, revisar código y verificar resultados son transferibles.

Comprueba la documentación del proveedor antes de seguir instrucciones de instalación o configuración, ya que las funciones disponibles pueden depender de la versión, el plan y las políticas de la organización.

## GitHub Copilot

- **Inicio:** [Get started with GitHub Copilot](https://docs.github.com/en/copilot/get-started). Permite elegir entre los distintos entornos de uso.
- **Guía rápida:** [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/get-started/quickstart).
- **Buenas prácticas para tareas:** [Best practices for using GitHub Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks). Se centra en Copilot cloud agent y en cómo definir, planificar y revisar tareas.

**Práctica sugerida:** pide que explique un módulo existente, identifique sus dependencias y proponga una prueba para un caso límite. Contrasta la respuesta con el código antes de solicitar cambios.

## Claude Code

- **Documentación:** [Claude Code overview](https://code.claude.com/docs/en/overview).
- **Inicio rápido:** [Claude Code quickstart](https://code.claude.com/docs/en/quickstart).
- **Buenas prácticas:** [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices). Describe flujos de exploración, planificación, implementación y verificación, así como el uso de instrucciones persistentes.

**Práctica sugerida:** pide al agente que investigue una funcionalidad sin modificar archivos. Después solicita un plan, revísalo y encarga un cambio pequeño con pruebas.

## Cursor

- **Documentación:** [Cursor Docs](https://cursor.com/docs).
- **Inicio rápido:** [Cursor Quickstart](https://cursor.com/docs/get-started/quickstart).
- **Primer proyecto:** [Your first project](https://prod.cursor.com/help/getting-started/first-project).

**Práctica sugerida:** abre un repositorio conocido, pide localizar dónde se implementa una funcionalidad y solicita un plan sin cambios. Luego encarga una mejora acotada y revisa el diff.

## OpenAI Codex

Codex ofrece distintos puntos de entrada, entre ellos CLI, extensión para IDE, aplicación y versión web. Utiliza el cliente disponible y autorizado en tu entorno.

- **Acceso con un plan de ChatGPT:** [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan).
- **Recursos para desarrolladores:** [Codex — OpenAI Developers](https://developers.openai.com/learn/codex).
- **CLI:** [Repositorio oficial de Codex CLI](https://github.com/openai/codex).

**Práctica sugerida:** pide a Codex que explique la estructura del repositorio y proponga un plan para un cambio pequeño. Revisa las modificaciones y ejecuta las pruebas antes de aceptarlas.

## Criterios para usar estas referencias

- Prioriza la documentación oficial para instalación, configuración, permisos y capacidades.
- Distingue las características generales de los asistentes de las funciones específicas de cada producto.
- Comprueba qué datos se procesan, qué permisos recibe la herramienta y qué políticas de retención o privacidad se aplican.
- No compartas credenciales, datos de clientes ni información confidencial sin autorización explícita y sin verificar las condiciones aplicables.

## Relación con el resto de la guía

- [Primeros pasos con asistentes de programación](primeros-pasos.md): metodología inicial para trabajar con IA.
- [Laboratorio práctico](../laboratorio/README.md): ejercicios para aplicar esas prácticas con código.
