cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10500000,
        'fact': 'It is located on the northwest coast of Java.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'Its metropolitan area is one of the largest in the world.',
    },
    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'The Eiffel Tower was completed there in 1889.',
    },
}
for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: about {info['population']}")
    print(f"\tFact: {info['fact']}\n")