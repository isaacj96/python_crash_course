# 5-1 Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test.

game_console = 'xbox'
print("Is game_console == 'xbox' I predict True.")
print(game_console == 'xbox')

print("\nIs game_console == 'playstation'? I predict False.")
print(game_console == 'playstation')

print("\nEmployee")
employee_list = ['George', 'Tom', 'Bob', 'Sally']
employee = 'George'
employee_one = 'Kelly'

if employee in employee_list:
    print(True)
else:
    print(False)

if employee not in employee_list:
    print(True)
else:
    print(False)

print("\nNumbers")
number_one = 22
number_two = 18

if number_one >= 20 and number_two >= 20:
    print(True)
else:
    print(False)

if number_one >= 20 or number_two >= 20:
    print(True)
else:
    print(False)

print("Car example")

car = 'Tesla'
if car == 'Toyota':
    print(True)
else:
    print(False)

if car.lower() == 'tesla':
    print(True)
else:
    print(False)

if car != 'Ford':
    print(True)
else:
    print(False)

print("\nIs it true?")
isTrue = True
print(isTrue)
