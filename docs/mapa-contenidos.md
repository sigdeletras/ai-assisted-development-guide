# Mapa de contenidos

Índice de consulta de la guía. **No es un curso obligatorio:** empieza por [Primeros pasos](primeros-pasos.md) y consulta cada módulo cuando tengas una necesidad concreta.

## Vista general

```mermaid
flowchart TB
    M1["1 · Fundamentos"]
    M2["2 · Contexto e instrucciones"]
    M3["3 · Agentes y herramientas"]
    M4A["4A · Ingeniería y calidad"]
    M4B["4B · Seguridad y control"]
    M5["5 · Gobierno y evaluación"]
    M1 --> M2 --> M3 --> M4A
    M4A --- M4B
    M4B --> M5
    classDef fundamentos fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
    classDef contexto fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef agentes fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef ingenieria fill:#ede9fe,stroke:#7c3aed,color:#4c1d95
    classDef seguridad fill:#fee2e2,stroke:#dc2626,color:#7f1d1d
    classDef gobierno fill:#f3e8ff,stroke:#a21caf,color:#701a75
    class M1 fundamentos
    class M2 contexto
    class M3 agentes
    class M4A ingenieria
    class M4B seguridad
    class M5 gobierno
```

## Módulos

### 1. Fundamentos del desarrollo asistido
- [Primeros pasos](primeros-pasos.md)
- [Glosario de términos](glosario.md)
- [Laboratorio 01: primer contacto](../laboratorio/01-primer-contacto/README.md)
- [Laboratorio 02: proyecto nuevo](../laboratorio/02-proyecto-nuevo/README.md)
- [Laboratorio 05: desarrollo de una funcionalidad con IA](../laboratorio/05-desarrollo-funcionalidad-ia/README.md)

### 2. Contexto e instrucciones
- [Referencias de herramientas](referencias-herramientas.md)
- [Diseño de ejercicios](estructura-ejercicios.md)
- [Laboratorio 03: proyecto existente](../laboratorio/03-proyecto-existente/README.md)
- [Laboratorio 04: configuración del entorno de IA](../laboratorio/04-configuracion-entorno-ia/README.md)

### 3. Agentes, herramientas y automatización
Agentes y subagentes, skills, hooks, MCP, permisos y delegación de tareas. No es necesario activar todos los mecanismos.
- [Glosario de términos](glosario.md)
- [Referencias de herramientas](referencias-herramientas.md)
- [Laboratorio 04: configuración del entorno de IA](../laboratorio/04-configuracion-entorno-ia/README.md)
- [Laboratorio 05: desarrollo de una funcionalidad con IA](../laboratorio/05-desarrollo-funcionalidad-ia/README.md)

### 4A. Ingeniería del software y calidad
Pruebas, revisión de cambios, análisis estático, CI, *harness engineering* y *Spec-Driven Development*.
- [Primeros pasos: flujo de revisión](primeros-pasos.md)
- [Glosario de términos](glosario.md)
- [Laboratorio 01](../laboratorio/01-primer-contacto/README.md)
- [Laboratorio 02](../laboratorio/02-proyecto-nuevo/README.md)
- [Laboratorio 03](../laboratorio/03-proyecto-existente/README.md)
- [Laboratorio 05: desarrollo de una funcionalidad con IA](../laboratorio/05-desarrollo-funcionalidad-ia/README.md)

### 4B. Seguridad, privacidad y control de cambios
Protección de datos y secretos, permisos mínimos, prompt injection, revisión humana y límites de autonomía.
- [Seguridad y privacidad al programar con IA](seguridad-privacidad-ia.md)
- [Glosario de términos](glosario.md)
- [Primeros pasos: seguridad y responsabilidad](primeros-pasos.md)
- [Referencias de herramientas](referencias-herramientas.md)
- [Laboratorio 04](../laboratorio/04-configuracion-entorno-ia/README.md)
- [Laboratorio 05: desarrollo de una funcionalidad con IA](../laboratorio/05-desarrollo-funcionalidad-ia/README.md)

### 5. Gobierno, evaluación y mejora continua
- [Criterios de la guía](../README.md#principios)
- [Glosario de términos](glosario.md)
- [Referencias de herramientas](referencias-herramientas.md)
- [Laboratorio: recorrido completo](../laboratorio/README.md)

## Proyectos y ejercicios de práctica

Los laboratorios pueden recorrerse de forma progresiva o consultarse por necesidad.

| Laboratorio | Objetivo | Referencia |
| --- | --- | --- |
| 01 · Primer contacto | Practicar chat, autocompletado y cambios pequeños. | [Abrir laboratorio 01](../laboratorio/01-primer-contacto/README.md) |
| 02 · Proyecto nuevo | Convertir requisitos en un proyecto estructurado, con pruebas y API REST. | [Abrir laboratorio 02](../laboratorio/02-proyecto-nuevo/README.md) |
| 03 · Proyecto existente | Analizar el repositorio y establecer la línea base. | [Abrir laboratorio 03](../laboratorio/03-proyecto-existente/README.md) |
| 04 · Configuración del entorno de IA | Crear y validar instrucciones, rules y skills; evaluar agentes, hooks y permisos. | [Abrir laboratorio 04](../laboratorio/04-configuracion-entorno-ia/README.md) |
| 05 · Desarrollo de una funcionalidad con IA | Especificar, confirmar el plan, implementar por incrementos y validar. | [Abrir laboratorio 05](../laboratorio/05-desarrollo-funcionalidad-ia/README.md) |

## Cómo está organizada la documentación
- **Guía:** conceptos, criterios de decisión y riesgos.
- **Laboratorio:** ejercicios y proyectos con resultados verificables.
- **Referencias de herramientas:** enlaces oficiales específicos de cada proveedor.

El estado de desarrollo de nuevos contenidos se debe gestionar como trabajo editorial, no como una lista de tareas dentro de este índice.
