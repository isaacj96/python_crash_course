# Modify your program from excersise 6-2(page 99)

# Modify dictionary so a person can have more than 1 favorite number

favorite_numbers = {
    'Robbie': [13, 15, 2],
    'Dillon': [17],
    'Oceane': [5, 7, 10, 15],
    'Alex': [10, 3],
    'Jamie': [10, 1],
}

for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{person.title()}'s favorite number is: ")
        for number in numbers:
            print(number)
    else:
        print(f"{person.title()}'s favorite numbers are: ")
        for number in numbers:
            print(number)