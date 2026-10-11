# LLM: familias de modelos, distribución y criterios de selección

Este documento ofrece una referencia conceptual sobre las principales familias de modelos de lenguaje (LLM), sus modalidades de distribución y los criterios para elegirlos en proyectos de desarrollo asistido por IA. No es un ranking de rendimiento ni un catálogo de lanzamientos.

La guía prioriza conceptos duraderos y documentación primaria. Las familias, licencias y modalidades de acceso pueden cambiar; verifica siempre las condiciones del modelo concreto antes de adoptarlo.

## 1. Qué estamos comparando

Conviene distinguir estos elementos:

- **Modelo:** sistema entrenado que genera o transforma contenido; puede ser de lenguaje o multimodal.
- **Familia de modelos:** conjunto de modelos relacionados publicados por una organización.
- **Proveedor o desarrollador:** organización que crea o distribuye el modelo.
- **Servicio de inferencia:** infraestructura que permite consultar un modelo, por ejemplo mediante una API.
- **Aplicación o herramienta:** producto que utiliza uno o varios modelos, como un asistente de programación o una extensión de IDE.

Un proveedor puede ofrecer modelos propietarios y otros con pesos disponibles. Una aplicación puede cambiar de modelo según el plan, la configuración o la tarea. Por tanto, no debe atribuirse una única modalidad de distribución a toda una empresa.

## 2. Modalidades de disponibilidad

Los términos no son intercambiables:

| Categoría | Criterio de lectura | Qué comprobar |
| --- | --- | --- |
| **Propietario** | El modelo se ofrece mediante un servicio controlado o bajo condiciones de uso propias y sus pesos no se distribuyen públicamente. | Condiciones del servicio, acceso, tratamiento de datos y restricciones de uso. |
| **Pesos abiertos** (*open weights*) | Los pesos entrenados pueden descargarse o redistribuirse conforme a una licencia. | Licencia, usos permitidos, atribución, redistribución, restricciones comerciales y disponibilidad de otros componentes. |
| **Código abierto para IA** (*open source AI*) | El sistema satisface los criterios de una definición de código abierto para IA, no solo la disponibilidad de los pesos. | Componentes publicados, información suficiente para modificar el sistema, licencia y cumplimiento de la definición aplicable. |
| **Mixto / variable** | Una organización o familia distribuye distintos modelos con condiciones diferentes. | La ficha y licencia de cada modelo o distribución concreta. |

La **disponibilidad de los pesos no implica por sí sola que el modelo sea de código abierto**. Puede que no se publiquen los datos de entrenamiento, el código, la información necesaria para reproducir el entrenamiento o que la licencia imponga restricciones.

