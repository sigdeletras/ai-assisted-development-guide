"""Pruebas de caracterización del comportamiento existente."""

from poi_app.geojson import build_feature


def test_build_feature_returns_geojson_point() -> None:
    feature = build_feature("Mezquita", -4.7794, 37.8791)

    assert feature["type"] == "Feature"
    assert feature["geometry"] == {
        "type": "Point",
        "coordinates": [-4.7794, 37.8791],
    }
    assert feature["properties"] == {"name": "Mezquita"}


def test_build_feature_preserves_additional_properties() -> None:
    feature = build_feature(
        "Biblioteca",
        -4.78,
        37.88,
        {"category": "cultural", "accessible": True},
    )

    assert feature["properties"] == {
        "name": "Biblioteca",
        "category": "cultural",
        "accessible": True,
    }


def test_additional_name_property_currently_overrides_argument() -> None:
    """Caracteriza el comportamiento actual; no lo declara deseable."""
    feature = build_feature(
        "Nombre del argumento",
        -4.78,
        37.88,
        {"name": "Nombre de properties"},
    )

    assert feature["properties"]["name"] == "Nombre de properties"
