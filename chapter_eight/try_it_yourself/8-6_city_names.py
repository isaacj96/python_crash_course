def city_country(city, country):
   full_city = f"{city}, {country}"
   return full_city

city_state = city_country('Austin', 'United States')
print(city_state)
city_state = city_country('Mexico City', 'Mexico')
print(city_state)
city_state = city_country('Barcelona', 'Spain')
print(city_state)