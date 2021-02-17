# Start with the program you wrote for Excersise 6-1

person = {
    'First Name': 'Robert',
    'Last Name': 'Starke',
    'Age': 23,
    'City': 'Lockhart',
}
""" print(person)

first_name = person['First Name']
last_name = person['Last Name']
age = person['Age']
city = person['City']

print(f"{first_name}, {last_name}, {age}, {city}")

first_name = person.get('First Name', 'First Name does not exist')
state = person.get('State', 'State was not given')
print(first_name)
print(state) """

#Make two new dictionaries representing different people, and store all three dictionaries in a list called people

Albub = {
    'First Name': 'Albus',
    'Last Name': 'Dumbledore',
    'Age': 'Dead',
    'City': 'La la Land'

}

Pancito = {
    'First Name': 'Pancho',
    'Last Name': 'Jaramillo',
    'Age': 11,
    'City': 'Austin',
}

list_of_people = [Albub, person, Pancito]

for person in list_of_people:
    print(f"{person['First Name']} {person['Last Name']} is {person['Age']} and from {person['City']}")