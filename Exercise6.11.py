# 6.11 Cities
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'It hosted the Summer Olympics in 1964.',
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'The Eiffel Tower was completed there in 1889.',
    },
    'singapore': {
        'country': 'singapore',
        'population': 6_000_000,
        'fact': 'It is both a city and an island country.',
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: about {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")