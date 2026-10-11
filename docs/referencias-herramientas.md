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

Los nombres y mecanismos no son idénticos entre herramientas. La tabla sirve para localizar el concepto equivalente, no para asumir que los archivos, el alcance o el comportamiento son intercambiables.

| Concepto común | GitHub Copilot | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- | --- |
| Instrucciones persistentes del proyecto | `.github/copilot-instructions.md`; también admite `AGENTS.md` en entornos compatibles | `CLAUDE.md`; también admite `AGENTS.md` | Reglas de proyecto en `.cursor/rules/`; admite instrucciones `AGENTS.md` en flujos compatibles | `AGENTS.md` |
| Instrucciones específicas por contexto o ruta | `.github/instructions/*.instructions.md` en entornos compatibles | Instrucciones y reglas mediante archivos de memoria/configuración y reglas del proyecto | Reglas con ámbito y patrones de aplicación | Instrucciones `AGENTS.md` por directorio; el alcance depende de la ubicación |
| Flujos de trabajo reutilizables (*skills*) | Disponibilidad y soporte según el producto y el entorno | Skills | Skills | Skills |
| Automatización por eventos (*hooks*) | Depende del producto o entorno de Copilot; no hay correspondencia universal | Hooks de Claude Code | No asumir equivalencia directa con reglas o skills; comprobar la funcionalidad vigente | Hooks según el entorno y las extensiones disponibles; comprobar la documentación vigente |
| Conexión con herramientas externas | Integraciones y servidores MCP compatibles con el entorno | MCP | MCP | MCP |

**Importante:** esta equivalencia es conceptual y no implica compatibilidad automática. El soporte puede variar entre la app, el IDE, la CLI, el agente en la nube, la versión y el plan. Antes de copiar una configuración entre herramientas, verifica su documentación oficial. Los conceptos de [instrucciones y contexto](mapa-contenidos.md), [agentes y automatización](mapa-contenidos.md) y [seguridad](mapa-contenidos.md) se explican en el mapa temático.

## Relación con el resto de la guía

- [Primeros pasos](primeros-pasos.md): flujo inicial de trabajo y verificación.
- [Mapa de contenidos](mapa-contenidos.md): conceptos, criterios de decisión y metodologías.
- [Laboratorio práctico](../laboratorio/README.md): ejercicios para aplicar las prácticas en proyectos.

Los ejercicios se describen junto a los conceptos que enseñan; este documento se limita a orientar hacia las herramientas y sus fuentes oficiales.
