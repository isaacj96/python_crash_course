print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) / int(second_number)
except ValueError:
    print("Put in a number!")
else:
    print(answer)
