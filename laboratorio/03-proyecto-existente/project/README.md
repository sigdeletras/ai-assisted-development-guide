# poi-app

Paquete Python para construir puntos de interés como entidades GeoJSON de tipo `Point` ([RFC 7946](https://www.rfc-editor.org/rfc/rfc7946)).

## Estructura

- `src/poi_app/geojson.py`: función `build_feature(name, longitude, latitude, properties=None)`.
- `tests/test_geojson.py`: pruebas de caracterización del comportamiento actual.
- `tests/test_regression.py`: pruebas de regresión asociadas a incidencias.
- `docs/incidencia.md`: incidencia abierta sobre validación de entradas.

Las coordenadas siguen el orden GeoJSON `[longitude, latitude]`.

## Requisitos

- Python 3.11 o posterior.

## Instalación

Desde este directorio, instala las herramientas de desarrollo (pytest, Ruff y mypy):

```bash
python -m pip install -e ".[dev]"
```

Los grupos `test` y `lint` de `pyproject.toml` permiten instalar solo una parte.

## Pruebas

```bash
python -m pytest
```

La configuración de pytest está en `pyproject.toml` (`testpaths = ["tests"]`, `pythonpath = ["src"]`), por lo que las pruebas también se pueden ejecutar sin instalar el paquete, con solo `python -m pip install pytest`.

## Calidad del código

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy
```

- `ruff check`: linter (errores, imports, modernización de sintaxis y posibles bugs).
- `ruff format --check`: comprueba el formato sin modificar archivos; `ruff format .` lo aplica.
- `mypy`: comprobación estática de tipos en modo estricto sobre `src/` y `tests/`.

La configuración de las tres herramientas está en `pyproject.toml`.

## Estado

La función no valida nombres ni coordenadas. Consulta `docs/incidencia.md`.
