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

## Instalación y pruebas

Desde este directorio:

```bash
python -m pip install pytest
python -m pytest
```

La configuración de pytest está en `pyproject.toml` (`testpaths = ["tests"]`, `pythonpath = ["src"]`), por lo que no es necesario instalar el paquete para ejecutar las pruebas.

## Estado

La función no valida nombres ni coordenadas. Consulta `docs/incidencia.md`.
