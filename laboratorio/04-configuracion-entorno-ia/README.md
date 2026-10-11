# 04 · Configurar el entorno de desarrollo asistido por IA

## Objetivo

Diseñar, implementar y validar una configuración de IA adecuada para un proyecto existente. El ejercicio parte del diagnóstico del [laboratorio 03](../03-proyecto-existente/README.md) y convierte sus conclusiones en instrucciones, reglas y capacidades reutilizables cuando aporten valor.

Al terminar, el repositorio tendrá una configuración **mínima, explicada y probada** para las herramientas seleccionadas. No se pretende instalar todos los mecanismos disponibles ni asumir que los distintos proveedores ofrecen equivalencias exactas.

## Preparación

- Completa primero el [laboratorio 03](../03-proyecto-existente/README.md), o realiza un diagnóstico equivalente.
- Utiliza el proyecto de práctica o un repositorio propio autorizado y no confidencial.
- Elige una herramienta principal y, si procede, una segunda herramienta con la que quieras compartir instrucciones.
- Comprueba la documentación oficial vigente y las políticas de tu organización.
- Revisa el estado de Git antes de empezar y trabaja en una rama de ejercicio.
- No añadas credenciales, datos personales ni información de clientes a los archivos de configuración.

## Conceptos que vas a distinguir

| Necesidad | Mecanismo habitual | Cuándo utilizarlo |
| --- | --- | --- |
| Orientación persistente sobre el proyecto | Instrucciones generales, por ejemplo `AGENTS.md` o el mecanismo propio de la herramienta | Convenciones, arquitectura, comandos y límites que se aplican habitualmente. |
| Instrucciones para una parte del código | Rules o instrucciones por ruta | Reglas específicas para directorios, lenguajes o tipos de archivo. |
| Procedimiento reutilizable | Skill | Flujo de trabajo con pasos, criterios y recursos que el agente debe aplicar cuando corresponda. |
| Rol con responsabilidades delimitadas | Agente personalizado o especializado | Tareas que justifican instrucciones, herramientas o permisos distintos. |
| Control determinista durante el ciclo de trabajo | Hook o mecanismo de evento equivalente | Ejecutar comprobaciones o controles en eventos definidos, sin depender solo de que el modelo los recuerde. |
| Capacidades y límites de ejecución | Ajustes, permisos y configuración del cliente | Definir qué herramientas, comandos, rutas o conexiones están autorizados. |
| Plantilla de tarea invocable manualmente | Prompt reutilizable, si la herramienta lo ofrece | Repetir una petición estructurada sin convertirla en una instrucción permanente. |

Estos mecanismos no son intercambiables. Una instrucción expresa expectativas; una skill describe un procedimiento; un hook ejecuta una acción en un evento; los permisos limitan lo que la herramienta puede hacer.

## Ejercicios

### 1. Diseñar antes de crear archivos

Recupera del laboratorio 03 las convenciones verificadas, los comandos reales, los riesgos y las dudas pendientes. Prepara una tabla de decisión con estas columnas:

- necesidad detectada;
- mecanismo propuesto;
- herramienta y alcance;
- evidencia que justifica la decisión;
- decisión: implementar, posponer o descartar;
- criterio para comprobar que funciona.

No conviertas hipótesis en convenciones. No crees archivos solo porque una herramienta permita crearlos.

### 2. Configurar las instrucciones principales

Crea o adapta el mecanismo de instrucciones persistentes que lea la herramienta elegida. Incluye únicamente información útil para tareas recurrentes:

- propósito y arquitectura del proyecto;
- comandos reales para instalar, ejecutar, probar y validar;
- convenciones confirmadas;
- límites de alcance y política para cambios no solicitados;
- requisitos de pruebas, revisión del diff y comunicación de incertidumbres;
- normas de seguridad para secretos y datos sensibles.

Mantén el contenido breve y verificable. Si vas a utilizar varias herramientas, identifica una fuente común cuando sea viable y añade adaptaciones específicas solo donde haya diferencias reales. No supongas que un archivo se lee automáticamente en todos los productos.

### 3. Crear una regla específica

Identifica una convención que solo deba aplicarse a una parte del repositorio. Implementa una regla por ruta o el mecanismo equivalente de la herramienta elegida.

Ejemplos: reglas para pruebas, migraciones, interfaz web o módulos geográficos. Si el proyecto no tiene una necesidad real de alcance específico, documenta por qué no hace falta crearla.

Comprueba tanto un caso en el que la regla deba aplicarse como otro en el que no deba activarse, si la herramienta permite verificarlo.

### 4. Crear una skill para un flujo repetible

Elige una tarea acotada que se repita en el proyecto, como preparar una revisión de cambios, diagnosticar un fallo de pruebas o incorporar una nueva capa de datos.

La skill debe especificar:

- nombre y descripción que permitan identificar cuándo usarla;
- precondiciones y contexto necesario;
- pasos de trabajo;
- comprobaciones y criterios de finalización;
- tratamiento de errores e incertidumbres;
- scripts, ejemplos o referencias auxiliares, solo si son necesarios.

Prueba la skill con una petición que encaje con su propósito y comprueba que no se activa o recomienda indebidamente para una tarea distinta.

### 5. Evaluar agentes especializados y hooks

