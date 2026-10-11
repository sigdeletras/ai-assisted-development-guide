# Instrucciones persistentes del proyecto

Las instrucciones persistentes son un archivo versionado en el repositorio que el asistente carga al empezar a trabajar. Sirven para que no tengas que repetir en cada conversación cómo se prueba el proyecto, qué convenciones sigue y qué límites debe respetar.

Este documento explica qué incluir, cómo elegir el archivo según las herramientas y cómo comprobar que funciona. Las reglas por ruta, las skills, los hooks y los permisos se tratan en el [laboratorio 04](../laboratorio/04-configuracion-entorno-ia/README.md).

## Qué son y qué no son

Un archivo de instrucciones expresa **expectativas generales** que se aplican a casi cualquier tarea del proyecto. No sustituye a otros mecanismos:

| Mecanismo | Para qué sirve | Ejemplo |
| --- | --- | --- |
| Prompt | Una tarea concreta en una conversación. | «Añade validación de latitud a `build_feature`». |
| Instrucciones persistentes | Contexto y normas que valen para casi todas las tareas. | «Ejecuta `python -m pytest` antes de dar un cambio por terminado». |
| Reglas por ruta (*rules*) | Normas que solo aplican a ciertos directorios o tipos de archivo. | Convenciones de las migraciones de base de datos. |
| Skill | Un procedimiento con pasos que se activa cuando la tarea lo requiere. | Flujo para preparar una versión. |
| Hook | Una acción que la herramienta ejecuta automáticamente ante un evento. | Formatear un archivo después de editarlo. |
| Permisos | Lo que la herramienta puede o no puede hacer. | Prohibir comandos de red o la escritura fuera del repositorio. |

Las instrucciones son orientaciones: el modelo las tiene en cuenta, pero no garantizan su cumplimiento. Si algo debe cumplirse siempre, como no leer `.env` o ejecutar el formateador, utiliza permisos, hooks o la CI.

## Qué incluir

Incluye solo información que el asistente necesite con frecuencia y que no pueda deducir con facilidad del código:

- **Propósito y estructura**, en pocas líneas: qué hace el proyecto y dónde está cada cosa.
- **Comandos reales** para instalar, probar, analizar y formatear, copiados de la documentación o configuración del proyecto y comprobados.
- **Convenciones observadas** que no son evidentes: orden de coordenadas, formato de errores, nombres de ramas.
- **Límites de alcance**: no modificar archivos generados, no añadir dependencias sin consultar, no cambiar las pruebas para que pasen.
- **Criterio de terminado**: qué comprobaciones deben pasar y cómo comunicar lo que no se ha podido verificar.
- **Restricciones de seguridad**: archivos que no se deben leer ni modificar y tratamiento de secretos.

Cada línea debe ser **comprobable**: si no puedes señalar el archivo o la salida que la respalda, no la incluyas todavía.

## Qué no incluir

- Secretos, credenciales, URL internas o datos personales. El archivo se versiona y se envía al proveedor del modelo.
- Lo que el asistente ya deduce del código: el lenguaje, la lista completa de archivos o la API de cada función.
- Consejos genéricos como «escribe código limpio» o «sigue buenas prácticas»: no cambian el comportamiento y ocupan contexto.
- Convenciones deseadas que el proyecto aún no cumple. Si las escribes como hechos, el asistente las aplicará de forma inconsistente.
- Documentación extensa que ya existe. Remite a ella con una ruta en lugar de copiarla.
- Contenido generado por el propio asistente sin revisar. Validar sus propuestas es parte del trabajo.

Como referencia práctica, un archivo que no cabe en una pantalla o dos suele contener información que debería estar en otro sitio.

## Elegir el archivo según las herramientas

