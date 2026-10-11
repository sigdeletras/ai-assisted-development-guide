"""Funciones de creación de entidades GeoJSON para puntos de interés."""

from typing import Any


def build_feature(
    name: str,
    longitude: float,
    latitude: float,
    properties: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Construye una entidad GeoJSON Point.

    La función conserva el comportamiento inicial del proyecto. La validación
    de nombres y coordenadas es una mejora propuesta en la incidencia del lab.
    """
    feature_properties: dict[str, Any] = {"name": name}
    if properties:
        feature_properties.update(properties)

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [longitude, latitude],
        },
        "properties": feature_properties,
    }
