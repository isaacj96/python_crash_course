rivers = {
    'nile': 'egypt',
    'mississippi river': 'united states',
    'yangtze': 'china',
}

for r, c in rivers.items():
    print(f"The {r.title()} runs through {c.title()}.")

for r in rivers.keys():
    print(f"The name of the river is {r.title()}")
for c in rivers.values():
    print(f"This river is from {c.title()}")
