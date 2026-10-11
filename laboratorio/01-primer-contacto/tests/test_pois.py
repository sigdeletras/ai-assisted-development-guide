import pytest

from src.pois import crear_punto


def test_crea_feature_geojson_con_coordenadas_en_orden():
    punto = crear_punto("Mezquita", -4.7794, 37.8791)

    assert punto["type"] == "Feature"
    assert punto["properties"]["nombre"] == "Mezquita"
    assert punto["geometry"]["type"] == "Point"
    assert punto["geometry"]["coordinates"] == [-4.7794, 37.8791]


@pytest.mark.parametrize(
    ("longitud", "latitud"),
    [(-180, -90), (180, 90), (0, 0)],
)
def test_acepta_limites_y_origen(longitud, latitud):
    assert crear_punto("Lugar", longitud, latitud)["type"] == "Feature"


@pytest.mark.parametrize(
    ("longitud", "latitud"),
    [(180.1, 0), (-180.1, 0), (0, 90.1), (0, -90.1)],
)
def test_rechaza_coordenadas_fuera_de_rango(longitud, latitud):
    with pytest.raises(ValueError):
        crear_punto("Lugar", longitud, latitud)


@pytest.mark.parametrize(
    ("longitud", "latitud"),
    [(float("nan"), 0), (0, float("inf")), (float("-inf"), 0)],
)
def test_rechaza_coordenadas_no_finitas(longitud, latitud):
    with pytest.raises(ValueError):
        crear_punto("Lugar", longitud, latitud)


def test_rechaza_nombre_vacio():
    with pytest.raises(ValueError):
        crear_punto("   ", 0, 0)
