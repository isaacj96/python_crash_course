# 7-5 Movie Tickets: A movie theater charges different ticket prices depending on a person's age
# If a person is under the age of 3, the ticket is free;
# If they are between 3 and 12, the ticket is $10;
# And if they are over age 12, the ticket is $15.


# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

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





