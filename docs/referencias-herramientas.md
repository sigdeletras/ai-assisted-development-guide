# Referencias de herramientas

Una entrada y un inicio rápido por herramienta. Consulta estas páginas para instalarla y conocer sus capacidades; para decidir cómo trabajar, empieza por la [guía metodológica](primeros-pasos.md).

## Acceso rápido

| Herramienta | Documentación | Inicio rápido |
| --- | --- | --- |
| GitHub Copilot | [Documentación de Copilot](https://docs.github.com/en/copilot) | [Primeros pasos con la app de Copilot](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app) |
| Claude Code | [Documentación de Claude Code](https://code.claude.com/docs/en/overview) | [Quickstart](https://code.claude.com/docs/en/quickstart) |
| Cursor | [Documentación de Cursor](https://cursor.com/docs) | [Quickstart](https://prod.cursor.com/docs/get-started/quickstart) |
| OpenAI Codex | [Documentación de Codex](https://developers.openai.com/learn/codex) | [Inicio rápido de Codex CLI](https://github.com/openai/codex#quickstart) |

Los productos ofrecen distintas modalidades (IDE, CLI, aplicación o agente en la nube). El inicio rápido enlazado corresponde a una modalidad concreta; comprueba que sea la adecuada para tu entorno y las políticas de tu organización.

## Equivalencias orientativas

Los nombres y mecanismos no son idénticos entre herramientas. Esta tabla sirve para localizar el concepto equivalente, no para asumir que los archivos, el alcance o el comportamiento son intercambiables.

| Concepto común | GitHub Copilot | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- | --- |
| Instrucciones persistentes del proyecto | `.github/copilot-instructions.md`; `AGENTS.md` en entornos compatibles | `CLAUDE.md` | `.cursor/rules/*.mdc` o `AGENTS.md` | `AGENTS.md` |
| Instrucciones específicas por ruta | `.github/instructions/*.instructions.md` en entornos compatibles | Reglas en `.claude/rules/` con ámbito configurable | Reglas `.cursor/rules/*.mdc` con patrones de aplicación | `AGENTS.md` anidados por directorio; el más específico puede añadir instrucciones |
| Flujos de trabajo reutilizables (*skills*) | Directorios con `SKILL.md`; la ruta depende del cliente | `.claude/skills/<nombre>/SKILL.md` | Skills con `SKILL.md`; ubicación según el tipo de instalación | `.agents/skills/<nombre>/SKILL.md` |
| Automatización por eventos (*hooks*) | Hooks en CLI y plugins; la configuración depende del cliente | Hooks configurados en los ajustes de Claude Code | Hooks en la configuración de agente/plugins | Hooks disponibles en determinados entornos y plugins |
| Conexión con herramientas externas (MCP) | Servidores MCP, según el cliente | Servidores MCP, configurables por ámbito | Servidores MCP desde configuración o archivos de proyecto | Servidores MCP desde configuración o plugins |

**Importante:** las equivalencias son conceptuales, no compatibilidad automática. Algunas funciones solo están disponibles en determinadas modalidades o versiones, y el alcance de una configuración puede cambiar entre productos. Antes de reutilizar archivos o copiar una configuración, verifica la documentación oficial de la herramienta y el entorno concretos.

Para profundizar, consulta el [mapa de contenidos](mapa-contenidos.md): [contexto e instrucciones](mapa-contenidos.md), [agentes y automatización](mapa-contenidos.md) y [seguridad](mapa-contenidos.md).

## Relación con el resto de la guía

- [Primeros pasos](primeros-pasos.md): flujo inicial de trabajo y verificación.
- [Mapa de contenidos](mapa-contenidos.md): conceptos, criterios de decisión y metodologías.
- [Laboratorio práctico](../laboratorio/README.md): ejercicios para aplicar las prácticas en proyectos.

Los ejercicios se describen junto a los conceptos que enseñan; este documento se limita a orientar hacia las herramientas y sus fuentes oficiales.
