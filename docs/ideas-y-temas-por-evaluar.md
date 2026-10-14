# Banco de ideas y temas por evaluar

Este documento funciona como una bandeja de entrada para ideas que podrían incorporarse a **AI-Assisted Development Guide**. Puede recoger propuestas surgidas de noticias, artículos, documentación técnica, novedades de herramientas o necesidades detectadas durante el uso de la guía.

**Las ideas de este documento no forman parte del temario consolidado ni están aprobadas para su incorporación.** Antes de desarrollarlas, hay que valorar su utilidad, encaje, vigencia, nivel de aprendizaje y posible duplicidad con los contenidos existentes.

## Cómo registrar una idea

Para cada entrada, anota lo que se conozca en ese momento. No es necesario completar todos los campos al registrar una idea.

- **Idea:** resumen breve.
- **Origen:** experiencia propia, noticia, artículo, documentación oficial u otra fuente.
- **Problema o aprendizaje:** qué necesidad podría cubrir.
- **Encaje posible:** documento, módulo o laboratorio relacionado, si se conoce.
- **Evaluación:** pendiente, en evaluación, aceptada para planificación, descartada o incorporada.
- **Siguiente paso:** comprobación o decisión necesaria.
- **Fuentes:** enlaces y fecha de consulta cuando la información pueda cambiar.

## Ideas registradas

### 1. Utilizar un único proyecto transversal para los laboratorios

- **Origen:** propuesta editorial interna.
- **Estado:** pendiente de evaluación.
- **Idea:** utilizar un único proyecto de referencia a lo largo de los laboratorios, en lugar de introducir un proyecto distinto en cada ejercicio. El proyecto inicial se desarrollaría en Python, con una API REST como caso de uso, y podría reproducirse posteriormente en otros lenguajes.
- **Objetivo potencial:** reducir la carga cognitiva asociada a aprender distintos dominios funcionales y facilitar la comparación entre metodologías, configuraciones y herramientas de IA. El alumnado podría observar cómo evoluciona el mismo código base al incorporar requisitos, pruebas, instrucciones, reglas, skills, agentes, seguridad y documentación del ciclo de vida.
- **Posible aplicación:** mantener un proyecto base pequeño y progresivo; cada laboratorio partiría de una versión identificable o de una tarea acotada sobre ese proyecto.
- **Cuestiones por resolver:**
  - Definir el dominio funcional y los recursos de la API, procurando que el ejemplo sea comprensible y permita incorporar complejidad gradualmente.
  - Decidir si todos los laboratorios deben modificar el mismo repositorio o si algunos deben trabajar sobre ramas, etiquetas o copias reproducibles.
  - Evitar que el proyecto acumule complejidad accidental o que la preparación del entorno distraiga del objetivo de cada ejercicio.
  - Establecer una estrategia para clonar el caso de uso en otros lenguajes sin convertir la guía inicial en un catálogo multilenguaje.
  - Comprobar la coherencia con los laboratorios actuales y estimar el esfuerzo de migración.
- **Criterio de aceptación posible:** cada laboratorio debe poder explicar qué aporta respecto al anterior, partir de una base reproducible y tener criterios de éxito verificables.

### 2. Chuleta de comandos de Claude Code CLI

- **Origen:** propuesta editorial interna; contrastar con la documentación oficial antes de redactar una referencia estable.
- **Estado:** pendiente de evaluación.
- **Idea:** preparar una chuleta breve de comandos de Claude Code en terminal, especialmente los que permiten iniciar, configurar, inspeccionar o mantener una sesión y el contexto de trabajo.
- **Ejemplo relevante:** `/init`, que analiza el proyecto y genera una primera versión de `CLAUDE.md`. Es un ejemplo de automatización de una tarea de configuración, pero el resultado generado debe revisarse y adaptarse al proyecto.
- **Contenido potencial:**
  - Comandos de sesión y ayuda.
  - Inicialización y contexto del proyecto, incluida la revisión de `CLAUDE.md`.
  - Gestión del contexto y recuperación de sesiones.
  - Inspección y configuración de permisos, hooks, skills y otras capacidades disponibles.
  - Diferencia entre comandos interactivos con barra (`/...`) y comandos o argumentos del ejecutable `claude`.
  - Advertencias sobre opciones que amplían permisos o ejecutan acciones con menos confirmaciones.
- **Criterio editorial:** organizar la chuleta por tareas («quiero inicializar el contexto del proyecto», «quiero revisar permisos»), no solo como un listado alfabético. Indicar que los comandos disponibles pueden variar según la versión, la configuración, el plataforma o las extensiones instaladas.
- **Fuentes iniciales:**
  - [Documentación oficial: CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-usage)
  - [Claude Code cheatsheet, centro de ayuda oficial](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- **Cuestión por resolver:** decidir si conviene una chuleta específica de Claude Code o una referencia comparativa de comandos y flujos equivalentes en varias herramientas. Una referencia específica es más sencilla y precisa; una comparativa encaja mejor con el enfoque agnóstico, pero requiere explicar las diferencias y evitar falsas equivalencias.

## Criterios para evaluar las ideas

Antes de trasladar una entrada al [roadmap](../ROADMAP.md) o convertirla en contenido consolidado, valorar:

1. **Utilidad didáctica:** ¿resuelve una dificultad real o mejora un aprendizaje identificable?
2. **Encaje:** ¿complementa la estructura y el nivel del itinerario existente?
3. **No duplicidad:** ¿aporta algo que no esté explicado de forma suficiente en otro documento?
4. **Verificabilidad:** ¿se puede comprobar mediante documentación oficial, una prueba reproducible o criterios de aceptación?
5. **Agnosticismo:** ¿puede explicarse primero el principio general y después las particularidades de cada proveedor?
6. **Mantenimiento:** ¿cuánto cambiará el contenido y qué coste tendrá mantenerlo actualizado?
7. **Proporcionalidad:** ¿el valor aportado justifica el tiempo de redacción y la complejidad añadida?

## Relación con otros documentos

- [Mapa de contenidos](mapa-contenidos.md): para comprobar dónde encajaría un tema.
- [Referencias de herramientas](referencias-herramientas.md): para decidir si una novedad debe ser solo una referencia externa.
- [Laboratorio](../laboratorio/README.md): para comprobar si una idea se puede convertir en un ejercicio práctico.
- [Roadmap](../ROADMAP.md): para las propuestas ya evaluadas y priorizadas.

Mantén aquí las ideas sin evaluar. Cuando una propuesta se acepte para planificación, trasládala al roadmap con un alcance concreto y actualiza su estado en este documento. Si se descarta, registra brevemente el motivo para evitar volver a evaluarla sin nueva información.
