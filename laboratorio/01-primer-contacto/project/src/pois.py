"""Funciones mínimas para construir puntos de interés en GeoJSON."""

from math import isfinite
from typing import Any


def crear_punto(nombre: str, longitud: float, latitud: float) -> dict[str, Any]:
    """Construye una entidad GeoJSON Point para un punto de interés.

    Las coordenadas se reciben como longitud y latitud, en ese orden.
    """
    if not isfinite(longitud) or not -180 <= longitud <= 180:
        raise ValueError("La longitud debe estar entre -180 y 180.")
    if not isfinite(latitud) or not -90 <= latitud <= 90:
        raise ValueError("La latitud debe estar entre -90 y 90.")
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    return {
        "type": "Feature",
        "properties": {"nombre": nombre.strip()},
        "geometry": {
            "type": "Point",
            "coordinates": [longitud, latitud],
        },
    }
