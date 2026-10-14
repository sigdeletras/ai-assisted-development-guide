# Guía de contribución

El objetivo es mantener una guía práctica, verificable y agnóstica respecto a proveedores.

## Qué aportar

- Correcciones de errores, enlaces rotos y contenido obsoleto.
- Mejoras en metodologías, itinerarios y laboratorios.
- Conceptos o casos de uso que cubran una necesidad identificada.
- Comparativas basadas en fuentes verificables.
- Mejoras de seguridad, privacidad, pruebas y gobierno.

Antes de crear contenido, consulta el [mapa](docs/mapa-contenidos.md), el [glosario](docs/glosario.md), las [referencias de herramientas](docs/referencias-herramientas.md) y el [laboratorio](laboratorio/README.md). Evita duplicidades.

## Criterios editoriales

- Explica el problema que resuelve una práctica, cuándo usarla y cómo verificarla.
- Describe primero el concepto general; después, las equivalencias y diferencias entre herramientas.
- Prioriza documentación oficial y repositorios originales.
- Distingue hechos, recomendaciones e incertidumbres.
- No confundas software de código abierto, modelos de pesos abiertos y modelos propietarios.
- Escribe de forma concisa. Usa ejemplos mínimos y enlaces relativos para documentos del repositorio.
- Comprueba la vigencia de funciones, planes, configuraciones y garantías que puedan cambiar.

## Flujo de trabajo

1. **Delimita el cambio.** Identifica el problema, el público, el resultado esperado y los archivos afectados. Para cambios estructurales, abre primero una incidencia o discusión.
2. **Prepara una propuesta acotada.** Mantén separados los cambios no relacionados. Trabaja en una rama basada en la principal actualizada; si no tienes permisos, usa un fork.
3. **Valida.** Comprueba enlaces, estructura Markdown, referencias, coherencia con documentos relacionados y seguridad de los ejemplos.
4. **Revisa el diff.** Elimina cambios accidentales, archivos temporales, credenciales y datos confidenciales.
5. **Explica el resultado.** Indica motivo, archivos modificados, comprobaciones realizadas, limitaciones y fuentes relevantes.

Comandos habituales para una rama de documentación:

```bash
git switch main
git pull --ff-only
git switch -c docs/descripcion-breve
```

Sustituye `main` por el nombre real de la rama principal si es distinto. No introduzcas convenciones de commits nuevas sin acuerdo.

### Laboratorios relacionados

El proyecto de `laboratorio/04-configuracion-entorno-ia/project/` replica el de `laboratorio/03-proyecto-existente/project/` y añade `AGENTS.md`. Si cambias código, pruebas o configuración del laboratorio 03, revisa si el mismo cambio debe aplicarse a la réplica.

## Seguridad al contribuir con IA

- Verifica las afirmaciones contra las fuentes originales.
- No compartas secretos, credenciales, datos de clientes ni información confidencial con herramientas no autorizadas.
- Revisa comandos, permisos, cambios de código y el diff completo.
- No atribuyas a una fuente afirmaciones que no respalde.

## Revisión y aceptación

Las propuestas se valoran por utilidad, exactitud, fuentes, coherencia editorial, ausencia de duplicidades y coste de mantenimiento. Una propuesta o pull request enviada no implica aceptación ni incorporación a la guía; puede requerir cambios o rechazarse.

## Documentación relacionada

- [README](README.md): punto de entrada.
- [Mapa de contenidos](docs/mapa-contenidos.md): organización temática.
- [Primeros pasos](docs/primeros-pasos.md): flujo inicial.
- [Laboratorio](laboratorio/README.md): ejercicios prácticos.
- [Referencias de herramientas](docs/referencias-herramientas.md): fuentes oficiales y equivalencias.
- [Roadmap](ROADMAP.md): propuestas evaluadas pendientes.

Para el funcionamiento de ramas y pull requests, consulta la [documentación oficial de GitHub para contribuir a proyectos de código abierto](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source).
