# Guía de contribución

Esta guía explica cómo proponer, preparar y revisar cambios en **AI-Assisted Development Guide**. El objetivo es mantener una referencia práctica, verificable y agnóstica respecto a proveedores para el desarrollo de software asistido por IA.

## Qué contribuciones buscamos

Son bienvenidas las contribuciones que mejoren la utilidad, exactitud o mantenibilidad de la guía:

- Correcciones de errores, enlaces rotos y problemas de claridad.
- Mejoras de los itinerarios de aprendizaje, metodologías y ejercicios del laboratorio.
- Nuevos conceptos, prácticas, criterios de decisión o casos de uso que cubran una necesidad identificable.
- Comparativas entre herramientas y proveedores sustentadas en documentación verificable.
- Mejoras de seguridad, privacidad, revisión humana, pruebas y gobierno del desarrollo asistido por IA.
- Actualizaciones de documentación que haya quedado obsoleta.

Antes de proponer un tema nuevo, revisa el [mapa de contenidos](docs/mapa-contenidos.md), el [glosario](docs/glosario.md), las [referencias de herramientas](docs/referencias-herramientas.md), los [primeros pasos](docs/primeros-pasos.md) y el [laboratorio](laboratorio/README.md). Evita duplicar contenido que ya tenga una ubicación adecuada.

## Principios editoriales

Toda contribución debe respetar estos criterios:

1. **Priorizar la metodología.** Explica qué problema resuelve una práctica, cuándo aplicarla, cómo verificarla y cuáles son sus límites. Evita convertir la guía en un catálogo de productos.
2. **Mantener el agnosticismo tecnológico.** Describe primero el concepto general y añade equivalencias entre herramientas cuando existan. No presupongas que dos funciones con nombres similares son equivalentes.
3. **Usar fuentes primarias.** Para funciones, configuraciones, precios, planes o límites de herramientas, prioriza documentación oficial y repositorios originales. Añade enlaces directos a las fuentes relevantes.
4. **Distinguir hechos de interpretación.** Identifica recomendaciones, ejemplos e inferencias como tales. Señala las incertidumbres y las diferencias entre proveedores.
5. **Evitar afirmaciones absolutas sin respaldo.** En particular, distingue entre modelos propietarios, modelos con pesos abiertos y software de código abierto; no los trates como categorías intercambiables.
6. **Redactar de forma clara y concisa.** Usa español técnico comprensible, títulos descriptivos, ejemplos mínimos reproducibles y enlaces relativos para documentos del repositorio.
7. **Controlar la vigencia.** Cuando una afirmación pueda cambiar con rapidez, indica la fecha de consulta o revisión y evita duplicar información cambiante si basta con enlazar la fuente oficial.

## Flujo de contribución

### 1. Identificar y delimitar el cambio

- Consulta los documentos relacionados y las incidencias abiertas para evitar duplicidades.
- Para cambios sustanciales, abre una incidencia o discusión antes de redactar. Expón el problema, el público destinatario, el resultado esperado y los documentos que podrían verse afectados.
- Para correcciones pequeñas y evidentes, puedes preparar directamente una propuesta.

### 2. Preparar los cambios

Si trabajas localmente, utiliza una rama descriptiva basada en la rama principal actualizada:

```bash
git switch main
git pull --ff-only
git switch -c docs/descripcion-breve
```

Sustituye `main` por el nombre real de la rama principal si el repositorio utiliza otro. Si no tienes permisos de escritura, trabaja en un fork y envía una solicitud de integración (*pull request*).

Realiza cambios acotados y coherentes. Mantén separadas las modificaciones no relacionadas para que puedan revisarse de forma independiente.

El proyecto de `laboratorio/04-configuracion-entorno-ia/project/` es una réplica de `laboratorio/03-proyecto-existente/project/` más su `AGENTS.md`. Si modificas el código, las pruebas o la configuración del proyecto del laboratorio 03, aplica el mismo cambio en la réplica y revisa que `AGENTS.md` siga siendo correcto.

### 3. Validar el contenido

Antes de enviar la propuesta, comprueba:

- [ ] El cambio resuelve una necesidad concreta y no duplica documentación existente.
- [ ] Las afirmaciones técnicas importantes tienen fuentes adecuadas y accesibles.
- [ ] Los enlaces relativos apuntan a archivos existentes y los enlaces externos funcionan.
- [ ] La estructura Markdown es correcta y los encabezados mantienen una jerarquía lógica.
- [ ] Las comparativas distinguen los principios generales de las particularidades de cada herramienta.
- [ ] Los ejemplos se han revisado y no contienen credenciales, datos personales ni información confidencial.
- [ ] Se han actualizado los índices o documentos relacionados cuando corresponde.
- [ ] El diff no incluye cambios accidentales ni archivos temporales.

Para cambios exclusivamente documentales, no inventes pruebas automatizadas que el repositorio no tenga configuradas. La revisión manual de enlaces, estructura, referencias y coherencia es el mínimo esperado.

### 4. Registrar y enviar la propuesta

Usa un título breve que describa el cambio. Si el proyecto ya utiliza una convención de mensajes de commit, síguela; no introduzcas una convención nueva sin acuerdo.

La solicitud de integración debe explicar:

- **Motivo:** qué problema o carencia se aborda.
- **Cambios:** qué documentos o secciones se han modificado.
- **Verificación:** qué comprobaciones se han realizado y cuáles no se han podido hacer.
- **Fuentes:** referencias primarias utilizadas, cuando proceda.
- **Seguimiento:** enlace a la incidencia relacionada, si existe.

Incluye capturas o ejemplos solo cuando ayuden a revisar el cambio. Mantén una única solicitud por objetivo principal y responde a las observaciones en esa misma conversación.

## Uso de asistentes y agentes de IA para contribuir

Se pueden utilizar asistentes y agentes para investigar, proponer estructuras, redactar, revisar enlaces o detectar inconsistencias. Su uso no sustituye la responsabilidad de quien contribuye.

- Verifica las afirmaciones y las referencias contra las fuentes originales.
- No aceptes automáticamente cambios de código, comandos, configuraciones o recomendaciones de seguridad generados por un modelo.
- No proporciones a herramientas de IA secretos, credenciales, datos de clientes ni información confidencial.
- Revisa el diff completo y explica las limitaciones de las comprobaciones realizadas.
- No atribuyas a una fuente afirmaciones que esta no respalde.

## Revisión y aceptación

Las propuestas se revisarán según su pertinencia, exactitud, trazabilidad de las fuentes, coherencia editorial, ausencia de duplicidades y facilidad de mantenimiento. Los cambios que afecten a la estructura de la guía o introduzcan un módulo nuevo pueden requerir una discusión previa.

Una solicitud enviada no implica su aceptación ni que el contenido ya forme parte de la guía. Las personas mantenedoras pueden pedir aclaraciones, proponer ajustes o cerrar una propuesta que no encaje con los objetivos del proyecto.

## Documentación relacionada

- [README](README.md): punto de entrada a la guía.
- [Mapa de contenidos](docs/mapa-contenidos.md): organización temática.
- [Primeros pasos](docs/primeros-pasos.md): itinerario inicial.
- [Laboratorio](laboratorio/README.md): ejercicios prácticos.
- [Referencias de herramientas](docs/referencias-herramientas.md): fuentes oficiales y equivalencias.
- [Roadmap](ROADMAP.md): mejoras y contenidos pendientes.

## Referencia general

El flujo de ramas, commits y solicitudes de integración sigue las prácticas habituales de colaboración en GitHub. Consulta la [documentación oficial para contribuir a proyectos de código abierto](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source) para conocer los detalles de la plataforma.
