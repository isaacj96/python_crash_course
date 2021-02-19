# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.

cities = {
    'Austin': {
        'State': 'Texas',
        'Country': 'United States',
        'Population': 1_000_000,
        'Fact': 'Has the only nude beach in texas',
    },
    'Barcelona': {
        'State': 'N/A',
        'Country': 'Spain',
        'Population': 1_620_000,
        'Fact': 'Drivers are considered to be the worst in the world',
    },
    'Trondheim': {
        'State': 'N/A',
        'Country': 'Norway',
        'Population': 182_000,
        'Fact': 'City\'s founder was a viking king',
    },
}

for city, information in cities.items():
    print(f"The city, {city.title()} is in {information['State']} {information['Country']}. The population is around {information['Population']}. A interesting fact is: \n{information['Fact']}")