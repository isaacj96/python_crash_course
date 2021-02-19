#Asl the user for a number, and then report if it's a multiple of 10

user_input = input("Please enter a number: ")
user_input = int(user_input)

if user_input % 10 == 0:
    print("The number is a multiple of 10")
else:
    print("The number is not a multiple of 10")