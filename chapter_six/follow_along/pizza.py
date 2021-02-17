#Creating a list inside a dictionary to access it


# Store information of a pizza being ordered.

pizza = {
    'crust': 'thicc',
    'toppings': ['mustrooms', 'extra cheese']
}

# Summarize the order.

print(f"You ordered a {pizza['crust']}-crust pizza " # to break a line, use a "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
