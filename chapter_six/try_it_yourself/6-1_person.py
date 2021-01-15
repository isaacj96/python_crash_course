person = {
    'First Name': 'Robert',
    'Last Name': 'Starke',
    'Age': 23,
    'City': 'Lockhart',
}
print(person)

first_name = person['First Name']
last_name = person['Last Name']
age = person['Age']
city = person['City']

print(f"{first_name}, {last_name}, {age}, {city}")

first_name = person.get('First Name', 'First Name does not exist')
state = person.get('State', 'State was not given')
print(first_name)
print(state)
