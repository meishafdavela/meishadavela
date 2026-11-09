# exercise11.1/test_cities.py
from city_function import city_country

def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

    result = city_country('paris', 'france')
    assert result == 'Paris, France'

    result = city_country('tokyo', 'japan')
    assert result == 'Tokyo, Japan'
