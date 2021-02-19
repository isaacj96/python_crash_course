# Make a dictionary called favorite Places

favorite_places = {
    'Paco': ['Turkey', 'Not playing with us', 'Mongville'],
    'Alecs': ['KFC'],
    'Jamie': ['Home Gym', 'Grocery Store', 'Indonesia'],
    'Wank': ['Honestly, not a clue'],
}

for person, places in favorite_places.items():
    if(len(places) == 1):
        print(f"{person.title()} favorite place is: ")
        for place in places:
            print(place)
    else:
        print(f"{person.title()} favorite places are:")
        for place in places:
            print(place)