# exercise11.2/test_cities.py
from city_functions import city_country


def test_city_country():
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - population 5000000'

    result = city_country('paris', 'france', 2148000)
    assert result == 'Paris, France - population 2148000'

    result = city_country('tokyo', 'japan', 13929286)
    assert result == 'Tokyo, Japan - population 13929286'