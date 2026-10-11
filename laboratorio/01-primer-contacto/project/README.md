# Puntos de interés en GeoJSON

Script mínimo para construir puntos de interés como entidades GeoJSON de tipo `Point` ([RFC 7946](https://www.rfc-editor.org/rfc/rfc7946)).

## Estructura

- `src/pois.py`: función `crear_punto(nombre, longitud, latitud)`.
- `tests/test_pois.py`: pruebas con pytest.

Las coordenadas siguen el orden GeoJSON `[longitud, latitud]`.

## Requisitos

- Python 3.11 o posterior.
- pytest, solo para ejecutar las pruebas.

## Pruebas

Desde este directorio:

```bash
python -m pip install pytest
python -m pytest
```
