dream_vacation = {}

active = True
while active:
    name = input("What is your name?")
    vacation = input("What is your dream vacation spot?")

    dream_vacation[name] = vacation
    repeat = input("Would you like to add another person y/n?")
    
    if repeat == 'n' or repeat == 'no':
        active = False
    for person,spot in dream_vacation.items():
        print(f"{person.title()}'s dream spot is {spot.title()}.")

theme_parks = {}

active_two = True

while active_two:
    name = input("What is your name? ")
    dream_theme = input("What theme park would you like to visit?")

    theme_parks[name] = dream_theme

    repeat = input("Would you like to add another person? y/n ")
    if repeat == 'n' or repeat == 'no':
        active_two = False
    
    print("\n--- Poll Results ---")
    for person,spot in theme_parks.items():
        print(f"{person.title()} would like to visit {spot.title()}")