Cada herramienta lee archivos distintos. Consulta la [tabla de equivalencias](referencias-herramientas.md#equivalencias-orientativas) y, antes de crear nada, la documentación oficial vigente de las herramientas que realmente vais a utilizar.

Criterios:

1. **Parte de las herramientas que usa el equipo**, no de una lista de todos los formatos posibles.
2. **Si solo usáis una herramienta**, utiliza su archivo propio.
3. **Si usáis varias**, mantén una sola fuente de contenido. `AGENTS.md` es un formato abierto que leen varias herramientas; las que usan su propio archivo pueden remitir a él cuando lo admitan.
4. **No dupliques contenido**. Dos archivos con las mismas instrucciones acaban divergiendo y el asistente recibe indicaciones contradictorias.

## El formato AGENTS.md

[AGENTS.md](https://agents.md/) es un formato abierto que funciona como un «README para agentes»: reúne el contexto que necesita un agente de programación y que sobrecargaría el README dirigido a personas. Lo mantiene la Agentic AI Foundation, dentro de la Linux Foundation, y lo leen herramientas como Codex, Cursor, GitHub Copilot, VS Code, Gemini CLI o Claude Code.

Según la guía oficial del formato:

- **No tiene campos obligatorios.** Es Markdown estándar y admite cualquier encabezado; el agente interpreta el texto.
- **Se crea en la raíz del repositorio.**
- **Temas recomendados:** descripción del proyecto, comandos de compilación y pruebas, estilo de código, instrucciones de pruebas y consideraciones de seguridad.
- **Temas adicionales útiles:** convenciones de commits y pull requests, particularidades de seguridad, conjuntos de datos grandes y pasos de despliegue; en general, lo que contarías a una persona nueva en el equipo.
- **Archivos anidados:** en monorepos, cada subproyecto puede tener su propio `AGENTS.md`. Prevalece el más cercano al archivo que se edita.
- **Prioridad:** las peticiones explícitas en el chat prevalecen sobre cualquier `AGENTS.md`. Por eso no sirve para imponer límites de seguridad.
- **Comandos:** si el archivo incluye comandos de comprobación, el agente intentará ejecutarlos y corregir los fallos antes de terminar. Incluye solo comandos reales y verificados.
- **Mantenimiento:** es documentación viva; actualízala cuando cambie el proyecto.
- **Migración:** si el proyecto ya tenía otro archivo de instrucciones, la guía propone renombrarlo a `AGENTS.md` y dejar un enlace simbólico con el nombre antiguo.

No dupliques el README. Remite a él para la estructura o la instalación detallada y reserva `AGENTS.md` para lo que el agente necesita para trabajar: comandos, convenciones, límites y criterio de terminado.

### Una fuente común para varias herramientas

Cuando el equipo usa varias herramientas, `AGENTS.md` es la fuente común. Cada herramienta lo carga a su manera; comprueba el comportamiento en su documentación oficial antes de añadir archivos propios:

- **GitHub Copilot:** admite uno o varios `AGENTS.md` en cualquier lugar del repositorio; prevalece el más cercano en el árbol de directorios. Convive con `.github/copilot-instructions.md`.
- **Claude Code:** desde la versión 2.1.277 lee `AGENTS.md` como instrucciones del proyecto **si no hay** `CLAUDE.md`, `.claude/CLAUDE.md` ni `CLAUDE.local.md` en el directorio de trabajo o por encima. Si existe alguno de ellos, carga solo los `CLAUDE.md`, salvo que se cambie el ajuste **Project instructions**.

Si necesitas instrucciones específicas de Claude Code, o trabajas en una sesión que no puede leer `AGENTS.md` directamente, crea un `CLAUDE.md` que lo importe:

```markdown
<!-- CLAUDE.md -->
@AGENTS.md

<!-- Solo instrucciones específicas de Claude Code a partir de aquí, si las hay. -->
```

La sintaxis `@ruta` es propia de Claude Code. Un `CLAUDE.md` que solo diga «lee AGENTS.md» con palabras no equivale a importarlo: el agente solo verá el archivo si decide abrirlo. Ten en cuenta también que crear un `CLAUDE.local.md` personal desactiva la lectura directa de `AGENTS.md`.

## Ejemplo orientativo

El siguiente archivo corresponde a un proyecto **ficticio**. Muestra la forma y el nivel de detalle, no un contenido para copiar: tus instrucciones deben derivarse de tu propio inventario y de la línea base del proyecto.

```markdown
# AGENTS.md

## Proyecto
Visor web de rutas turísticas. Frontend TypeScript (Vite) en `web/`;
API de datos en Python (FastAPI) en `api/`. Arquitectura en `docs/arquitectura.md`.

## Comandos
- Frontend: `npm ci`, `npm run test`, `npm run lint` (desde `web/`).
- API: `python -m pip install -e ".[dev]"`, `python -m pytest`, `python -m ruff check .` (desde `api/`).

## Convenciones
- Coordenadas en orden `[longitud, latitud]` (GeoJSON, EPSG:4326) en todo el código.
- Los errores de la API se devuelven con el esquema de `api/src/errors.py`; no crear formatos nuevos.

## Límites
- No modificar `web/src/generated/`: se genera con `npm run codegen`.
- No añadir dependencias ni cambiar la configuración de lint sin consultarlo.
- No modificar pruebas existentes para que pasen; si una prueba parece incorrecta, explícalo.

## Pruebas
- Todo cambio de comportamiento incluye pruebas nuevas junto al código afectado.

## Antes de dar una tarea por terminada
- Ejecuta las pruebas y el lint del componente afectado y resume el resultado.
- Indica qué no has podido verificar.

## Commits y pull requests
- Mensajes con el formato `tipo(ámbito): resumen` (Conventional Commits).
- No hagas commit ni push sin que se te pida.

## Seguridad
- No leer ni mostrar `.env` ni `api/config/secrets/`.
```

Observa que cada línea es concreta, se puede verificar y remite a una ruta cuando el detalle está en otro sitio.

## Comprobar que la herramienta lo aplica

Crear el archivo no garantiza que se use. Antes de darlo por válido:

1. **Confirma que se carga.** Inicia una sesión nueva y pregunta qué comandos de prueba debe usar en el proyecto o qué límites tiene. Algunas herramientas muestran además qué archivos han cargado; por ejemplo, en Claude Code, `/context` los lista en **Memory files**.
2. **Pruébalo con una tarea de planificación.** Pide un plan para una incidencia pequeña y comprueba que propone los comandos y límites documentados.
3. **Prueba un límite.** Pide algo que el archivo prohíbe y verifica que el asistente lo señala.
4. **Revisa el estado de Git** después de la prueba para confirmar que no hay cambios no solicitados.

Si el asistente ignora una instrucción, revisa si es ambigua, si contradice otra o si está enterrada en un archivo demasiado largo antes de añadir más texto.

## Mantenimiento

- Trata el archivo como código: se versiona, se revisa en los pull requests y tiene responsable.
- Actualízalo cuando cambien los comandos, la estructura o las convenciones.
- Cuando el asistente repita un mismo error, valora si falta una instrucción. Añádela solo si es general; si afecta a una parte del código, considera una regla por ruta.
- Elimina instrucciones que ya no se cumplen o que nadie sabe justificar.

## Relación con el resto de la guía

- [Glosario](glosario.md): definiciones de AGENTS.md, CLAUDE.md, rules y skills.
- [Referencias de herramientas](referencias-herramientas.md): equivalencias entre productos y enlaces a la documentación oficial.
- Documentación oficial: [AGENTS.md](https://agents.md/), [Claude Code: CLAUDE.md y AGENTS.md](https://code.claude.com/docs/en/memory#agents-md) y [GitHub Copilot: instrucciones del repositorio](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md): tratamiento de secretos y datos en archivos de instrucciones.
- [Laboratorio 03](../laboratorio/03-proyecto-existente/README.md): crear las instrucciones mínimas a partir del análisis de un proyecto existente.
- [Laboratorio 04](../laboratorio/04-configuracion-entorno-ia/README.md): ampliar la configuración con reglas por ruta, skills, hooks y permisos.
