# Taken program 7-5, do these 3 things

# Use a conditional test in the while statement to stop the loop
# Use an active variable to control how long the loop runs
# Use a break statement to exit the loop when the user enters a 'quit' value.

# This scenario fits the 3rd request
prompt = "\nPlease enter your age:"
prompt += "\nType 'quit' at any point to exit. "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("You're child enters for free!")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    elif age > 12:
        print("The ticket is $15")

# This scenario fits the 1st request
user_input = 1
while user_input <= 5:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("You're child enters for free!")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    elif age > 12:
        print("The ticket is $15")

# This scenario fits the 2nd request
active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False

    age = int(age)

    if age < 3:
        print("You're child enters for free!")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    elif age > 12:
        print("The ticket is $15")



