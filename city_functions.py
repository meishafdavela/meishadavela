# exercise11.2/city_functions.py

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    return f"{city.title()}, {country.title()} - population {population}"