def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    # print(toppings)
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
