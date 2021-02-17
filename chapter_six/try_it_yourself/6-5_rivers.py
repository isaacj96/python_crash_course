# Creating a dictionary and printing out the rivers and countries, printing out the keys, printing out the values

# Dictionary List
rivers = {
    'nile': 'egypt',
    'mississippi river': 'united states',
    'yangtze': 'china',
}

# for river and country in dictionary called rivers and printing out each key and value
for r, c in rivers.items():
    print(f"The {r.title()} runs through {c.title()}.")
# for each key
for r in rivers.keys():
    print(f"The name of the river is {r.title()}")
#for each key, get the value
for c in rivers.values():
    print(f"This river is from {c.title()}")
