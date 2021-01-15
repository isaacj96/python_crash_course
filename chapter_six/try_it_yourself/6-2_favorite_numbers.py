favorite_numbers = {
    'Robbie': 13,
    'Dillon': 17,
    'Oceane': 5,
    'Alex': 10,
    'Jamie': 10,
}

oceane_fav = favorite_numbers.get('Oceane', 'No favorite number')
alex_fav = favorite_numbers.get('Alex', 'No favorite number')
print(
    f'Robbie\'s favorite number is {favorite_numbers["Robbie"]}, Dillon\'s favorite number is {favorite_numbers["Dillon"]}\
, Oceane\'s favorite number is {oceane_fav}, Alec\'s favorite number is {alex_fav}, Jamie\'s favorite number is \
{favorite_numbers["Jamie"]}')
