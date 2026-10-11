# Primeros pasos con asistentes de programación

Esta guía está pensada para desarrolladores con experiencia que empiezan a utilizar las suscripciones de IA disponibles en su empresa. El objetivo inicial no es configurar un entorno avanzado, sino incorporar estas herramientas a tareas reales y aprender a verificar sus resultados.

Para practicar estas técnicas con código, consulta el **[laboratorio de desarrollo asistido por IA](../laboratorio/README.md)**. El primer ejercicio utiliza un pequeño ejemplo de puntos geográficos y GeoJSON.

## Cómo empezar

1. Elige una herramienta que ya tengas autorizada por tu empresa.
2. Empieza con una tarea de bajo riesgo: comprender una parte del código, investigar un error, añadir una prueba o proponer una refactorización pequeña.
3. Pide explicaciones o un plan antes de solicitar cambios cuando la tarea no esté clara.
4. Revisa el diff, ejecuta las pruebas y comprueba el comportamiento antes de aceptar el resultado.
5. No introduzcas secretos, credenciales ni datos confidenciales en una herramienta sin confirmar antes las políticas de la empresa.

No es necesario aprender todas las herramientas a la vez. Las cuatro guías siguientes son puntos de entrada; las funciones disponibles pueden variar según el producto, la integración y el plan contratado.

## GitHub Copilot

- **Guía de inicio oficial:** [Get started with GitHub Copilot](https://docs.github.com/en/copilot/get-started). Desde aquí puedes elegir el uso en GitHub, en el IDE, por CLI o en la aplicación Copilot.
- **Guía rápida para el IDE:** [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/get-started/quickstart). Selecciona la pestaña de tu editor o entorno.
- **Buenas prácticas:** [Best practices for using GitHub Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks). Se centra en Copilot cloud agent: definición de tareas, criterios de aceptación, planificación e iteración antes de abrir un Pull Request.

**Práctica inicial sugerida:** pide a Copilot que explique un módulo existente, identifique sus dependencias y proponga una prueba para un caso límite. Revisa la explicación y valida la prueba antes de pedir una modificación.

## Claude Code

- **Documentación oficial:** [Claude Code overview](https://code.claude.com/docs/en/overview). Introduce el agente, su configuración y su uso desde el entorno de desarrollo.
- **Guía de inicio rápido:** [Claude Code quickstart](https://code.claude.com/docs/en/quickstart). Recorrido inicial para instalar y utilizar el agente.
- **Buenas prácticas de Anthropic:** [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices). Explica flujos como explorar el repositorio, planificar, implementar, probar e iterar, además del uso de instrucciones persistentes como `CLAUDE.md`.

**Práctica inicial sugerida:** pide a Claude Code que investigue cómo se implementa una funcionalidad sin modificar archivos; después solicita un plan y, solo tras revisarlo, una modificación pequeña con pruebas.

## Cursor

- **Documentación oficial:** [Cursor Docs](https://cursor.com/docs). Punto de entrada a instalación, uso del agente, contexto, reglas y otras capacidades.
- **Guía rápida:** [Cursor Quickstart](https://cursor.com/docs/get-started/quickstart). Acompaña desde la instalación hasta la primera modificación útil, incluyendo revisión del diff y ejecución de comprobaciones.
- **Primer proyecto:** [Your first project](https://prod.cursor.com/help/getting-started/first-project). Explica cómo abrir un proyecto, trabajar con Agent y aportar contexto.

**Práctica inicial sugerida:** abre un repositorio conocido, pide al agente que localice dónde se implementa una funcionalidad y solicita un plan sin cambios. A continuación, encárgale una mejora acotada y revisa cada modificación en el diff.

## OpenAI Codex

Codex dispone de varios puntos de entrada: terminal (CLI), extensión para IDE, aplicación de escritorio y versión web. Para iniciarse, elige el cliente que esté aprobado y disponible en tu entorno de trabajo.

- **Primeros pasos y acceso con ChatGPT:** [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan). Describe cómo acceder a Codex desde los distintos clientes; la disponibilidad de funciones depende del plan y de la configuración del espacio de trabajo.
- **Documentación para desarrolladores:** [Codex — OpenAI Developers](https://developers.openai.com/learn/codex). Recopila guías, vídeos y recursos de uso.
- **CLI e instalación:** [Repositorio oficial de Codex CLI](https://github.com/openai/codex). Incluye instrucciones de instalación y puesta en marcha.

**Práctica inicial sugerida:** abre un repositorio conocido con el cliente de Codex autorizado y pídele que explique la estructura del proyecto. Después solicita un plan para una modificación pequeña, revisa los cambios propuestos y ejecuta las pruebas antes de aceptarlos.

## Qué aprender primero

Con independencia de la herramienta, conviene practicar estas capacidades antes de entrar en configuraciones avanzadas:

- Dar contexto relevante y describir el resultado esperado.
- Dividir tareas grandes en pasos pequeños y verificables.
- Pedir un plan antes de cambios complejos.
- Revisar el diff y entender el código generado.
- Ejecutar pruebas, linters y otras comprobaciones del proyecto.
- Reconocer cuándo una tarea requiere criterio humano o información que el modelo no tiene.

Los archivos de instrucciones, las reglas, las skills, los hooks, los subagentes y MCP se abordarán más adelante, cuando exista una necesidad concreta que justifique configurarlos.

## Nota de seguridad

Antes de conectar un agente a un repositorio de trabajo, terminal, servicios externos o credenciales, comprueba las políticas de la empresa sobre datos, propiedad intelectual, retención, permisos y herramientas aprobadas. No des por hecho que una suscripción empresarial permite compartir cualquier información con cualquier función del producto.
