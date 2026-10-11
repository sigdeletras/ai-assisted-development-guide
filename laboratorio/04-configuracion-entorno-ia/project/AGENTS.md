# poi-app

## Proyecto

Paquete Python que construye puntos de interés como entidades GeoJSON `Point` (RFC 7946). La estructura de archivos está en `README.md`; la incidencia abierta y sus criterios de aceptación, en `docs/incidencia.md`.

## Comandos

Desde la raíz del proyecto, con Python 3.11 o posterior:

- Instalar herramientas de desarrollo: `python -m pip install -e ".[dev]"`
- Pruebas: `python -m pytest`
- Lint: `python -m ruff check .`
- Formato (solo comprobar): `python -m ruff format --check .`
- Tipos: `python -m mypy`

La configuración de las herramientas está en `pyproject.toml`.

## Convenciones

- Las coordenadas siguen el orden GeoJSON `[longitude, latitude]`.
- El código debe pasar `mypy` en modo estricto: anota los tipos de funciones y pruebas.
- Longitud de línea y reglas de lint: las definidas en `pyproject.toml`; no las cambies.

## Pruebas

- Todo cambio de comportamiento debe ir acompañado de pruebas nuevas; las asociadas a incidencias van en `tests/test_regression.py`.
- Las pruebas de `tests/test_geojson.py` describen el comportamiento actual, no el deseado. Para el comportamiento esperado, consulta `docs/incidencia.md`.
- No modifiques pruebas existentes para que pasen. Si una prueba parece incorrecta, explícalo antes de cambiarla.

## Límites

- No añadas dependencias ni modifiques la configuración de `pyproject.toml` sin consultarlo.
- Limita los cambios a la tarea solicitada; no refactorices el módulo ni cambies la estructura de la entidad GeoJSON para entradas válidas.

## Antes de dar una tarea por terminada

- Ejecuta las pruebas, el lint, la comprobación de formato y mypy, y resume el resultado.
- Indica qué no has podido verificar y por qué.
- Revisa el diff y confirma que solo incluye cambios relacionados con la tarea.

## Git

- No hagas commit ni push sin que se te pida.
- Antes de proponer un commit, muestra `git status` y el diff, y confirma que las comprobaciones anteriores pasan.

## Seguridad

- No leas, muestres ni versiones archivos `.env` ni credenciales.
- No ejecutes comandos con acceso a red salvo la instalación de dependencias ya declaradas.