No es obligatorio implementar ambos. Para cada uno, responde primero a una necesidad concreta.

**Agente especializado:** ¿existe una tarea que requiera un rol claramente separado, instrucciones distintas o un conjunto limitado de herramientas? Si la respuesta es sí, crea uno con responsabilidades y límites explícitos y prueba una tarea representativa.

**Hook:** ¿hay una comprobación que deba ejecutarse en un evento concreto, independientemente de que el agente se acuerde de pedirla? Si la respuesta es sí, implementa un hook sencillo, seguro y documentado. Empieza con una comprobación no destructiva; revisa qué evento lo dispara, qué datos recibe y qué permisos necesita.

Si no hay una justificación suficiente, deja estos mecanismos sin configurar y registra la decisión. No simules un hook mediante instrucciones en lenguaje natural ni confundas un agente especializado con un subagente que la herramienta delega en tiempo de ejecución.

### 6. Revisar ajustes y permisos

Inspecciona la configuración de la herramienta y establece el mínimo acceso necesario para el ejercicio.

- Limita comandos y herramientas a los necesarios.
- No guardes tokens, contraseñas ni claves en instrucciones, skills o archivos versionados.
- No habilites acceso a red, MCP, despliegues ni operaciones destructivas si la tarea no los necesita.
- Comprueba qué archivos de configuración son compartidos por el equipo y cuáles son locales o personales.
- Documenta las diferencias entre configuración versionada y configuración externa al repositorio.

No copies ajustes de ejemplo sin comprender sus efectos. Los nombres, formatos y opciones dependen del producto y de su versión.

### 7. Validar con pruebas controladas

Usa al menos dos peticiones: una que deba activar las instrucciones o el mecanismo creado y otra que permita comprobar sus límites. Antes de ejecutar acciones, pide al asistente que explique qué instrucciones aplican y qué comprobaciones realizará.

Verifica:

- que utiliza comandos y convenciones reales;
- que la regla se aplica al ámbito correcto;
- que la skill sigue su procedimiento y criterios de finalización;
- que agentes y hooks, si existen, respetan sus límites;
- que no intenta acceder a secretos ni ejecutar acciones fuera del alcance;
- que las pruebas y comprobaciones producen resultados observables.

Revisa el diff y el estado de Git. Repite el ajuste y la validación si encuentras instrucciones contradictorias, mecanismos que no se activan o permisos excesivos.

## Entregables

- Matriz de decisiones: mecanismos implementados, pospuestos o descartados y motivo.
- Archivos de instrucciones y configuración necesarios para las herramientas elegidas.
- Al menos una skill probada con una tarea representativa.
- Una regla específica validada cuando exista una necesidad real; si no, justificación de su ausencia.
- Decisión documentada sobre agente especializado y hooks.
- Registro breve de las pruebas de validación, incidencias y ajustes.
- Diff revisado y estado final de Git.

## Flujo de trabajo

```mermaid
flowchart TD
    A["Recuperar el diagnóstico del lab. 03"] --> B["Identificar necesidades y elegir herramienta"]
    B --> C["Diseñar la configuración mínima"]
    C --> D["Crear instrucciones persistentes"]
    D --> E["Añadir reglas y skills cuando aporten valor"]
    E --> F["Evaluar agentes, hooks y permisos"]
    F --> G["Probar con tareas controladas"]
    G --> H{"¿Se comporta según lo esperado?"}
    H -- "Sí" --> I["Revisar diff y documentar decisiones"]
    H -- "No" --> J["Corregir instrucciones o configuración"]
    J --> G
    I --> K["Entorno validado para el proyecto"]
```

## Criterios de aceptación

- Cada mecanismo implementado responde a una necesidad identificada y documentada.
- Las instrucciones no inventan arquitectura, comandos ni convenciones.
- Las reglas tienen un ámbito explícito y no se aplican indiscriminadamente.
- La skill incluye un procedimiento comprobable y se ha probado.
- Agentes especializados y hooks se incorporan solo si están justificados y soportados por la herramienta.
- Los permisos son proporcionales a la tarea; no se versionan secretos.
- Las diferencias entre herramientas están documentadas y verificadas en sus fuentes oficiales.
- La validación deja evidencias observables, y el diff y el estado final de Git se han revisado.

## Fuentes oficiales para consultar antes de configurar

La disponibilidad de cada mecanismo depende de la herramienta, la interfaz, la versión y, en algunos casos, el plan. Consulta la documentación del producto concreto antes de implementar:

- [GitHub Copilot: guía comparativa de opciones de personalización](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)
- [GitHub Copilot: tipos de instrucciones y compatibilidad](https://docs.github.com/en/copilot/reference/custom-instructions-support)
- [Claude Code: memoria e instrucciones del proyecto](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Claude Code: skills](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code: hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code: subagentes](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Cursor: documentación](https://docs.cursor.com/)
- [Codex: documentación](https://developers.openai.com/codex/)
- [Formato AGENTS.md](https://github.com/agentsmd/agents.md)

## Regla de trabajo

Configura solo lo que puedas explicar, probar y mantener. Un entorno con instrucciones breves, una skill útil y permisos bien definidos es preferible a una colección de archivos redundantes que nadie valida.
