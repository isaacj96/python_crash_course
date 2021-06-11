from random import choice

my_list = [54, 42, 90, 27, 32, 0, 1, 50, 100, 32, 'b', 'c', 'd', 'e', 'r']

i = 0
x = 4

while i < x:
    winner = choice(my_list)
    print(f"If you have the ticket number or letter {winner} please come forward!")
    i += 1
