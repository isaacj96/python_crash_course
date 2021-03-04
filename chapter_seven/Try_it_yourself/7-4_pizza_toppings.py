# Prompt users to enter a series of pizza topping until they inout 'stop'

user_toppings = "\nPlease enter the toppings 1 by 1:"
user_toppings += "\nEnter 'quit' to exit. "

# As they enter each topping, print out a statement saying you're adding that topping.
while True:
    user_input = input(user_toppings)
    if user_input == 'quit':
        break
    else:
        print("I'll add that topping to their pizza")