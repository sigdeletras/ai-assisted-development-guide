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

Los nombres y mecanismos no son idénticos entre herramientas. La tabla permite localizar el concepto relacionado; no implica que los archivos, el alcance o el comportamiento sean intercambiables.

| Concepto común | GitHub Copilot | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- | --- |
| Instrucciones persistentes del proyecto | `.github/copilot-instructions.md`; `AGENTS.md` en entornos compatibles | `CLAUDE.md` | `.cursor/rules/*.mdc` o `AGENTS.md` | `AGENTS.md` |
| Instrucciones específicas por ruta | `.github/instructions/*.instructions.md` en entornos compatibles | Reglas en `.claude/rules/` con ámbito configurable | Reglas `.cursor/rules/*.mdc` con patrones de aplicación | `AGENTS.md` anidados por directorio |
| Flujos reutilizables (*skills*) | Directorios con `SKILL.md`; ubicación según cliente | `.claude/skills/<nombre>/SKILL.md` | Skills con `SKILL.md`; ubicación según modalidad | `.agents/skills/<nombre>/SKILL.md` |
| Automatización por eventos (*hooks*) | Disponible en CLI y determinados entornos/plugins | Hooks configurados en los ajustes de Claude Code | Hooks según configuración de agente y plugins | Disponible en determinados entornos |
| Herramientas externas (MCP) | Servidores MCP, según cliente | Servidores MCP configurables por ámbito | Servidores MCP desde configuración o archivos de proyecto | Servidores MCP desde configuración o plugins |

**Importante:** las equivalencias son conceptuales, no compatibilidad automática. La disponibilidad y el alcance pueden variar según modalidad, versión y configuración. Antes de reutilizar archivos o copiar una configuración, comprueba la documentación oficial del producto y entorno concretos.

## Dónde ampliar información

- [Primeros pasos](primeros-pasos.md): flujo inicial y verificación.
- [Mapa de contenidos](mapa-contenidos.md): conceptos, metodologías y criterios de decisión.
- [Laboratorios](../laboratorio/README.md): ejercicios prácticos.
- [Seguridad y trabajo pendiente](../ROADMAP.md): criterios generales y propuestas de evolución.