Como referencia conceptual, consultar la [Open Source AI Definition 1.0 de la Open Source Initiative (OSI)](https://opensource.org/ai). Para una decisión real, leer también la licencia y la ficha oficial de la distribución específica. No clasificar una familia completa basándose únicamente en un modelo.

## 3. Principales familias y organizaciones

La siguiente tabla es una orientación de cobertura, no una certificación de licencias. La modalidad indicada es general y debe comprobarse para cada modelo antes de usarlo.

| Organización | Familia o referencia | Orientación de disponibilidad | Fuente oficial |
| --- | --- | --- | --- |
| OpenAI | GPT y modelos relacionados | Oferta principalmente propietaria; también publica modelos con pesos abiertos. Evaluar cada línea por separado. | [Modelos](https://platform.openai.com/docs/models) · [OpenAI](https://openai.com/) |
| Anthropic | Claude | Propietaria, accesible a través de sus productos y servicios autorizados. | [Documentación de Claude](https://docs.anthropic.com/) |
| Google | Gemini y Gemma | Gemini es una familia propietaria; Gemma ofrece modelos con pesos disponibles bajo sus propias condiciones. | [Gemini](https://ai.google.dev/gemini-api/docs) · [Gemma](https://ai.google.dev/gemma) |
| Meta | Llama | Pesos disponibles bajo licencias y condiciones específicas; no asumir que equivale a código abierto. | [Llama](https://www.llama.com/) |
| Mistral AI | Mistral y familias relacionadas | Oferta mixta: hay modelos y servicios con condiciones distintas. | [Documentación](https://docs.mistral.ai/) · [Modelos](https://mistral.ai/models) |
| DeepSeek | DeepSeek | Existen modelos con pesos disponibles y servicios alojados; comprobar la licencia del modelo concreto. | [DeepSeek](https://www.deepseek.com/) · [Organización en Hugging Face](https://huggingface.co/deepseek-ai) |
| Alibaba | Qwen | Diversas distribuciones con licencias que deben verificarse individualmente. | [Qwen](https://qwenlm.github.io/) · [Organización en Hugging Face](https://huggingface.co/Qwen) |
| Microsoft | Phi | Consultar la ficha y licencia de cada modelo publicado. | [Microsoft Phi](https://azure.microsoft.com/en-us/products/phi) |
| Cohere | Command y Aya | Combina servicios comerciales con modelos publicados bajo condiciones específicas. | [Documentación](https://docs.cohere.com/) · [Modelos](https://huggingface.co/CohereForAI) |

La lista es representativa, no exhaustiva. Se mantiene deliberadamente a nivel de familias para evitar que el documento dependa de nombres de versiones, fechas de lanzamiento o resultados de benchmarks.

## 4. Cómo documentar una familia o modelo

Cuando sea útil ampliar la tabla, utilizar una ficha breve y homogénea:

- **Organización:** desarrollador o entidad responsable de la publicación.
- **Familia o modelo:** nombre oficial, evitando usar una versión efímera como título principal.
- **Disponibilidad:** propietario, pesos abiertos, código abierto para IA o mixto, con el alcance claramente indicado.
- **Licencia y restricciones:** enlace a la licencia oficial de la distribución concreta.
- **Modalidades de uso:** API, aplicación, integración en un IDE, ejecución local o despliegue propio, cuando estén disponibles.
- **Orientación general:** programación, razonamiento, tareas generales, multimodalidad u otras capacidades relevantes, sin prometer un rendimiento universal.
- **Documentación oficial:** página de modelos, ficha técnica o repositorio mantenido por el desarrollador.
- **Última comprobación:** fecha de revisión de los datos variables.

No atribuir licencias, capacidades ni modalidades de ejecución a partir del nombre de una familia. Si una condición no está verificada, indicarlo expresamente.

## 5. Criterios para seleccionar un modelo

La elección debe partir de la tarea y de las restricciones del proyecto, no de una clasificación general.

| Criterio | Preguntas para la evaluación |
| --- | --- |
| Calidad para la tarea | ¿Resuelve el tipo de programación, análisis, documentación o razonamiento requerido? |
| Herramientas e integración | ¿Admite llamadas a herramientas, salidas estructuradas y la integración que necesita el entorno? |
| Contexto | ¿Puede manejar el volumen de instrucciones, código y documentación necesario? |
| Coste y latencia | ¿Cuál es el coste real por uso y el tiempo de respuesta en el flujo previsto? |
| Privacidad y seguridad | ¿Qué datos se envían, cómo se retienen y qué controles ofrece el proveedor o despliegue? |
| Licencia y uso | ¿Permite el uso comercial, la redistribución, el ajuste o el despliegue previsto? |
| Infraestructura | ¿Requiere servicio externo, GPU, memoria, operación y mantenimiento propios? |
| Evaluación | ¿Se ha probado con tareas representativas, criterios de aceptación y revisión humana? |

Para programación asistida, evaluar con tareas reales y verificables: comprensión de un repositorio, implementación de cambios acotados, generación y corrección de pruebas, revisión de código y documentación. Registrar el contexto, la configuración, los criterios de aceptación y las limitaciones; no confiar únicamente en benchmarks publicados.

## 6. Modalidad de uso y privacidad

Distinguir la modalidad de distribución del modelo de la forma en que se utiliza:

- **API alojada:** el proveedor opera la inferencia; revisar contrato, políticas de datos, retención, región y condiciones del servicio.
- **Aplicación o IDE:** puede incorporar modelos de uno o varios proveedores y aplicar políticas propias. No asumir que la privacidad depende solo del modelo seleccionado.
- **Ejecución local o infraestructura propia:** puede reducir la transmisión de datos a servicios externos, pero exige revisar telemetría, dependencias, controles de acceso, seguridad del equipo y licencia.
- **Despliegue de terceros:** aunque los pesos sean descargables, un servicio intermediario puede procesar las peticiones y aplicar sus propias condiciones.

La ejecución local no garantiza por sí sola privacidad, y los pesos abiertos no eliminan las obligaciones contractuales ni las restricciones de licencia. Para el tratamiento de información confidencial, consultar también [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md).

## 7. Mantenimiento del documento

El contenido está diseñado para mantenerse estable:

- No incluir rankings permanentes, puntuaciones de benchmarks ni precios como si fueran datos duraderos.
- No añadir cada versión o lanzamiento; registrar nuevas familias solo cuando aporten una modalidad de distribución, una organización o una capacidad relevante para la guía.
- Revisar los enlaces oficiales y la clasificación cuando cambien las condiciones de licencia o distribución.
- Fechar las comprobaciones de licencia y distinguir los datos verificados de las observaciones generales.
- Mantener los detalles de productos concretos y las comparativas de rendimiento en documentos separados, si llegan a ser necesarios.

## Referencias y relación con la guía

- [Mapa de contenidos](mapa-contenidos.md): ubicación de este documento dentro de la guía.
- [Herramientas de desarrollo asistido por IA](herramientas-desarrollo-ia.md): categorías de herramientas y productos.
- [Referencias de herramientas y documentación](referencias-herramientas.md): enlaces oficiales para aprender a utilizar asistentes concretos.
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md): tratamiento de datos, retención, permisos y riesgos.

**Nota de alcance:** este documento es una referencia conceptual. La tabla de familias no sustituye la comprobación de la licencia, ficha técnica y condiciones vigentes del modelo concreto antes de su adopción.
