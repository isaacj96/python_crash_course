# Write a program that aks the user how many people are in their dinner group. If the answer is more than eight, print a message
# saying they'll have to wait for a table. Otherise report that their table is ready

number_seating = input("How many people will we be seating today? ")
number_seating = int(number_seating)

if number_seating >= 8:
    print("I'm sorry, but you'll have to wait.")
else:
    print("Your table is ready!")