# Make several dictionaries, where each dictionary represents a different pet. In each
# dictionary, include the kind of animal and the owner's name.

# Create the dictionary
Milo = {
    'Name': 'Milo',
    'Type': 'Cat',
    'Age': 7,
    'Color': 'Orange',
    'Owner': 'Mikey'
}

Pancho = {
    'Name': 'Pancho',
    'Type': 'Dog',
    'Age': 11,
    'Color': 'Gold',
    'Owner': 'Isaac'
}

Fletcher = {
    'Name': 'Fletcher',
    'Type': 'Dog',
    'Age': 10,
    'Color': 'Mixed',
    'Owner': 'Lilly',
}

# Store the pets as a list
pets = [Milo, Pancho, Fletcher]

#Loop through each pet and it's information
for pet in pets:
    print(f"{pet['Name']} is a {pet['Type']}, is {pet['Age']} and is also {pet['Color']}. The owner of the pet is {pet['Owner']}.")